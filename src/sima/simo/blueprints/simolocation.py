# 
# Generated with SIMOLocationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .commonlocation import CommonLocationBlueprint

class SIMOLocationBlueprint(CommonLocationBlueprint):
    """"""

    def __init__(self, name="SIMOLocation", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("initialViewpoint","sima/sima/InitialViewpoint","",True))
        self.attributes.append(BlueprintAttribute("initialRotationpoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("viewpoints","sima/sima/NamedViewpoint","",True,Dimension("size","")))
        self.attributes.append(Attribute("relativeCompassAngle","number","Relative angle between analysis x-axis and north direction in anti-clockwise direction",default=0.0))
        self.attributes.append(Attribute("utmX","number","Offset of local coordinate system origin (X) relative to UTM (Easting).",default=0.0))
        self.attributes.append(Attribute("utmY","number","Offset of local coordinate system origin (Y) relative to UTM (Northing).",default=0.0))
        self.attributes.append(Attribute("gridZone","string","Zone consists of a number from [01-60] and a letter from [C-Z], or just one of [A,B,Y,Z] if on the antarctic or arctic pole.",default=""))
        self.attributes.append(BlueprintAttribute("infrastructureBodies","sima/sima/InfrastructureBody","",True,Dimension("size","")))
        self.attributes.append(Attribute("waterDepth","number","Water depth for kinematics",default=1000.0))
        self.attributes.append(BlueprintAttribute("seaSurface","sima/environment/SeaSurface","",True))
        self.attributes.append(BlueprintAttribute("flatBottom","sima/sima/FlatBottom","",True))
        self.attributes.append(BlueprintAttribute("physicalConstants","sima/simo/PhysicalConstants","",True))