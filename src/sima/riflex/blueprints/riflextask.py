# 
# Generated with RIFLEXTaskBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.simo.blueprints.simotask import SIMOTaskBlueprint

class RIFLEXTaskBlueprint(SIMOTaskBlueprint):
    """"""

    def __init__(self, name="RIFLEXTask", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.attributes.append(Attribute("runNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("variations","sima/condition/ModelVariation","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("referenceVariables","sima/condition/ModelReferenceVariable","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("initialCondition","sima/condition/InitialCondition","",True))
        self.attributes.append(BlueprintAttribute("conditions","sima/condition/ConditionTaskCondition","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("model","sima/riflex/RIFLEXModel","",True))
        self.attributes.append(Attribute("simoMemory","integer","Enables override of the default memory settings for SIMO. Given in MB",default=128))
        self.attributes.append(Attribute("removeIntermediateFiles","boolean","",default=True))
        self.attributes.append(EnumAttribute("exportMassUnit","sima/simo/MassUnit","Used as export unit for mass ( and indirectly force)"))
        self.attributes.append(Attribute("exportAsFMU","boolean","Generate FMU (Functional Mockup Unit) from model",default=False))
        self.attributes.append(Attribute("riflexStamodMemory","integer","Enables override of the default memory settings. Given in MB",default=512))
        self.attributes.append(Attribute("numRiflexStamodArrays","integer","Enables override of the default memory settings",default=20000))
        self.attributes.append(Attribute("riflexDynmodMemory","integer","Enables override of the default memory settings. Given in MB. Also used for VIVANA and Eigenvalue analysis",default=512))
        self.attributes.append(Attribute("vivanaWorkArraySize","integer","Enables override of the default memory settings",default=9000000))
        self.attributes.append(Attribute("maxRiflexArrays","integer","Enables override of the default memory settings",default=2000))
        self.attributes.append(Attribute("riflexOutmodMemory","integer","Enables override of the default memory settings. Given in MB",default=32))
        self.attributes.append(Attribute("skipRiflexDynmodTransformation","boolean","",default=True))