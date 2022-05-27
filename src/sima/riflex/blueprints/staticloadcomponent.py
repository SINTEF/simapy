# 
# Generated with StaticLoadComponentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .segmentreference import SegmentReferenceBlueprint

class StaticLoadComponentBlueprint(SegmentReferenceBlueprint):
    """"""

    def __init__(self, name="StaticLoadComponent", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(Attribute("node","integer","Local node number within segment (if global reference system) or element number within segment (if local reference system)",default=0))
        self.attributes.append(Attribute("dof","integer","Degree of freedom within the specified node/element (1-6 for nodes, 1-6 for end 1 of an element and 7-12 for end 2 of an element)",default=0))
        self.attributes.append(Attribute("magnitude","number","Magnitude of load component",default=0.0))
        self.attributes.append(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Reference system for application of nodal load components. If GLOBAL the force is applied at the specified node; if LOCAL the force is applied to the specified element."))
        self.attributes.append(Attribute("specForceIncrement","number","Force increment on magnitude",default=0.0))