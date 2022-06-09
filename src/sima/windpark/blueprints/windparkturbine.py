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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("_type","sima/windpark/WindTurbineType","",False))
        self.attributes.append(Attribute("x","number","Global x-coordinate of the hub",default=0.0))
        self.attributes.append(Attribute("y","number","Global y-coordinate of the hub",default=0.0))
        self.attributes.append(Attribute("z","number","Global z-coordinate of the hub",default=0.0))
        self.attributes.append(Attribute("shaftAngle","number","",default=0.0))
        self.attributes.append(Attribute("target","boolean","",default=False))