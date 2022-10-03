# 
# Generated with ConditionNodeResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.signalstorage import SignalStorageBlueprint

class ConditionNodeResultBlueprint(SignalStorageBlueprint):
    """"""

    def __init__(self, name="ConditionNodeResult", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))
        self.attributes.append(Attribute("filenames","string","",Dimension("*"),default=""))