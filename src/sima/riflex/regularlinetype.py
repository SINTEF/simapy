# This an autogenerated file
# 
# Generated with RegularLineType
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.regularlinetype import RegularLineTypeBlueprint
from typing import Dict
from sima.riflex.arlinetype import ARLineType
from sima.riflex.regularsegment import RegularSegment
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.internalfluidtype import InternalFluidType
    from sima.riflex.nodalcomponenttype import NodalComponentType

class RegularLineType(ARLineType):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    internalFluid : InternalFluidType
         Internal fluid component type.
    endComponent : NodalComponentType
         Nodal component type number for attached body or connector at end 2 of rthe last segment.
    segments : List[RegularSegment]
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.internalFluid = None
        self.endComponent = None
        self.segments = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RegularLineTypeBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def internalFluid(self) -> InternalFluidType:
        """Internal fluid component type."""
        return self.__internalFluid

    @internalFluid.setter
    def internalFluid(self, value: InternalFluidType):
        """Set internalFluid"""
        self.__internalFluid = value

    @property
    def endComponent(self) -> NodalComponentType:
        """Nodal component type number for attached body or connector at end 2 of rthe last segment."""
        return self.__endComponent

    @endComponent.setter
    def endComponent(self, value: NodalComponentType):
        """Set endComponent"""
        self.__endComponent = value

    @property
    def segments(self) -> List[RegularSegment]:
        """"""
        return self.__segments

    @segments.setter
    def segments(self, value: List[RegularSegment]):
        """Set segments"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__segments = value
