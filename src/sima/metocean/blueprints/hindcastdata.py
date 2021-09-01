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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("dataFile","string","",default=""))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("firstDate","string","",default=""))
        self.attributes.append(Attribute("lastDate","string","",default=""))
        self.attributes.append(BlueprintAttribute("waveData","sima/metocean/HindcastWaveContainer","",True))
        self.attributes.append(BlueprintAttribute("windData","sima/metocean/HindcastLevelContainer","",True))
        self.attributes.append(BlueprintAttribute("currentData","sima/metocean/HindcastLevelContainer","",True))