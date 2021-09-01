# 
# Generated with TurbineBladeResponseStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TurbineBladeResponseStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TurbineBladeResponseStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("store","boolean","",default=False))
        self.attributes.append(EnumAttribute("responseAmount","sima/riflex/ResponseAmount",""))
        self.attributes.append(Attribute("timeInterval","number","Desired time interval for storage. A value of 0 gives storage at each time step.",default=0.0))
        self.attributes.append(EnumAttribute("fileFormat","sima/riflex/StorageType",""))
        self.attributes.append(BlueprintAttribute("elements","sima/riflex/ElementReference","Specification of elements for turbine blade response storage",True,Dimension("size","")))