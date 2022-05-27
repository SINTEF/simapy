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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.attributes.append(Attribute("resource","string","",default=""))
        self.attributes.append(Attribute("relative","boolean","",default=False))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("results","sima/sima/Result","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("entries","sima/sima/ResultEntry","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("lisFile","sima/simo/LisFile","",True))
        self.attributes.append(BlueprintAttribute("simoLDAT","sima/sima/Result","",True))
        self.attributes.append(BlueprintAttribute("timeSimulationResult","sima/simo/TimeSimulationResult","",True))
        self.attributes.append(BlueprintAttribute("riflexLDAT","sima/sima/Result","",True))
        self.attributes.append(BlueprintAttribute("resFile","sima/riflex/ResFile","",True))
        self.attributes.append(BlueprintAttribute("combinedLoadingResuls","sima/sima/Result","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("outmodResuls","sima/sima/Result","",True,Dimension("*")))