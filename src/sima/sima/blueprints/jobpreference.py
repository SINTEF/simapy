# 
# Generated with JobPreferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simapreference import SIMAPreferenceBlueprint

class JobPreferenceBlueprint(SIMAPreferenceBlueprint):
    """"""

    def __init__(self, name="JobPreference", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("computeConditionsAutomatically","boolean","Compute concurrent condition runs automatically",default=True))
        self.add_attribute(Attribute("maxConditionRuns","integer","Maximum number of concurrent condition runs",default=0))
        self.add_attribute(Attribute("computeWorkflowsAutomatically","boolean","Compute concurrent condition runs automatically",default=True))
        self.add_attribute(Attribute("maxWorkflowRuns","integer","Maximum number of concurrent workflow runs",default=0))