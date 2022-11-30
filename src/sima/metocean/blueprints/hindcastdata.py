# 
# Generated with HindcastDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class HindcastDataBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="HindcastData", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("dataFile","string",""))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("firstDate","string",""))
        self.add_attribute(Attribute("lastDate","string",""))
        self.add_attribute(BlueprintAttribute("waveData","sima/metocean/HindcastWaveContainer","",True))
        self.add_attribute(BlueprintAttribute("windData","sima/metocean/HindcastLevelContainer","",True))
        self.add_attribute(BlueprintAttribute("currentData","sima/metocean/HindcastLevelContainer","",True))