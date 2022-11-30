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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.add_attribute(Attribute("runNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("variations","sima/condition/ModelVariation","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("referenceVariables","sima/sima/ModelReferenceVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("initialCondition","sima/condition/InitialCondition","",True))
        self.add_attribute(BlueprintAttribute("conditions","sima/condition/ConditionTaskCondition","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("model","sima/riflex/RIFLEXModel","",True))
        self.add_attribute(Attribute("simoMemory","integer","Enables override of the default memory settings for SIMO. Given in MB",default=128))
        self.add_attribute(Attribute("removeIntermediateFiles","boolean","",default=True))
        self.add_attribute(EnumAttribute("exportMassUnit","sima/simo/MassUnit","Used as export unit for mass ( and indirectly force)"))
        self.add_attribute(Attribute("exportAsFMU","boolean","Generate FMU (Functional Mockup Unit) from model",default=False))
        self.add_attribute(Attribute("riflexStamodMemory","integer","Enables override of the default memory settings. Given in MB",default=512))
        self.add_attribute(Attribute("numRiflexStamodArrays","integer","Enables override of the default memory settings",default=20000))
        self.add_attribute(Attribute("riflexDynmodMemory","integer","Enables override of the default memory settings. Given in MB. Also used for VIVANA and Eigenvalue analysis",default=512))
        self.add_attribute(Attribute("vivanaWorkArraySize","integer","Enables override of the default memory settings",default=9000000))
        self.add_attribute(Attribute("maxRiflexArrays","integer","Enables override of the default memory settings",default=2000))
        self.add_attribute(Attribute("riflexOutmodMemory","integer","Enables override of the default memory settings. Given in MB",default=32))
        self.add_attribute(Attribute("skipRiflexDynmodTransformation","boolean","",default=True))