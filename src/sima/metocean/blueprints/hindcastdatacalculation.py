# 
# Generated with HindcastDataCalculationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class HindcastDataCalculationBlueprint(NamedObjectBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="HindcastDataCalculation", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("currentModel","sima/metocean/CurrentModel",""))
        self.attributes.append(Attribute("kfactor","number","",default=1.0))
        self.attributes.append(Attribute("directionRelativeToWind","number","Direction relative to wind. Zero angle means collinear wind and current",default=0.0))
        self.attributes.append(Attribute("windReferenceLevel","number","The Level in wind data at which wind speed and direction will be used to define the current",default=0.0))
        self.attributes.append(BlueprintAttribute("windCurrentProfile","sima/metocean/Profile","",False))
        self.attributes.append(Attribute("baseCurrentSpeed","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("baseCurrentProfile","sima/metocean/Profile","",False))
        self.attributes.append(BlueprintAttribute("currentLevels","sima/metocean/CalculationLevel","",True,Dimension("*")))
        self.attributes.append(Attribute("relativeCompassAngle","number","Relative angle between analysis x-axis and north direction in anti-clockwise direction.\nShould match the angle given in the recieving SIMA task location.",default=0.0))
        self.attributes.append(EnumAttribute("inputReferenceSystem","sima/metocean/InputReferenceSystem","Defines the input reference system of the data.\nIf the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated"))
        self.attributes.append(BlueprintAttribute("hindcastData","sima/metocean/HindcastData","",False))
        self.attributes.append(Attribute("from","string","",default=""))
        self.attributes.append(Attribute("to","string","",default=""))
        self.attributes.append(BlueprintAttribute("windLevels","sima/metocean/CalculationLevel","",True,Dimension("*")))