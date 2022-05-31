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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("frequencyDependentAddedMass","sima/hydro/CoupledFrequencyDependentAddedMass","",True))
        self.attributes.append(BlueprintAttribute("frequencyDependentDamping","sima/hydro/CoupledFrequencyDependentDamping","",True))
        self.attributes.append(BlueprintAttribute("retardationFunction","sima/hydro/CoupledRetardationFunction","",True))
        self.attributes.append(BlueprintAttribute("addedMassZeroFrequency","sima/hydro/CoupledAddedMassZeroFrequency","",True))
        self.attributes.append(BlueprintAttribute("addedMassInfiniteFrequency","sima/hydro/CoupledAddedMassInfiniteFrequency","",True))