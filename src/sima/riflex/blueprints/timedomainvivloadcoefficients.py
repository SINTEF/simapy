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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("vivLoadFormulation","sima/riflex/VIVLoadFormulation",""))
        self.attributes.append(Attribute("cv","number","Vortex shedding load coefficient for cross-flow excitation (nondimensional)",default=0.0))
        self.attributes.append(Attribute("fnull","number","Natural cross-flow vortex shedding frequency (nondimensional)",default=0.0))
        self.attributes.append(Attribute("fmin","number","Minimum cross-flow vortex shedding frequency (nondimensional)",default=0.0))
        self.attributes.append(Attribute("fmax","number","Maximum cross-flow vortex shedding frequency (nondimensional)",default=0.0))
        self.attributes.append(Attribute("nmem","integer","Number of time steps used in calculation of standard deviation",default=500))
        self.attributes.append(Attribute("cvil","number","Load coefficient for in-line excitation",default=0.0))
        self.attributes.append(Attribute("alphil","number","Nondimensional parameter giving freedom to in-line excitation frequency",default=0.0))
        self.attributes.append(Attribute("chh","number","Higher harmonic load coefficient (nondimensional)",default=0.0))
        self.attributes.append(Attribute("fnullil","number","Natural in-line vortex shedding frequency (nondimensional)",default=0.0))
        self.attributes.append(Attribute("fminil","number","Minimum in-line vortex shedding frequency (nondimensional)",default=0.0))
        self.attributes.append(Attribute("fmaxil","number","Maximum in-line vortex shedding frequency (nondimensional)",default=0.0))