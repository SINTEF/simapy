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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("volume","number","Volume of element",default=0.0))
        self.attributes.append(Attribute("mass","number","Mass of element",default=0.0))
        self.attributes.append(EnumAttribute("waveIntegrationMethod","sima/simo/WaveIntegrationMethod","Parameter defining wave force integration method"))
        self.attributes.append(EnumAttribute("loadType","sima/simo/LoadType","Include gravity and buoyancy forces?"))
        self.attributes.append(EnumAttribute("waveParticleMethod","sima/simo/FixedBodyWaveParticleMethod","Include wave particle velocity and acceleration?"))
        self.attributes.append(BlueprintAttribute("position","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("refPointXAxis","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("refPointXYPlane","sima/sima/Point3","",True))
        self.attributes.append(Attribute("zcoef","number","Vertical position used as reference for depth dependency",default=0.0))
        self.attributes.append(BlueprintAttribute("depthDependentHydrodynamicCoefficients","sima/simo/DepthDependenthydrodynamicCoefficient","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("diffractedWave","sima/hydro/DiffractedWave","",False))
        self.attributes.append(Attribute("c2x","number","Quadratic drag x",default=0.0))
        self.attributes.append(Attribute("c2y","number","Quadratic drag y",default=0.0))
        self.attributes.append(Attribute("c2z","number","Quadratic drag z",default=0.0))
        self.attributes.append(Attribute("c1x","number","Linear drag x",default=0.0))
        self.attributes.append(Attribute("c1y","number","Linear drag y",default=0.0))
        self.attributes.append(Attribute("c1z","number","Linear drag z",default=0.0))
        self.attributes.append(Attribute("amx","number","Added mass x",default=0.0))
        self.attributes.append(Attribute("amy","number","Added mass y",default=0.0))
        self.attributes.append(Attribute("amz","number","Added mass z",default=0.0))