# 
# Generated with VolumeBoxItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .volumemassportion import VolumeMassPortionBlueprint

class VolumeBoxItemBlueprint(VolumeMassPortionBlueprint):
    """"""

    def __init__(self, name="VolumeBoxItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("volume","sima/simo/Volume","Add or subtract volume"))
        self.add_attribute(BlueprintAttribute("centerPoint","sima/sima/Point3","Location of center of bottom plane in local coordinates",True))
        self.add_attribute(Attribute("lengthX","number","Length of box i x-direction",default=0.0))
        self.add_attribute(Attribute("lengthY","number","Length of box i y-direction",default=0.0))
        self.add_attribute(Attribute("lengthZ","number","Length of box i z-direction",default=0.0))