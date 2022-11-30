# 
# Generated with WindTurbineTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class WindTurbineTypeBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="WindTurbineType", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("airfoilDatabaseFilename","string",""))
        self.add_attribute(EnumAttribute("direction","sima/windpark/TurbineDirection","Option for choosing the best approach for handling multiple deficits"))
        self.add_attribute(Attribute("outerRadius","number","Outer airfoil radius",default=0.0))
        self.add_attribute(Attribute("numberOfBlades","integer","",default=0))
        self.add_attribute(EnumAttribute("turbineDirection","sima/windpark/TurbineDirection",""))
        self.add_attribute(BlueprintAttribute("bladeElements","sima/windpark/BladeElement","",True,Dimension("*")))
        self.add_attribute(Attribute("cutInWindSpeed","number","",default=0.0))
        self.add_attribute(Attribute("cutOutWindSpeed","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("performanceRelations","sima/windpark/PerformanceRelation","",True,Dimension("*")))