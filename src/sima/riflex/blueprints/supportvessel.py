# 
# Generated with SupportVesselBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.body import BodyBlueprint

class SupportVesselBlueprint(BodyBlueprint):
    """"""

    def __init__(self, name="SupportVessel", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("length","number","Length",default=10.0))
        self.attributes.append(Attribute("width","number","Width",default=5.0))
        self.attributes.append(Attribute("height","number","Height",default=5.0))
        self.attributes.append(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
        self.attributes.append(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.attributes.append(BlueprintAttribute("viewpoints","sima/sima/BodyViewpoint","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("firstOrderMotionTransferFunction","sima/hydro/FirstOrderMotionTransferFunction","",True))
        self.attributes.append(BlueprintAttribute("diffractedWaveFields","sima/hydro/DiffractedWaveField","",True,Dimension("size","")))