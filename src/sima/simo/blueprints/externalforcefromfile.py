# 
# Generated with ExternalForceFromFileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ExternalForceFromFileBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ExternalForceFromFile", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("forceFile","string","' File heading,  arbitrary number of lines with \n' apostrophe in the first position of the input line\nNCOL: Number of columns (=6)\nNROW: Number of rows (i.e. no. of time incidents)\nSAMP: Sampling interval [T]\nForce components, NROW lines (one per time incident)\nFX   FY   FZ   MX   MY   MZ\nFX   FY   FZ   MX   MY   MZ\nFX   FY   FZ   MX   MY   MZ\nFX   FY   FZ   MX   MY   MZ\n",default=""))
        self.attributes.append(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Which coordinate system is the force is given in?"))
        self.attributes.append(BlueprintAttribute("attachmentPoint","sima/sima/Point3","Attack point of force.",True))
        self.attributes.append(Attribute("fx","number","Force in X-direction",default=0.0))
        self.attributes.append(Attribute("fy","number","Force in Y-direction",default=0.0))
        self.attributes.append(Attribute("fz","number","Force in Z-direction",default=0.0))
        self.attributes.append(Attribute("mx","number","Moment about X-axis",default=0.0))
        self.attributes.append(Attribute("my","number","Moment about Y-axis",default=0.0))
        self.attributes.append(Attribute("mz","number","Moment about Z-axis",default=0.0))