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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.attributes.append(Attribute("numSlices","integer","Buffer size: Number of cross-sectional planes (slices) in memory",default=800))
        self.attributes.append(Attribute("windFileName","string","Path and filename for the binary wind file",default=""))
        self.attributes.append(Attribute("sumFileName","string","Path and filename for the summary file from TurbSim",default=""))