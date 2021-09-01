# 
# Generated with InitialConditionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.condition import ConditionBlueprint
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class InitialConditionBlueprint(ConditionBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="InitialCondition", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))