# 
# Generated with StabilityCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StabilityCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StabilityCalculationParameters", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("forceTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=100.0))
        self.add_attribute(Attribute("momentTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=1000.0))
        self.add_attribute(BlueprintAttribute("staticEquilibriumBodies","sima/simo/StaticEquilibriumBody","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("restrainFromGlobalDOFBodies","sima/simo/DOFElimination","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("body","sima/simo/SIMOBody","Body for which GZ-curve will be calculated",False))
        self.add_attribute(Attribute("minAzimuthAngle","number","Minimum angle of the azimuth axis of rotation (body-related coordinate system)",default=0.0))
        self.add_attribute(Attribute("maxAzimuthAngle","number","Maximum angle of the azimuth axis of rotation (body-related coordinate system)",default=0.0))
        self.add_attribute(Attribute("numAzimuthValues","integer","",default=0))
        self.add_attribute(Attribute("minRotationAngle","number","Minimum inclination angle about the azimuth axis",default=0.0))
        self.add_attribute(Attribute("maxRotationAngle","number","Maximum inclination angle about the azimuth axis",default=0.0))
        self.add_attribute(Attribute("numRotationvalues","integer","",default=0))