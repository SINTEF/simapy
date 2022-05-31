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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("massCoefficient","number","Mass / unit length",default=0.0))
        self.attributes.append(Attribute("extCrossSectionalArea","number","External cross-sectional area",default=0.0))
        self.attributes.append(Attribute("intCrossSectionalArea","number","Internal cross-sectional area",default=0.0))
        self.attributes.append(Attribute("gyrationRadius","number","Radius of gyration about local x-axis",default=0.0))
        self.attributes.append(Attribute("crossSectionArea","number","Cross-section area for stress calculations",default=0.0))
        self.attributes.append(Attribute("crossSectionModulus","number","Cross-section modulus for stress calculations",default=0.0))
        self.attributes.append(Attribute("diameter","number","Diameter for stress calculations (default = 2 * sqrt(external area/pi))",default=0.0))
        self.attributes.append(Attribute("thickness","number","Thickness for stress calculations (default = sqrt(external area/pi) - sqrt(internal area/pi))",default=0.0))
        self.attributes.append(Attribute("defaultStressCalculation","boolean","Use default stress calculation settings",default=True))
        self.attributes.append(Attribute("extContactRadius","number","External contact radius (default = 0.0)",default=0.0))
        self.attributes.append(Attribute("innerContactRadius","number","Inner contact radius (default = 0.0)",default=0.0))