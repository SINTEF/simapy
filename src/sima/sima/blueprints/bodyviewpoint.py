# 
# Generated with BodyViewpointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .viewpoint import ViewpointBlueprint
from .namedobject import NamedObjectBlueprint

class BodyViewpointBlueprint(ViewpointBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="BodyViewpoint", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("eye","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("dir","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("up","sima/sima/Vector3","",True))