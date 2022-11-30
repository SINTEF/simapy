# 
# Generated with SuperNodeReferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .bodyforcecomponent import BodyForceComponentBlueprint

class SuperNodeReferenceBlueprint(BodyForceComponentBlueprint):
    """"""

    def __init__(self, name="SuperNodeReference", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))