# 
# Generated with UnitPreferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simapreference import SIMAPreferenceBlueprint

class UnitPreferenceBlueprint(SIMAPreferenceBlueprint):
    """"""

    def __init__(self, name="UnitPreference", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("frequency","sima/sima/Frequency",""))
        self.attributes.append(EnumAttribute("forceUnit","sima/sima/ForceUnit",""))
        self.attributes.append(EnumAttribute("massUnit","sima/sima/MassUnit",""))
        self.attributes.append(EnumAttribute("lengthUnit","sima/sima/LengthUnit",""))
        self.attributes.append(EnumAttribute("powerUnit","sima/sima/PowerUnit",""))