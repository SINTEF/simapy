# 
# Generated with ScatterDataCalculationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class ScatterDataCalculationBlueprint(NamedObjectBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="ScatterDataCalculation", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("currentModel","sima/metocean/CurrentModel",""))
        self.add_attribute(Attribute("kfactor","number","",default=1.0))
        self.add_attribute(Attribute("directionRelativeToWind","number","Direction relative to wind. Zero angle means collinear wind and current",default=0.0))
        self.add_attribute(Attribute("windReferenceLevel","number","The Level in wind data at which wind speed and direction will be used to define the current",default=0.0))
        self.add_attribute(BlueprintAttribute("windCurrentProfile","sima/metocean/Profile","",False))
        self.add_attribute(Attribute("baseCurrentSpeed","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("baseCurrentProfile","sima/metocean/Profile","",False))
        self.add_attribute(BlueprintAttribute("currentLevels","sima/metocean/CalculationLevel","",True,Dimension("*")))
        self.add_attribute(Attribute("relativeCompassAngle","number","Relative angle between analysis x-axis and north direction in anti-clockwise direction.\nShould match the angle given in the recieving SIMA task location.",default=0.0))
        self.add_attribute(EnumAttribute("inputReferenceSystem","sima/metocean/InputReferenceSystem","Defines the input reference system of the data.\nIf the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated"))
        self.add_attribute(BlueprintAttribute("scatterData","sima/metocean/ScatterData","",False))
        self.add_attribute(BlueprintAttribute("directions","sima/metocean/CalculationDirection","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("windLevels","sima/metocean/CalculationLevel","",True,Dimension("*")))