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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("relativeBody","sima/simo/SIMOBody","",False))
        self.attributes.append(Attribute("xRef","number","X-coordinate of wanted position",default=0.0))
        self.attributes.append(Attribute("yRef","number","Y-coordinate of wanted position",default=0.0))
        self.attributes.append(Attribute("dirRef","number","Wanted heading",default=0.0))
        self.attributes.append(Attribute("circleXRef","number","X-coordinate of circle center",default=0.0))
        self.attributes.append(Attribute("circleYRef","number","Y-coordinate of circle center ",default=0.0))
        self.attributes.append(Attribute("circleRadius","number","Radius of the circle",default=0.0))
        self.attributes.append(Attribute("xLocal","number","X-coordinate of the point on the body which shall be positioned at the secified reference",default=0.0))
        self.attributes.append(Attribute("yLocal","number","Y-coordinate of the point on the body which shall be positioned at the specified reference",default=0.0))
        self.attributes.append(EnumAttribute("controlReference","sima/simo/ControlReference","Control Reference:\n Global:              Global position\n Body Relative:  Relative to another body\n Waypoint:        Wayoint reference"))
        self.attributes.append(Attribute("xyRelative","boolean","follow body position",default=True))
        self.attributes.append(Attribute("dirRelative","boolean","Follow body heading",default=True))
        self.attributes.append(Attribute("referenceCutOff","number","Cut-off time in low-pass filter for position measurement of body to follow",default=0.0))
        self.attributes.append(BlueprintAttribute("controlConfigurations","sima/simo/DOFControlConfiguration","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("estimator","sima/simo/Estimator","",True))
        self.attributes.append(Attribute("intialXForce","number","Initial x value on non-measured external forces acting on the body",default=0.0))
        self.attributes.append(Attribute("intialYForce","number","Initial y value on non-measured external forces acting on the body",default=0.0))
        self.attributes.append(Attribute("intialMoment","number","Initial value on non-measured external moment acting on the body",default=0.0))
        self.attributes.append(Attribute("windCutOff","number","Cut-off time in low-pass filter for wind measurements",default=0.0))
        self.attributes.append(EnumAttribute("windMeasurement","sima/simo/WindMeasurement","Flag for measurement of wind forces to be included in the controller"))
        self.attributes.append(BlueprintAttribute("allocationSystem","sima/simo/AllocationSystem","",True))
        self.attributes.append(BlueprintAttribute("guidanceSystem","sima/simo/GuidanceSystem","",True))