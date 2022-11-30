# 
# Generated with MotionSequenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class MotionSequenceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="MotionSequence", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("start","number","Sequence start time",default=0.0))
        self.add_attribute(Attribute("stop","number","Sequence stop time",default=0.0))
        self.add_attribute(Attribute("deltaPos","number","Change in position during sequence",default=0.0))
        self.add_attribute(Attribute("speed","number","Sequence travelling speed after ramp-up",default=0.0))
        self.add_attribute(Attribute("acceleration","number","Acceleration / retardation for start and stop of sequence",default=0.0))