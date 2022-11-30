# 
# Generated with HLALocationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.location import LocationBlueprint

class HLALocationBlueprint(LocationBlueprint):
    """"""

    def __init__(self, name="HLALocation", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("initialViewpoint","sima/sima/InitialViewpoint","",True))
        self.add_attribute(BlueprintAttribute("initialRotationpoint","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("viewpoints","sima/sima/NamedViewpoint","",True,Dimension("*")))
        self.add_attribute(Attribute("relativeCompassAngle","number","Relative angle between analysis x-axis and north direction in anti-clockwise direction",default=0.0))
        self.add_attribute(Attribute("utmX","number","Offset of local coordinate system origin (X) relative to UTM (Easting).",default=0.0))
        self.add_attribute(Attribute("utmY","number","Offset of local coordinate system origin (Y) relative to UTM (Northing).",default=0.0))
        self.add_attribute(Attribute("gridZone","string","Zone consists of a number from [01-60] and a letter from [C-Z], or just one of [A,B,Y,Z] if on the antarctic or arctic pole."))
        self.add_attribute(BlueprintAttribute("infrastructureBodies","sima/sima/InfrastructureBody","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("seaSurface","sima/hla/HLASeaSurface","",True))
        self.add_attribute(BlueprintAttribute("flatBottom","sima/sima/FlatBottom","",True))
        self.add_attribute(BlueprintAttribute("sim3DBottom","sima/hla/SIM3DBottom","",True))