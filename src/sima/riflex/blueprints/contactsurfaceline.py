# 
# Generated with ContactSurfaceLineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ContactSurfaceLineBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ContactSurfaceLine", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Reference to line to be checked for contact with the contact surface.",False))
        self.add_attribute(Attribute("firstSegmentContact","integer","First segment to be checked for contact",default=1))
        self.add_attribute(Attribute("firstElementContact","integer","First element within first contact segment to be chekced for contact",default=1))
        self.add_attribute(Attribute("lastSegmentContact","integer","Last segment to be checked for contact",default=0))
        self.add_attribute(Attribute("lastElementContact","integer","Last element within last contact segment to be checked for contact",default=0))