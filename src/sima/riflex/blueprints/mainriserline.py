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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("riserLines","sima/riflex/ARLineItem","",True,Dimension("*")))
        self.add_attribute(Attribute("flowRho","number","Density of contents",default=0.0))
        self.add_attribute(Attribute("flowPressure","number","Pressure at specified end",default=0.0))
        self.add_attribute(EnumAttribute("flowPressureEnd","sima/riflex/End","End for which flow data is specified."))
        self.add_attribute(Attribute("flowPressureDrop","number","Pressure drop",default=0.0))