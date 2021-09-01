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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("jarFile","string","Path to jar file",default=""))
        self.attributes.append(Attribute("className","string","Class name of controller",default=""))
        self.attributes.append(BlueprintAttribute("measurementEntities","sima/simo/SignalEntity","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("feedbackEntities","sima/simo/SignalEntity","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("intParameters","sima/simo/NamedIntParameter","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("doubleParameters","sima/simo/NamedDoubleParameter","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("stringParameters","sima/simo/NamedStringParameter","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("libraryPaths","sima/sima/LibraryPaths","",True))