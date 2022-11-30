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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("store","boolean","",default=False))
        self.add_attribute(EnumAttribute("responseAmount","sima/riflex/ResponseAmount",""))
        self.add_attribute(Attribute("timeInterval","number","Desired time interval for storage. A value of 0 gives storage at each time step.",default=0.0))
        self.add_attribute(EnumAttribute("fileFormat","sima/riflex/StorageType",""))
        self.add_attribute(BlueprintAttribute("elements","sima/riflex/ElementReference","Specification of elements for turbine blade response storage",True,Dimension("*")))