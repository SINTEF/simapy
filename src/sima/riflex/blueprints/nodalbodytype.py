# 
# Generated with NodalBodyTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .nodalcomponenttype import NodalComponentTypeBlueprint

class NodalBodyTypeBlueprint(NodalComponentTypeBlueprint):
    """"""

    def __init__(self, name="NodalBodyType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("mass","number","Mass",default=0.0))
        self.add_attribute(Attribute("volume","number","Displacement volume",default=0.0))
        self.add_attribute(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Reference frame"))
        self.add_attribute(Attribute("dragX","number","Drag force coefficient in X-direction",default=0.0))
        self.add_attribute(Attribute("dragY","number","Drag force coefficient in Y-direction",default=0.0))
        self.add_attribute(Attribute("dragZ","number","Drag force coefficient in Z-direction",default=0.0))
        self.add_attribute(Attribute("addedMassX","number","Added mass in X-direction",default=0.0))
        self.add_attribute(Attribute("addedMassY","number","Added mass in Y-direction",default=0.0))
        self.add_attribute(Attribute("addedMassZ","number","Added mass in Z-direction",default=0.0))