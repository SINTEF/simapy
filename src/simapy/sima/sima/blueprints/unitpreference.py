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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("frequency","sima/sima/Frequency",""))
        self.add_attribute(EnumAttribute("forceUnit","sima/sima/ForceUnit",""))
        self.add_attribute(EnumAttribute("massUnit","sima/sima/MassUnit",""))
        self.add_attribute(EnumAttribute("lengthUnit","sima/sima/LengthUnit",""))
        self.add_attribute(EnumAttribute("powerUnit","sima/sima/PowerUnit",""))