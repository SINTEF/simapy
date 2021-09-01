# 
# Generated with SletringenBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class SletringenBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="Sletringen", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.attributes.append(Attribute("profileExponent","number","Wind profile exponent",default=0.11))
        self.attributes.append(Attribute("averageVelocity","number","Average velocity at reference height",default=0.0))
        self.attributes.append(Attribute("friction","number","Surface drag coefficient.\nAlso used for transverse gust spectrum, if specified in DYNMOD.",default=0.002))
        self.attributes.append(Attribute("gamma","number","Temperature stability parameter",default=10.0))
        self.attributes.append(Attribute("referenceHeight","number","Reference height for wind velocity",default=10.0))