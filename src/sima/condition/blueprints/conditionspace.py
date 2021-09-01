# 
# Generated with ConditionSpaceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .conditiontaskcondition import ConditionTaskConditionBlueprint
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ConditionSpaceBlueprint(ConditionTaskConditionBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="ConditionSpace", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))
        self.attributes.append(BlueprintAttribute("selection","sima/sima/ConditionSelectable","",False))
        self.attributes.append(BlueprintAttribute("variableItems","sima/sima/VariableItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("variableItemSets","sima/condition/VariableItemSet","",True,Dimension("size","")))
        self.attributes.append(Attribute("inputFromFile","boolean","Specify variable values from file.",default=False))
        self.attributes.append(Attribute("path","string","Import variable values from file. Expected file format:\n' any comment specified with '\n'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  \n1.0      2.0    3\n4.0      5.0    4\n'any comment\n           ",default=""))