# 
# Generated with FluctuatingThreeComponentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class FluctuatingThreeComponentBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="FluctuatingThreeComponent", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("meanSpeed","number","Mean wind speed (along wind propagation direction)",default=0.0))
        self.add_attribute(BlueprintAttribute("velocityProfiles","sima/environment/FluctuatingWindVelocityProfile","",True,Dimension("*")))
        self.add_attribute(Attribute("longitudinalFileName","string","Path and filename for the fluctuating longitudinal wind time series"))
        self.add_attribute(Attribute("lateralFileName","string","Path and filename for the fluctuating lateral wind time series"))
        self.add_attribute(Attribute("verticalFileName","string","Path and filename for the fluctuating vertical wind time series"))
        self.add_attribute(Attribute("lowerLeftX","number","X-coordinate of the lower left corner of the upstream border of the wind",default=0.0))
        self.add_attribute(Attribute("lowerLeftY","number","Y-coordinate of the lower left corner of the wind field domain",default=0.0))
        self.add_attribute(Attribute("lowerLeftZ","number","Z-coordinate of the lower left corner of the wind field domain",default=0.0))
        self.add_attribute(Attribute("numPointsX","integer","Number of grid points in X- (longitudinal) direction",default=0))
        self.add_attribute(Attribute("numPointsY","integer","Number of grid points in Y- (lateral) direction",default=0))
        self.add_attribute(Attribute("numPointsZ","integer","Number of grid points in Z- (vertical) direction",default=0))
        self.add_attribute(Attribute("sizeX","number","Field size in X- (longitudinal) direction",default=0.0))
        self.add_attribute(Attribute("sizeY","number","Field size in Y- (lateral) direction",default=0.0))
        self.add_attribute(Attribute("sizeZ","number","Field size in Z- (vertical) direction",default=0.0))
        self.add_attribute(Attribute("numSlices","integer","Buffer size: Number of wind crossectional planes (Slices) in memory",default=800))