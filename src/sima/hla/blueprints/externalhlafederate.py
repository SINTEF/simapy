# 
# Generated with ExternalHLAFederateBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlafederate import HLAFederateBlueprint

class ExternalHLAFederateBlueprint(HLAFederateBlueprint):
    """"""

    def __init__(self, name="ExternalHLAFederate", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("timeStep","number","",default=0.0))
        self.attributes.append(Attribute("launch","boolean","Launch federate from provided class",default=True))
        self.attributes.append(Attribute("jarFile","string","Path to jar file",default=""))
        self.attributes.append(Attribute("className","string","Class name starting HLAFederate",default=""))
        self.attributes.append(Attribute("classPath","string","Additional classpath needed by the external jar",default=""))
        self.attributes.append(Attribute("arguments","string","Arguments passed to the class' main function",default=""))
        self.attributes.append(Attribute("libraryPath","string","Sometimes needed when using native libraries. Corresponds to the -Djava.library.path argument",default=""))
        self.attributes.append(Attribute("showOutput","boolean","Show output from federate",default=False))
        self.attributes.append(BlueprintAttribute("hlaObjects","sima/hla/HLAObject","",True,Dimension("size","")))