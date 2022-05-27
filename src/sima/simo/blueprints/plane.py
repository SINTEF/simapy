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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("unlimited","boolean","Whether the fender plane is limited to a restricted sector",default=False))
        self.attributes.append(Attribute("width","number","Width of plane",default=0.0))
        self.attributes.append(Attribute("length","number","Length of plane",default=0.0))
        self.attributes.append(BlueprintAttribute("point","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("normalVector","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("parallelVector","sima/sima/Vector3","",True))