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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("bodyName","string","HLA name of body"))
        self.add_attribute(Attribute("vMaxRot","number","Maximum rotation speed",default=1.0))
        self.add_attribute(Attribute("vMaxX","number","Maximum speed in x",default=2.0))
        self.add_attribute(Attribute("vMaxY","number","Maximum speed in y",default=1.0))
        self.add_attribute(Attribute("aMaxRot","number","Maximum rotation acceleration",default=0.1))
        self.add_attribute(Attribute("aMaxX","number","Maximum acceleration in x",default=0.2))
        self.add_attribute(Attribute("aMaxY","number","maximum acceleration in y",default=0.05))
        self.add_attribute(Attribute("limRot","number","The rotation accuracy",default=1.0))
        self.add_attribute(Attribute("limXY","number","The movement accuracy",default=0.5))
        self.add_attribute(EnumAttribute("controlReference","sima/hla/HLAControlReference","Control reference"))