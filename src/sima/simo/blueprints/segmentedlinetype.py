# 
# Generated with SegmentedLineTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .linetype import LineTypeBlueprint

class SegmentedLineTypeBlueprint(LineTypeBlueprint):
    """"""

    def __init__(self, name="SegmentedLineType", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("segments","sima/simo/LineSegment","",True,Dimension("*")))
        self.add_attribute(Attribute("vmin","number","Min. relative z-pos. for which the line characteristics will be calculated.",default=0.0))
        self.add_attribute(Attribute("vmax","number","Max. relative z-pos. for which the line characteristics will be calculated.",default=0.0))
        self.add_attribute(EnumAttribute("bottomContactOption","sima/simo/BottomContactOption","Bottom contact option"))
        self.add_attribute(Attribute("anchorZ","number","Z-coordinate of the anchor in global coordinate system",default=0.0))
        self.add_attribute(Attribute("maxTension","number","Maximum tension to be used in the line characteristics\ncalculations",default=0.0))
        self.add_attribute(Attribute("minHTension","number","Minimum horizontal tension to be used for calculation\nof line characteristics",default=0.0))
        self.add_attribute(EnumAttribute("method","sima/simo/LineCharacteristicMethod","Method for initialization of line"))
        self.add_attribute(Attribute("npth","integer","Number of points in the line characteristics matrix, offset variation in the horizontal plane.",default=40))
        self.add_attribute(Attribute("nptv","integer","Number of points in the line characteristics matrix, offset variation in the vertical plane.",default=5))
        self.add_attribute(Attribute("slope","number","The angle of the seabed under the catenary line. Slope = 0 means a flat seabed. Positive slope means that the seabed is sloping downwards from the anchor towards the attachment point.",default=0.0))