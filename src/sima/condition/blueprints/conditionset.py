# 
# Generated with ConditionSetBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .conditiontaskcondition import ConditionTaskConditionBlueprint
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ConditionSetBlueprint(ConditionTaskConditionBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="ConditionSet", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("changeNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))
        self.add_attribute(BlueprintAttribute("selection","sima/sima/ConditionSelectable","",False))
        self.add_attribute(BlueprintAttribute("variableItems","sima/sima/VariableItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("probabilityVariable","sima/sima/DoubleVariable","Used to set a probability for single runs",False))
        self.add_attribute(BlueprintAttribute("variableItemSets","sima/condition/VariableItemSet","",True,Dimension("*")))
        self.add_attribute(Attribute("inputFromFile","boolean","Specify variable values from file.",default=False))
        self.add_attribute(Attribute("path","string","Import variable values from file. Expected file format:\n' any comment specified with '\n'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  \n1.0      2.0    3\n4.0      5.0    4\n'any comment\n           "))