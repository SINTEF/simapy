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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("eye","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("dir","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("up","sima/sima/Vector3","",True))
        self.add_attribute(Attribute("name","string",""))