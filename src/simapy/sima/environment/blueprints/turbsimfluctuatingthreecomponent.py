# 
# Generated with TurbSimFluctuatingThreeComponentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class TurbSimFluctuatingThreeComponentBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="TurbSimFluctuatingThreeComponent", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("numSlices","integer","Buffer size: Number of cross-sectional planes (slices) in memory",default=800))
        self.add_attribute(Attribute("windFileName","string","Path and filename for the binary wind file"))
        self.add_attribute(Attribute("sumFileName","string","Path and filename for the summary file from TurbSim"))