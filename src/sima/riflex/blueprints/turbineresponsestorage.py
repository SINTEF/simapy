# 
# Generated with TurbineResponseStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TurbineResponseStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TurbineResponseStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("store","boolean","",default=False))
        self.attributes.append(Attribute("timeInterval","number","Desired time interval for storage. A value of 0 gives storage at each time step.",default=0.0))
        self.attributes.append(EnumAttribute("fileFormat","sima/riflex/StorageType",""))