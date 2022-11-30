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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("length","number","Length",default=10.0))
        self.add_attribute(Attribute("width","number","Width",default=5.0))
        self.add_attribute(Attribute("height","number","Height",default=5.0))
        self.add_attribute(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
        self.add_attribute(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.add_attribute(BlueprintAttribute("viewpoints","sima/sima/BodyViewpoint","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("firstOrderMotionTransferFunction","sima/hydro/FirstOrderMotionTransferFunction","",True))
        self.add_attribute(BlueprintAttribute("diffractedWaveFields","sima/hydro/DiffractedWaveField","",True,Dimension("*")))