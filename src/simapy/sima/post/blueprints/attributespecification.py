# 
# Generated with AttributeSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .pathspecification import PathSpecificationBlueprint
from .signalproperties import SignalPropertiesBlueprint

class AttributeSpecificationBlueprint(PathSpecificationBlueprint,SignalPropertiesBlueprint):
    """"""

    def __init__(self, name="AttributeSpecification", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("attribute","string",""))
        self.add_attribute(Attribute("value","string",""))