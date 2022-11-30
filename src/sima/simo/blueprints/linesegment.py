# 
# Generated with LineSegmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LineSegmentBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LineSegment", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("length","number","Length of the segment",default=0.0))
        self.add_attribute(BlueprintAttribute("buoy","sima/simo/BuoyType","",False))
        self.add_attribute(EnumAttribute("segmentType","sima/simo/SegmentType","Segment type"))
        self.add_attribute(Attribute("numElements","integer","Number of elements. Used for calculation of fibre rope characteristics and for visualization",default=0))
        self.add_attribute(Attribute("bottomFriction","number","Friction coefficient between line and sea bottom",default=0.0))
        self.add_attribute(Attribute("diameter","number","Segment diameter",default=0.0))
        self.add_attribute(Attribute("eMod","number","Modulus of elasticity",default=0.0))
        self.add_attribute(Attribute("emFac","number","Factor of elasticity - 2 for chains - 1 for other segment types",default=1.0))
        self.add_attribute(Attribute("transverseDrag","number","Transverse drag coefficient",default=0.0))
        self.add_attribute(Attribute("longitudinalDrag","number","Longitudinal drag coefficient",default=0.0))
        self.add_attribute(Attribute("uwia","number","Unit weight in air",default=0.0))
        self.add_attribute(Attribute("watfac","number","The ratio of weight in water to weight in air",default=0.0))
        self.add_attribute(BlueprintAttribute("elongationCharacteristic","sima/simo/ElongationCharacteristic","Non-linear Elongation characteristic",False))