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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("frequencyDependentAddedMass","sima/hydro/FrequencyDependentAddedMass","",True))
        self.attributes.append(BlueprintAttribute("frequencyDependentDamping","sima/hydro/FrequencyDependentDamping","",True))
        self.attributes.append(BlueprintAttribute("retardationFunction","sima/hydro/RetardationFunction","",True))
        self.attributes.append(BlueprintAttribute("addedMassZeroFrequency","sima/hydro/AddedMassZeroFrequency","",True))
        self.attributes.append(BlueprintAttribute("addedMassInfiniteFrequency","sima/hydro/AddedMassInfiniteFrequency","",True))