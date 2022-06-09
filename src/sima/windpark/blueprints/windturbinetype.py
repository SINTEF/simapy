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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("airfoilDatabaseFilename","string","",default=""))
        self.attributes.append(EnumAttribute("direction","sima/windpark/TurbineDirection","Option for choosing the best approach for handling multiple deficits"))
        self.attributes.append(Attribute("outerRadius","number","Outer airfoil radius",default=0.0))
        self.attributes.append(Attribute("numberOfBlades","integer","",default=0))
        self.attributes.append(EnumAttribute("turbineDirection","sima/windpark/TurbineDirection",""))
        self.attributes.append(BlueprintAttribute("bladeElements","sima/windpark/BladeElement","",True,Dimension("*")))
        self.attributes.append(Attribute("cutInWindSpeed","number","",default=0.0))
        self.attributes.append(Attribute("cutOutWindSpeed","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("performanceRelations","sima/windpark/PerformanceRelation","",True,Dimension("*")))