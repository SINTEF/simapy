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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attachmentPoint","sima/sima/Point3","Attack point of force.",True))
        self.add_attribute(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Which coordinate system is the force is given in?"))
        self.add_attribute(Attribute("nStorageParameters","integer","Number of parameters for intermediate storage",default=0))
        self.add_attribute(BlueprintAttribute("intParameters","sima/simo/StringIntItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("doubleParameters","sima/simo/StringDoubleItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringParameters","sima/simo/StringItem","",True,Dimension("*")))
        self.add_attribute(Attribute("importAttackPoint","boolean","",default=False))
        self.add_attribute(Attribute("fx","number","Force in X-direction",default=0.0))
        self.add_attribute(Attribute("fy","number","Force in Y-direction",default=0.0))
        self.add_attribute(Attribute("fz","number","Force in Z-direction",default=0.0))
        self.add_attribute(Attribute("mx","number","Moment about X-axis",default=0.0))
        self.add_attribute(Attribute("my","number","Moment about Y-axis",default=0.0))
        self.add_attribute(Attribute("mz","number","Moment about Z-axis",default=0.0))