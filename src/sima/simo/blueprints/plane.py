# 
# Generated with PlaneBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PlaneBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Plane", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("unlimited","boolean","Whether the fender plane is limited to a restricted sector",default=False))
        self.add_attribute(Attribute("width","number","Width of plane",default=0.0))
        self.add_attribute(Attribute("length","number","Length of plane",default=0.0))
        self.add_attribute(BlueprintAttribute("point","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("normalVector","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("parallelVector","sima/sima/Vector3","",True))