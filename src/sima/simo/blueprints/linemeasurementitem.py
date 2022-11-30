# 
# Generated with LineMeasurementItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LineMeasurementItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LineMeasurementItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/simo/LineForceProvider","",False))
        self.add_attribute(EnumAttribute("lineEnd","sima/simo/LineEnd","Line end to read measurements from"))