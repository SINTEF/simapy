# 
# Generated with FrequencyDependentAddedMassBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FrequencyDependentAddedMassBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FrequencyDependentAddedMass", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.attributes.append(BlueprintAttribute("items","sima/hydro/TwoDofData","",True,Dimension("*")))