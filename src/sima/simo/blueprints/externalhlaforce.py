# 
# Generated with ExternalHLAForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ExternalHLAForceBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ExternalHLAForce", package_path="sima/simo", description=""):
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
        self.attributes.append(Attribute("importAttackPoint","boolean","",default=False))
        self.attributes.append(Attribute("fx","number","Force in X-direction",default=0.0))
        self.attributes.append(Attribute("fy","number","Force in Y-direction",default=0.0))
        self.attributes.append(Attribute("fz","number","Force in Z-direction",default=0.0))
        self.attributes.append(Attribute("mx","number","Moment about X-axis",default=0.0))
        self.attributes.append(Attribute("my","number","Moment about Y-axis",default=0.0))
        self.attributes.append(Attribute("mz","number","Moment about Z-axis",default=0.0))