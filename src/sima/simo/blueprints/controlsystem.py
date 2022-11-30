# 
# Generated with ControlSystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ControlSystemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ControlSystem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("relativeBody","sima/simo/SIMOBody","",False))
        self.add_attribute(Attribute("xRef","number","X-coordinate of wanted position",default=0.0))
        self.add_attribute(Attribute("yRef","number","Y-coordinate of wanted position",default=0.0))
        self.add_attribute(Attribute("dirRef","number","Wanted heading",default=0.0))
        self.add_attribute(Attribute("circleXRef","number","X-coordinate of circle center",default=0.0))
        self.add_attribute(Attribute("circleYRef","number","Y-coordinate of circle center ",default=0.0))
        self.add_attribute(Attribute("circleRadius","number","Radius of the circle",default=0.0))
        self.add_attribute(Attribute("xLocal","number","X-coordinate of the point on the body which shall be positioned at the secified reference",default=0.0))
        self.add_attribute(Attribute("yLocal","number","Y-coordinate of the point on the body which shall be positioned at the specified reference",default=0.0))
        self.add_attribute(EnumAttribute("controlReference","sima/simo/ControlReference","Control Reference:\n Global:              Global position\n Body Relative:  Relative to another body\n Waypoint:        Wayoint reference"))
        self.add_attribute(Attribute("xyRelative","boolean","follow body position",default=True))
        self.add_attribute(Attribute("dirRelative","boolean","Follow body heading",default=True))
        self.add_attribute(Attribute("referenceCutOff","number","Cut-off time in low-pass filter for position measurement of body to follow",default=0.0))
        self.add_attribute(BlueprintAttribute("controlConfigurations","sima/simo/DOFControlConfiguration","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("estimator","sima/simo/Estimator","",True))
        self.add_attribute(Attribute("intialXForce","number","Initial x value on non-measured external forces acting on the body",default=0.0))
        self.add_attribute(Attribute("intialYForce","number","Initial y value on non-measured external forces acting on the body",default=0.0))
        self.add_attribute(Attribute("intialMoment","number","Initial value on non-measured external moment acting on the body",default=0.0))
        self.add_attribute(Attribute("windCutOff","number","Cut-off time in low-pass filter for wind measurements",default=0.0))
        self.add_attribute(EnumAttribute("windMeasurement","sima/simo/WindMeasurement","Flag for measurement of wind forces to be included in the controller"))
        self.add_attribute(BlueprintAttribute("allocationSystem","sima/simo/AllocationSystem","",True))
        self.add_attribute(BlueprintAttribute("guidanceSystem","sima/simo/GuidanceSystem","",True))