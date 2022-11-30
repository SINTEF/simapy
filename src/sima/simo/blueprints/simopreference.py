# 
# Generated with SIMOPreferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.simapreference import SIMAPreferenceBlueprint

class SIMOPreferenceBlueprint(SIMAPreferenceBlueprint):
    """"""

    def __init__(self, name="SIMOPreference", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("selectedVersion","string","Selected SIMO/RIFLEX installation",default='Default'))
        self.add_attribute(Attribute("locations","string","",Dimension("*")))
        self.add_attribute(Attribute("frevesLocation","string","Freves bin folder"))
        self.add_attribute(Attribute("frelinLocation","string","Frelin bin folder"))