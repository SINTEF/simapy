# 
# Generated with DiffractedWaveBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DiffractedWaveBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DiffractedWave", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("referencePoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("elevation","sima/hydro/DiffractedWaveElevation","",True))
        self.attributes.append(BlueprintAttribute("velocity","sima/hydro/DiffractedWaveVelocity","",True))