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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(Attribute("node","integer","Local node/element number within segment",default=0))
        self.attributes.append(Attribute("dof","integer","Degree of freedom within the specified node/element (1-6 at node on end 1, 7-12 at node on end 2)",default=0))
        self.attributes.append(EnumAttribute("coordinateSystem","sima/riflex/CoordinateSystem","Coordinate system code"))
        self.attributes.append(EnumAttribute("forceType","sima/riflex/ForceComponentType","Force component type"))
        self.attributes.append(Attribute("timeOn","number","Time for switching component on",default=0.0))
        self.attributes.append(Attribute("timeOff","number","Time for switching component off",default=0.0))
        self.attributes.append(Attribute("p1","number","Force component parameter 1",default=0.0))
        self.attributes.append(Attribute("p2","number","Force component parameter 2",default=0.0))
        self.attributes.append(Attribute("p3","number","Force component parameter 3",default=0.0))