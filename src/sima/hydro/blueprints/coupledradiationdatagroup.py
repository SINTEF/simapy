# 
# Generated with CoupledRadiationDataGroupBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CoupledRadiationDataGroupBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CoupledRadiationDataGroup", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("frequencyDependentAddedMass","sima/hydro/CoupledFrequencyDependentAddedMass","",True))
        self.add_attribute(BlueprintAttribute("frequencyDependentDamping","sima/hydro/CoupledFrequencyDependentDamping","",True))
        self.add_attribute(BlueprintAttribute("retardationFunction","sima/hydro/CoupledRetardationFunction","",True))
        self.add_attribute(BlueprintAttribute("addedMassZeroFrequency","sima/hydro/CoupledAddedMassZeroFrequency","",True))
        self.add_attribute(BlueprintAttribute("addedMassInfiniteFrequency","sima/hydro/CoupledAddedMassInfiniteFrequency","",True))