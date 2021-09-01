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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("graphicsfile","string","Graphics file",default=""))
        self.attributes.append(BlueprintAttribute("translation","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("rotation","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("scaling","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
        self.attributes.append(EnumAttribute("geomRepresentationType","sima/sima/GeomRepresentationType","Geometry representation type"))
        self.attributes.append(Attribute("radius","number","",default=1.0))
        self.attributes.append(Attribute("transparency","number","Transparency of geometry. No transparancy=0, Full transparency=1",default=0.0))
        self.attributes.append(EnumAttribute("symmetry","sima/sima/Symmetry","Symmetric properties of the geometry"))