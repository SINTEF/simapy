# 
# Generated with ControlSequenceItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ControlSequenceItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ControlSequenceItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("time","number","Time when signal is activated",default=0.0))
        self.attributes.append(Attribute("thrust","number","Thrust demand",default=0.0))
        self.attributes.append(Attribute("direction","number","Demanded thrust force direction",default=0.0))
        self.attributes.append(Attribute("acceptDPSystemInput","boolean","Should signals from DP system be accepted?",default=False))