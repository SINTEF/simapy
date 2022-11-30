# 
# Generated with RadiationDataGroupBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RadiationDataGroupBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RadiationDataGroup", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("frequencyDependentAddedMass","sima/hydro/FrequencyDependentAddedMass","",True))
        self.add_attribute(BlueprintAttribute("frequencyDependentDamping","sima/hydro/FrequencyDependentDamping","",True))
        self.add_attribute(BlueprintAttribute("retardationFunction","sima/hydro/RetardationFunction","",True))
        self.add_attribute(BlueprintAttribute("addedMassZeroFrequency","sima/hydro/AddedMassZeroFrequency","",True))
        self.add_attribute(BlueprintAttribute("addedMassInfiniteFrequency","sima/hydro/AddedMassInfiniteFrequency","",True))