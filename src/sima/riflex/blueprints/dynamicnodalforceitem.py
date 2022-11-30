# 
# Generated with DynamicNodalForceItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .segmentreference import SegmentReferenceBlueprint

class DynamicNodalForceItemBlueprint(SegmentReferenceBlueprint):
    """"""

    def __init__(self, name="DynamicNodalForceItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("node","integer","Local node/element number within segment",default=0))
        self.add_attribute(Attribute("dof","integer","Degree of freedom within the specified node/element (1-6 at node on end 1, 7-12 at node on end 2)",default=0))
        self.add_attribute(EnumAttribute("coordinateSystem","sima/riflex/CoordinateSystem","Coordinate system code"))
        self.add_attribute(EnumAttribute("forceType","sima/riflex/ForceComponentType","Force component type"))
        self.add_attribute(Attribute("timeOn","number","Time for switching component on",default=0.0))
        self.add_attribute(Attribute("timeOff","number","Time for switching component off",default=0.0))
        self.add_attribute(Attribute("p1","number","Force component parameter 1",default=0.0))
        self.add_attribute(Attribute("p2","number","Force component parameter 2",default=0.0))
        self.add_attribute(Attribute("p3","number","Force component parameter 3",default=0.0))