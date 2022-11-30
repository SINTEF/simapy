# 
# Generated with RIFLEXDynamicResultEntryBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.simo.blueprints.simodynamicresultentry import SIMODynamicResultEntryBlueprint

class RIFLEXDynamicResultEntryBlueprint(SIMODynamicResultEntryBlueprint):
    """"""

    def __init__(self, name="RIFLEXDynamicResultEntry", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(Attribute("resource","string",""))
        self.add_attribute(Attribute("relative","boolean","",default=False))
        self.add_attribute(Attribute("changeNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("results","sima/sima/Result","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("entries","sima/sima/ResultEntry","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("lisFile","sima/simo/LisFile","",True))
        self.add_attribute(BlueprintAttribute("simoLDAT","sima/sima/Result","",True))
        self.add_attribute(BlueprintAttribute("timeSimulationResult","sima/simo/TimeSimulationResult","",True))
        self.add_attribute(BlueprintAttribute("riflexLDAT","sima/sima/Result","",True))
        self.add_attribute(BlueprintAttribute("resFile","sima/riflex/ResFile","",True))
        self.add_attribute(BlueprintAttribute("combinedLoadingResuls","sima/sima/Result","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("outmodResuls","sima/sima/Result","",True,Dimension("*")))