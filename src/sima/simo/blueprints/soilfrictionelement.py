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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("dfric","number","Penetration relative to ZCONT (positive upwards)",default=0.0))
        self.attributes.append(Attribute("ftipdo","number","Depth dependent friction force for DOWNward motion",default=0.0))
        self.attributes.append(Attribute("ftipup","number","Depth dependent friction force for UPward motion",default=0.0))
        self.attributes.append(Attribute("fwall","number","Depth dependent friction force for both upwards and\ndownwards motion",default=0.0))
        self.attributes.append(Attribute("frich","number","Depth dependent friction force in horizontal direction (>=0)",default=0.0))