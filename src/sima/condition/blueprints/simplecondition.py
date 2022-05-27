# 
# Generated with SimpleConditionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .conditiontaskcondition import ConditionTaskConditionBlueprint
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class SimpleConditionBlueprint(ConditionTaskConditionBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="SimpleCondition", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))
        self.attributes.append(BlueprintAttribute("selection","sima/sima/ConditionSelectable","",False))
        self.attributes.append(BlueprintAttribute("variableItems","sima/sima/VariableItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("probabilityVariable","sima/sima/DoubleVariable","Used to set a probability for single runs",False))
        self.attributes.append(BlueprintAttribute("variation","sima/condition/ModelVariation","",False))