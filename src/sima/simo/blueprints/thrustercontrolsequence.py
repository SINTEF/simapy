# 
# Generated with ThrusterControlSequenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterControlSequenceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterControlSequence", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("specifyControlSequence","boolean","Should a list of control signals be specified for thruster?",default=False))
        self.add_attribute(EnumAttribute("signalType","sima/simo/ThrustSignalType","Unit for demanded thrust force"))
        self.add_attribute(BlueprintAttribute("items","sima/simo/ControlSequenceItem","",True,Dimension("*")))