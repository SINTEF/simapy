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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("timeStep","number","",default=0.0))
        self.add_attribute(Attribute("launch","boolean","Launch federate from provided class",default=True))
        self.add_attribute(Attribute("jarFile","string","Path to jar file"))
        self.add_attribute(Attribute("className","string","Class name starting HLAFederate"))
        self.add_attribute(Attribute("classPath","string","Additional classpath needed by the external jar"))
        self.add_attribute(Attribute("arguments","string","Arguments passed to the class' main function"))
        self.add_attribute(Attribute("libraryPath","string","Sometimes needed when using native libraries. Corresponds to the -Djava.library.path argument"))
        self.add_attribute(Attribute("showOutput","boolean","Show output from federate",default=False))
        self.add_attribute(BlueprintAttribute("hlaObjects","sima/hla/HLAObject","",True,Dimension("*")))