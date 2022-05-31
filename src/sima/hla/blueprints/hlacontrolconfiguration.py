# 
# Generated with HLAControlConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLAControlConfigurationBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLAControlConfiguration", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("bodyName","string","HLA name of body",default=""))
        self.attributes.append(Attribute("vMaxRot","number","Maximum rotation speed",default=1.0))
        self.attributes.append(Attribute("vMaxX","number","Maximum speed in x",default=2.0))
        self.attributes.append(Attribute("vMaxY","number","Maximum speed in y",default=1.0))
        self.attributes.append(Attribute("aMaxRot","number","Maximum rotation acceleration",default=0.1))
        self.attributes.append(Attribute("aMaxX","number","Maximum acceleration in x",default=0.2))
        self.attributes.append(Attribute("aMaxY","number","maximum acceleration in y",default=0.05))
        self.attributes.append(Attribute("limRot","number","The rotation accuracy",default=1.0))
        self.attributes.append(Attribute("limXY","number","The movement accuracy",default=0.5))
        self.attributes.append(EnumAttribute("controlReference","sima/hla/HLAControlReference","Control reference"))