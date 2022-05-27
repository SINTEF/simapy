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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("attachmentPoint","sima/sima/Point3","Attack point of force.",True))
        self.attributes.append(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Which coordinate system is the force is given in?"))
        self.attributes.append(Attribute("nStorageParameters","integer","Number of parameters for intermediate storage",default=0))
        self.attributes.append(BlueprintAttribute("intParameters","sima/simo/StringIntItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("doubleParameters","sima/simo/StringDoubleItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("stringParameters","sima/simo/StringItem","",True,Dimension("*")))
        self.attributes.append(Attribute("nCurrentPoints","integer","Number of points where current velocities shall be given.",default=1))
        self.attributes.append(Attribute("dllFile","string","",default=""))
        self.attributes.append(BlueprintAttribute("libraryPaths","sima/sima/LibraryPaths","",True))