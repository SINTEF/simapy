# 
# Generated with WindParkTurbineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class WindParkTurbineBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="WindParkTurbine", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("_type","sima/windpark/WindTurbineType","",False))
        self.add_attribute(Attribute("x","number","Global x-coordinate of the hub",default=0.0))
        self.add_attribute(Attribute("y","number","Global y-coordinate of the hub",default=0.0))
        self.add_attribute(Attribute("z","number","Global z-coordinate of the hub",default=0.0))
        self.add_attribute(Attribute("shaftAngle","number","",default=0.0))
        self.add_attribute(Attribute("target","boolean","",default=False))