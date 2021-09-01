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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Reference to line to be checked for contact with the contact surface.",False))
        self.attributes.append(Attribute("firstSegmentContact","integer","First segment to be checked for contact",default=1))
        self.attributes.append(Attribute("firstElementContact","integer","First element within first contact segment to be chekced for contact",default=1))
        self.attributes.append(Attribute("lastSegmentContact","integer","Last segment to be checked for contact",default=0))
        self.attributes.append(Attribute("lastElementContact","integer","Last element within last contact segment to be checked for contact",default=0))