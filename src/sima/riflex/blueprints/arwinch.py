# 
# Generated with ARWinchBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .segmentreference import SegmentReferenceBlueprint
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ARWinchBlueprint(SegmentReferenceBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="ARWinch", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(EnumAttribute("segmentEnd","sima/riflex/End","End of segment (and line) attached to winch (1 or 2)"))
        self.attributes.append(Attribute("relativeSegmentLength","number","Relative segment length where segment is attached to winch point",default=0.0))
        self.attributes.append(Attribute("x1","number","X-coordinate for static equilibrium position",default=0.0))
        self.attributes.append(Attribute("y1","number","Y-coordinate for static equilibrium position",default=0.0))
        self.attributes.append(Attribute("z1","number","Z-coordinate for static equilibrium position",default=0.0))
        self.attributes.append(Attribute("rotation","number","Specified rotation of supernode from stress free position to static equilibrium position.",default=0.0))
        self.attributes.append(Attribute("rotationDirection","number","Direction of axis for specified rotation",default=0.0))
        self.attributes.append(BlueprintAttribute("attachedBody","sima/sima/Body","",False))
        self.attributes.append(Attribute("maxVelocity","number","Maximum winch velocity",default=0.0))
        self.attributes.append(Attribute("timeToMaxVelocity","number","Time to reach maximum velocity (from zero)",default=0.0))
        self.attributes.append(Attribute("lineRelease","boolean","Line release when no more line on winch (Dynamic analysis)",default=False))
        self.attributes.append(Attribute("radius","number","Radius of winch",default=0.0))
        self.attributes.append(EnumAttribute("winchCenter","sima/riflex/CenterOfWinch","Center of winch in positive or negative local Z-axis"))
        self.attributes.append(Attribute("lengthJustification","boolean","Control parameter for adjusting the length of elements attached to winch",default=False))