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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("selectedVersion","string","Selected SIMO/RIFLEX installation",default='Default'))
        self.attributes.append(Attribute("locations","string","",Dimension("*"),default=""))
        self.attributes.append(Attribute("frevesLocation","string","Freves bin folder",default=""))
        self.attributes.append(Attribute("frelinLocation","string","Frelin bin folder",default=""))