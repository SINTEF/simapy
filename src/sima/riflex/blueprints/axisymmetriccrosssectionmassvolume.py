# 
# Generated with AxisymmetricCrossSectionMassVolumeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AxisymmetricCrossSectionMassVolumeBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AxisymmetricCrossSectionMassVolume", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("massCoefficient","number","Mass / unit length",default=0.0))
        self.add_attribute(Attribute("extCrossSectionalArea","number","External cross-sectional area",default=0.0))
        self.add_attribute(Attribute("intCrossSectionalArea","number","Internal cross-sectional area",default=0.0))
        self.add_attribute(Attribute("gyrationRadius","number","Radius of gyration about local x-axis",default=0.0))
        self.add_attribute(Attribute("crossSectionArea","number","Cross-section area for stress calculations",default=0.0))
        self.add_attribute(Attribute("crossSectionModulus","number","Cross-section modulus for stress calculations",default=0.0))
        self.add_attribute(Attribute("diameter","number","Diameter for stress calculations (default = 2 * sqrt(external area/pi))",default=0.0))
        self.add_attribute(Attribute("thickness","number","Thickness for stress calculations (default = sqrt(external area/pi) - sqrt(internal area/pi))",default=0.0))
        self.add_attribute(Attribute("defaultStressCalculation","boolean","Use default stress calculation settings",default=True))
        self.add_attribute(Attribute("extContactRadius","number","External contact radius (default = 0.0)",default=0.0))
        self.add_attribute(Attribute("innerContactRadius","number","Inner contact radius (default = 0.0)",default=0.0))