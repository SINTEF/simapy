# 
# Generated with ExternalDLLForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ExternalDLLForceBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ExternalDLLForce", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attachmentPoint","sima/sima/Point3","Attack point of force.",True))
        self.add_attribute(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Which coordinate system is the force is given in?"))
        self.add_attribute(Attribute("nStorageParameters","integer","Number of parameters for intermediate storage",default=0))
        self.add_attribute(BlueprintAttribute("intParameters","sima/simo/StringIntItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("doubleParameters","sima/simo/StringDoubleItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringParameters","sima/simo/StringItem","",True,Dimension("*")))
        self.add_attribute(Attribute("nCurrentPoints","integer","Number of points where current velocities shall be given.",default=1))
        self.add_attribute(Attribute("dllFile","string",""))
        self.add_attribute(BlueprintAttribute("libraryPaths","sima/sima/LibraryPaths","",True))