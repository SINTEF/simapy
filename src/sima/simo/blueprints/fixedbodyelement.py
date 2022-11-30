# 
# Generated with FixedBodyElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class FixedBodyElementBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="FixedBodyElement", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("volume","number","Volume of element",default=0.0))
        self.add_attribute(Attribute("mass","number","Mass of element",default=0.0))
        self.add_attribute(EnumAttribute("waveIntegrationMethod","sima/simo/WaveIntegrationMethod","Parameter defining wave force integration method"))
        self.add_attribute(EnumAttribute("loadType","sima/simo/LoadType","Include gravity and buoyancy forces?"))
        self.add_attribute(EnumAttribute("waveParticleMethod","sima/simo/FixedBodyWaveParticleMethod","Include wave particle velocity and acceleration?"))
        self.add_attribute(BlueprintAttribute("position","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("refPointXAxis","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("refPointXYPlane","sima/sima/Point3","",True))
        self.add_attribute(Attribute("zcoef","number","Vertical position used as reference for depth dependency",default=0.0))
        self.add_attribute(BlueprintAttribute("depthDependentHydrodynamicCoefficients","sima/simo/DepthDependenthydrodynamicCoefficient","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("diffractedWave","sima/hydro/DiffractedWave","",False))
        self.add_attribute(Attribute("c2x","number","Quadratic drag x",default=0.0))
        self.add_attribute(Attribute("c2y","number","Quadratic drag y",default=0.0))
        self.add_attribute(Attribute("c2z","number","Quadratic drag z",default=0.0))
        self.add_attribute(Attribute("c1x","number","Linear drag x",default=0.0))
        self.add_attribute(Attribute("c1y","number","Linear drag y",default=0.0))
        self.add_attribute(Attribute("c1z","number","Linear drag z",default=0.0))
        self.add_attribute(Attribute("amx","number","Added mass x",default=0.0))
        self.add_attribute(Attribute("amy","number","Added mass y",default=0.0))
        self.add_attribute(Attribute("amz","number","Added mass z",default=0.0))