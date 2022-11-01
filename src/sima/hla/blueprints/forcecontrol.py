# 
# Generated with ForceControlBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.custom.blueprints.customcomponent import CustomComponentBlueprint

class ForceControlBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="ForceControl", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("force","sima/hla/HLAForce","",False))
        self.attributes.append(Attribute("fx","number","",default=0.0))
        self.attributes.append(Attribute("fy","number","",default=0.0))
        self.attributes.append(Attribute("fz","number","",default=0.0))
        self.attributes.append(Attribute("mx","number","",default=0.0))
        self.attributes.append(Attribute("my","number","",default=0.0))
        self.attributes.append(Attribute("mz","number","",default=0.0))