# 
# Generated with SoilFrictionElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SoilFrictionElementBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SoilFrictionElement", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("dfric","number","Penetration relative to ZCONT (positive upwards)",default=0.0))
        self.add_attribute(Attribute("ftipdo","number","Depth dependent friction force for DOWNward motion",default=0.0))
        self.add_attribute(Attribute("ftipup","number","Depth dependent friction force for UPward motion",default=0.0))
        self.add_attribute(Attribute("fwall","number","Depth dependent friction force for both upwards and\ndownwards motion",default=0.0))
        self.add_attribute(Attribute("frich","number","Depth dependent friction force in horizontal direction (>=0)",default=0.0))