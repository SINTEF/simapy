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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("volume","sima/simo/Volume","Add or subtract volume"))
        self.add_attribute(BlueprintAttribute("centerPoint","sima/sima/Point3","Location of center of bottom plane in local coordinates",True))
        self.add_attribute(Attribute("length","number","Length of cone",default=0.0))
        self.add_attribute(Attribute("diameterBottomPlane","number","Diameter of plane 1 (bottom plane)",default=0.0))
        self.add_attribute(Attribute("diameterTopPlane","number","Diameter of plane 2",default=0.0))
        self.add_attribute(EnumAttribute("axis","sima/simo/Axis","Cone axis direction:\nX: parallell to Tank x-axis\nY: parallell to Tank y-axis\nZ: parallell to Tank z-axis"))