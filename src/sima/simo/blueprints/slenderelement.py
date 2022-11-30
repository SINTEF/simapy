# 
# Generated with SlenderElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class SlenderElementBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="SlenderElement", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("specificVolume","number","Specific volume (cross-section area) of element",default=0.0))
        self.add_attribute(Attribute("distributedMass","number","Distributed mass of element",default=0.0))
        self.add_attribute(EnumAttribute("waveIntegrationMethod","sima/simo/WaveIntegrationMethod","Wave force integration method"))
        self.add_attribute(EnumAttribute("loadType","sima/simo/LoadType","Parameter for load types"))
        self.add_attribute(EnumAttribute("waveParticleMethod","sima/simo/WaveParticleMethod","Wave particle options"))
        self.add_attribute(Attribute("numberOfStrips","integer","Number of strips",default=10))
        self.add_attribute(BlueprintAttribute("endPoint1","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("endPoint2","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("referencePoint","sima/sima/Point3","",True))
        self.add_attribute(Attribute("zcoef","number","Vertical position used as reference for depth dependency",default=0.0))
        self.add_attribute(BlueprintAttribute("depthDependentHydrodynamicCoefficients","sima/simo/DepthDependenthydrodynamicCoefficient","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("diffractedWaveEnd1","sima/hydro/DiffractedWave","",False))
        self.add_attribute(BlueprintAttribute("diffractedWaveEnd2","sima/hydro/DiffractedWave","",False))
        self.add_attribute(Attribute("c2x","number","Quadratic drag x",default=0.0))
        self.add_attribute(Attribute("c2y","number","Quadratic drag y",default=0.0))
        self.add_attribute(Attribute("c2z","number","Quadratic drag z",default=0.0))
        self.add_attribute(Attribute("c1x","number","Linear drag x",default=0.0))
        self.add_attribute(Attribute("c1y","number","Linear drag y",default=0.0))
        self.add_attribute(Attribute("c1z","number","Linear drag z",default=0.0))
        self.add_attribute(Attribute("amx","number","Added mass x",default=0.0))
        self.add_attribute(Attribute("amy","number","Added mass y",default=0.0))
        self.add_attribute(Attribute("amz","number","Added mass z",default=0.0))
        self.add_attribute(Attribute("windForces","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("aerodynamicDescription","sima/simo/AerodynamicDescription","",True))