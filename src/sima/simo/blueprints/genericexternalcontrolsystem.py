# 
# Generated with GenericExternalControlSystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class GenericExternalControlSystemBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="GenericExternalControlSystem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("jarFile","string","Path to jar file"))
        self.add_attribute(Attribute("className","string","Class name of controller"))
        self.add_attribute(BlueprintAttribute("measurementEntities","sima/simo/SignalEntity","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("feedbackEntities","sima/simo/SignalEntity","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("intParameters","sima/simo/NamedIntParameter","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("doubleParameters","sima/simo/NamedDoubleParameter","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringParameters","sima/simo/NamedStringParameter","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("libraryPaths","sima/sima/LibraryPaths","",True))