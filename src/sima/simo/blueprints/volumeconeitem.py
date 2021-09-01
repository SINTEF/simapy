# 
# Generated with VolumeConeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .volumemassportion import VolumeMassPortionBlueprint

class VolumeConeItemBlueprint(VolumeMassPortionBlueprint):
    """"""

    def __init__(self, name="VolumeConeItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("volume","sima/simo/Volume","Add or subtract volume"))
        self.attributes.append(BlueprintAttribute("centerPoint","sima/sima/Point3","Location of center of bottom plane in local coordinates",True))
        self.attributes.append(Attribute("length","number","Length of cone",default=0.0))
        self.attributes.append(Attribute("diameterBottomPlane","number","Diameter of plane 1 (bottom plane)",default=0.0))
        self.attributes.append(Attribute("diameterTopPlane","number","Diameter of plane 2",default=0.0))
        self.attributes.append(EnumAttribute("axis","sima/simo/Axis","Cone axis direction:\nX: parallell to Tank x-axis\nY: parallell to Tank y-axis\nZ: parallell to Tank z-axis"))