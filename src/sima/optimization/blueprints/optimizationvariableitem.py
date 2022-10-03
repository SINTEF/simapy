# 
# Generated with OptimizationVariableItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class OptimizationVariableItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="OptimizationVariableItem", package_path="sima/optimization", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("start","number","Starting value for the optimization variable",default=0.0))
        self.attributes.append(Attribute("min","number","Lower bound for the optimization variable",default=0.0))
        self.attributes.append(Attribute("max","number","Upper bound for the optimization variable",default=0.0))
        self.attributes.append(Attribute("delta","number","Delta for the optimization variable to be used in calculation of gradients",default=0.0))
        self.attributes.append(BlueprintAttribute("variable","sima/workflow/RealNumberInput","Optimization variable",False))