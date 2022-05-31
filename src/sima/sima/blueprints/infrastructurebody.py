# 
# Generated with InfrastructureBodyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .body import BodyBlueprint

class InfrastructureBodyBlueprint(BodyBlueprint):
    """"""

    def __init__(self, name="InfrastructureBody", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("length","number","Length",default=10.0))
        self.attributes.append(Attribute("width","number","Width",default=5.0))
        self.attributes.append(Attribute("height","number","Height",default=5.0))
        self.attributes.append(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
        self.attributes.append(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.attributes.append(BlueprintAttribute("viewpoints","sima/sima/BodyViewpoint","",True,Dimension("*")))
        self.attributes.append(Attribute("utmX","number","UTM x coordinates",default=0.0))
        self.attributes.append(Attribute("utmY","number","UTM y coordinates",default=0.0))