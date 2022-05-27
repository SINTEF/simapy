# 
# Generated with CRSAxialFrictionModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CRSAxialFrictionModelBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CRSAxialFrictionModel", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("staticFriction","number","Static friction force corresponding to elongation",default=0.0))
        self.attributes.append(Attribute("staticElongation","number","Relative elongation",default=0.0))
        self.attributes.append(Attribute("dynamicFriction","number","Dynamic friction force corresponding to elongation",default=0.0))
        self.attributes.append(Attribute("dynamicElongation","number","Relative elongation",default=0.0))
        self.attributes.append(Attribute("axialFriction","boolean","Local axial friction model",default=False))