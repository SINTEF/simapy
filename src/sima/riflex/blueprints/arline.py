# 
# Generated with ARLineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.simo.blueprints.lineforceprovider import LineForceProviderBlueprint

class ARLineBlueprint(LineForceProviderBlueprint):
    """"""

    def __init__(self, name="ARLine", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("lineType","sima/riflex/ARLineType","Line type.",False))
        self.attributes.append(BlueprintAttribute("end1","sima/riflex/SuperNode","Supernode at end 1.",False))
        self.attributes.append(BlueprintAttribute("end2","sima/riflex/SuperNode","Supernode at end 2.",False))
        self.attributes.append(Attribute("disabled","boolean","Do not include this line in the calculations",default=False))