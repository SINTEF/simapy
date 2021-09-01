# 
# Generated with CoupledFrequencyDependentAddedMassBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CoupledFrequencyDependentAddedMassBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CoupledFrequencyDependentAddedMass", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("frequencies","number","",Dimension("size",""),default=0.0))
        self.attributes.append(BlueprintAttribute("items","sima/hydro/TwoDofData","",True,Dimension("size","")))