# 
# Generated with WamitEnvironmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class WamitEnvironmentBlueprint(NamedObjectBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="WamitEnvironment", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("wave","sima/wamit/WamitWave","",True))