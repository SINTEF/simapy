# 
# Generated with MainRiserLineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class MainRiserLineBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="MainRiserLine", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("riserLines","sima/riflex/ARLineItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("flowRho","number","Density of contents",default=0.0))
        self.attributes.append(Attribute("flowPressure","number","Pressure at specified end",default=0.0))
        self.attributes.append(EnumAttribute("flowPressureEnd","sima/riflex/End","End for which flow data is specified."))
        self.attributes.append(Attribute("flowPressureDrop","number","Pressure drop",default=0.0))