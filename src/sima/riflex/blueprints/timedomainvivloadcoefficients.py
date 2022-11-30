# 
# Generated with TimeDomainVIVLoadCoefficientsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TimeDomainVIVLoadCoefficientsBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TimeDomainVIVLoadCoefficients", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("vivLoadFormulation","sima/riflex/VIVLoadFormulation",""))
        self.add_attribute(Attribute("cv","number","Vortex shedding load coefficient for cross-flow excitation (nondimensional)",default=0.0))
        self.add_attribute(Attribute("fnull","number","Natural cross-flow vortex shedding frequency (nondimensional)",default=0.0))
        self.add_attribute(Attribute("fmin","number","Minimum cross-flow vortex shedding frequency (nondimensional)",default=0.0))
        self.add_attribute(Attribute("fmax","number","Maximum cross-flow vortex shedding frequency (nondimensional)",default=0.0))
        self.add_attribute(Attribute("nmem","integer","Number of time steps used in calculation of standard deviation",default=500))
        self.add_attribute(Attribute("cvil","number","Load coefficient for in-line excitation",default=0.0))
        self.add_attribute(Attribute("alphil","number","Nondimensional parameter giving freedom to in-line excitation frequency",default=0.0))
        self.add_attribute(Attribute("chh","number","Higher harmonic load coefficient (nondimensional)",default=0.0))
        self.add_attribute(Attribute("fnullil","number","Natural in-line vortex shedding frequency (nondimensional)",default=0.0))
        self.add_attribute(Attribute("fminil","number","Minimum in-line vortex shedding frequency (nondimensional)",default=0.0))
        self.add_attribute(Attribute("fmaxil","number","Maximum in-line vortex shedding frequency (nondimensional)",default=0.0))