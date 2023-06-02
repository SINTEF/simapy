""" Read entities from SIMA s5 file"""
import json
from collections import OrderedDict
from importlib import import_module
from typing import Callable, Dict, Sequence

import h5py as h5
import numpy as np
from dmt.attribute import Attribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.entity import Entity
from dmt.enum_attribute import EnumAttribute

from sima import signals as containers


class S5Reader:
    """Read entities from S5 file"""

    class Reference:
        """Holds a reference until it can be resolved"""

        def __init__(self, entity, prop: Attribute, uid: str):
            self.entity = entity
            self.prop = prop
            self.uid = uid

    def __init__(
        self, external_refs: Dict[str, Entity] = None, root_package: str = None
    ):
        self.root_package: str = root_package
        self.entities = dict()
        self.unresolved = list()
        self.external_refs = dict()
        if external_refs:
            self.external_refs = external_refs
        self.datasource = None
        self.__h5_file = None

    def read(self, filename) -> Sequence[Entity]:
        """Read entities from s5 file"""
        entities = []
        with h5.File(filename, "r") as root:
            vds: h5.Dataset = root["version"]
            self.__h5_file = root
            version = vds.asstr()[0]
            if version != "2.0.0":
                raise ValueError(f"Unsupported version {version}")
            signals: h5.Dataset = root["signals"]
            json_data = signals.asstr()[0]
            entities_dict = json.loads(json_data)
            for name, dicts in entities_dict.items():
                entities.extend(self.__read_group(name, dicts))

        self.__resolve_all()
        return entities

    def __resolve_all(self):
        for ref in self.unresolved:
            if not self.__resolve(ref):
                raise ValueError(f"Unresolved reference: {ref}")

    def __read_group(self, name, e_dicts: Sequence[Dict]) -> Entity:
        """Read entities from Dict"""
        if name == "c":
            entities = []
            for e_dict in e_dicts:
                entities.append(self.__read_container(e_dict))
            return entities

        entity_type: str = e_dict.attrs["type"]
        constructor = self._resolve_type(entity_type)
        if not constructor:
            raise ValueError(f"Unkown entity type {entity_type}")
        entity_instance: Entity = constructor()
        blueprint = entity_instance.blueprint
        for name, node in e_dict.items():
            if name == "_id":
                uid = node[()].decode()
                self.entities[uid] = entity_instance
                continue
            attribute = blueprint.get_attribute(name)
            if not attribute:
                # FIXME
                continue
            if isinstance(attribute, BlueprintAttribute):
                self.__set_blueprint_value(entity_instance, attribute, node)
            elif attribute.is_enum:
                value = node[()].decode()
                self.__set_enum_value(entity_instance, attribute, value)
            else:
                value = node[()]
                if attribute.is_string():
                    if attribute.has_dimensions():
                        setattr(entity_instance, name, value.astype(str))
                    else:
                        setattr(entity_instance, name, value.decode())
                else:
                    setattr(entity_instance, name, value)

        return entity_instance

    def __read_container(self, e_dict: Dict) -> containers.Container:
        c = containers.Container(name=e_dict["name"])
        c_dicts = e_dict.get("c")
        if c_dicts:
            for c_dict in c_dicts:
                c.containers.append(self.__read_container(c_dict))
        s_dicts = e_dict.get("s")
        if s_dicts:
            for s_dict in s_dicts:
                s = self.__read_signal(s_dict)
                if s:
                    c.signals.append(s)
                    s_p_dicts = s_dict.get("p")
                    if s_p_dicts:
                        self.__read_attributes(s_p_dicts,s.attributes)

        p_dicts = e_dict.get("p")
        if p_dicts:
            self.__read_attributes(p_dicts,c.attributes)
        return c

    def __read_attributes(self, p_dict: Dict,attributes: Sequence[Attribute]) -> None:
        """Read attribute from Dict"""
        for name, value in p_dict.items():
            attributes.append(containers.Attribute(name=name, value=value))


    def __read_signal(self, s_dict: Dict) -> containers.Signal:
        sname = s_dict["name"]
        for name, dvalue in s_dict.items():
            if name == "n":
                return containers.DimensionalScalar(
                    name=sname, value=dvalue["v"], unit=dvalue.get("yunit")
                )
            if name == "ns":
                signal = containers.EquallySpacedSignal(name=sname)
                signal.xdelta = dvalue.get("dlt", signal.xdelta)
                signal.xunit = dvalue.get("xunit", signal.xunit)
                signal.unit = dvalue.get("yunit", signal.unit)
                signal.xstart = dvalue.get("st", signal.xstart)
                path = dvalue.get("path")
                if path:
                    # Found within the h5-file..
                    signal.value = self.__h5_file[path]
                else:
                    signal.value = dvalue["v"]
                return signal
            if name == "xy":
                signal = containers.NonEquallySpacedSignal(name=sname)
                props = s_dict.get("p",{})
                for name, value in props.items():
                    if name == "ylabel":
                        name = "label"
                    setattr(signal, name, value)

                signal.xunit = dvalue.get("xunit", signal.xunit)
                signal.unit = dvalue.get("yunit", signal.unit)
                path = dvalue.get("path")
                if path:
                    # Found within the h5-file..
                    ds = self.__h5_file[path]
                    sets = np.split(ds, 2)
                    signal.xvalue = sets[0]
                    signal.value = sets[1]
                return signal
            elif name == "s":
                return containers.SimpleString(name=sname, value=dvalue["v"])
            elif name == "i":
                return containers.IntegerScalar(name=sname, value=dvalue["v"])
            elif name == "b":
                return containers.SimpleBoolean(name=sname, value=dvalue["v"])
            elif name == "ss":
                path = dvalue.get("path")
                if path:
                    # Found within the h5-file..
                    ds = self.__h5_file[path].asstr()
                    return containers.StringArray(name=sname, value=ds)
                return containers.StringArray(name=sname, value=dvalue["v"])

        raise ValueError("Unexpected signal type:" + json.dumps(s_dict))

    def _resolve_type(self, atype: str) -> Callable:
        pkg: any = None
        parts = atype.split("/")
        if self.datasource:
            parts.remove(self.datasource)
        if parts[0] == "":
            del parts[0]
        ename = parts.pop()
        package_path = ".".join(parts)
        if self.root_package:
            package_path = self.root_package + "." + package_path
        try:
            pkg = import_module(package_path)
        except ModuleNotFoundError as error:
            raise Exception(f"Unable to load package {package_path}") from error

        constructor = pkg.__dict__.get(ename)
        return constructor

    def __set_blueprint_value(
        self, entity_instance: Entity, attribute: BlueprintAttribute, value
    ):
        if attribute.contained:
            self.__set_value(entity_instance, attribute, value)
        else:
            self.__set_reference(entity_instance, attribute, value)

    def __set_reference(
        self, entity_instance: Entity, prop: Attribute, group: h5.Group
    ):
        uid = group.get("_id")[()].decode()
        ref = self.Reference(entity_instance, prop, uid)
        if not self.__resolve(ref):
            self.unresolved.append(ref)
        return

    def __set_value(
        self, entity_instance: Entity, attribute: BlueprintAttribute, value
    ):
        if attribute.has_dimensions():
            root: h5.Group = value
            od = OrderedDict()
            children = []
            for name, v in root.items():
                od[name] = self.__read_group(v)

            order = root.attrs.get("order")
            if order is not None:
                sorder = order[()]
                for name in sorder:
                    children.append(od[name])
            else:
                children = list(od.values())
            setattr(entity_instance, attribute.name, children)
        else:
            setattr(entity_instance, attribute.name, self.__read_group(value))

    def __resolve(self, ref: Reference):
        value = self.entities.get(ref.uid, self.external_refs.get(ref.uid, None))
        if value:
            setattr(ref.entity, ref.prop.name, value)
            return True

        return False

    def __set_enum_value(self, entity: Entity, attribute: EnumAttribute, value: str):
        """Convert from string to Enum"""

        constructor = self._resolve_type(attribute.type)
        if not constructor:
            raise Exception(f"Unkown Enum type {attribute.type}")
        evalue = constructor[value]
        setattr(entity, attribute.name, evalue)
