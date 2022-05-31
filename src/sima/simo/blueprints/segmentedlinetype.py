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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("segments","sima/simo/LineSegment","",True,Dimension("*")))
        self.attributes.append(Attribute("vmin","number","Min. relative z-pos. for which the line characteristics will be calculated.",default=0.0))
        self.attributes.append(Attribute("vmax","number","Max. relative z-pos. for which the line characteristics will be calculated.",default=0.0))
        self.attributes.append(EnumAttribute("bottomContactOption","sima/simo/BottomContactOption","Bottom contact option"))
        self.attributes.append(Attribute("anchorZ","number","Z-coordinate of the anchor in global coordinate system",default=0.0))
        self.attributes.append(Attribute("maxTension","number","Maximum tension to be used in the line characteristics\ncalculations",default=0.0))
        self.attributes.append(Attribute("minHTension","number","Minimum horizontal tension to be used for calculation\nof line characteristics",default=0.0))
        self.attributes.append(EnumAttribute("method","sima/simo/LineCharacteristicMethod","Method for initialization of line"))
        self.attributes.append(Attribute("npth","integer","Number of points in the line characteristics matrix, offset variation in the horizontal plane.",default=40))
        self.attributes.append(Attribute("nptv","integer","Number of points in the line characteristics matrix, offset variation in the vertical plane.",default=5))
        self.attributes.append(Attribute("slope","number","The angle of the seabed under the catenary line. Slope = 0 means a flat seabed. Positive slope means that the seabed is sloping downwards from the anchor towards the attachment point.",default=0.0))