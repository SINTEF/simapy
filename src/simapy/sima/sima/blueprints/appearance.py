# 
# Generated with AppearanceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class AppearanceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Appearance", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("graphicsfile","string","Graphics file"))
        self.add_attribute(BlueprintAttribute("translation","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("rotation","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("scaling","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
        self.add_attribute(EnumAttribute("geomRepresentationType","sima/sima/GeomRepresentationType","Geometry representation type"))
        self.add_attribute(Attribute("radius","number","",default=1.0))
        self.add_attribute(Attribute("transparency","number","Transparency of geometry. No transparancy=0, Full transparency=1",default=0.0))
        self.add_attribute(EnumAttribute("symmetry","sima/sima/Symmetry","Symmetric properties of the geometry"))