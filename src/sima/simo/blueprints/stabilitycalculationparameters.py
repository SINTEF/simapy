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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("forceTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=100.0))
        self.attributes.append(Attribute("momentTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=1000.0))
        self.attributes.append(BlueprintAttribute("staticEquilibriumBodies","sima/simo/StaticEquilibriumBody","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("restrainFromGlobalDOFBodies","sima/simo/DOFElimination","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("body","sima/simo/SIMOBody","Body for which GZ-curve will be calculated",False))
        self.attributes.append(Attribute("minAzimuthAngle","number","Minimum angle of the azimuth axis of rotation (body-related coordinate system)",default=0.0))
        self.attributes.append(Attribute("maxAzimuthAngle","number","Maximum angle of the azimuth axis of rotation (body-related coordinate system)",default=0.0))
        self.attributes.append(Attribute("numAzimuthValues","integer","",default=0))
        self.attributes.append(Attribute("minRotationAngle","number","Minimum inclination angle about the azimuth axis",default=0.0))
        self.attributes.append(Attribute("maxRotationAngle","number","Maximum inclination angle about the azimuth axis",default=0.0))
        self.attributes.append(Attribute("numRotationvalues","integer","",default=0))