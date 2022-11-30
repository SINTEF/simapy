# 
# Generated with DynamicTemperatureVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .elementreference import ElementReferenceBlueprint

class DynamicTemperatureVariationItemBlueprint(ElementReferenceBlueprint):
    """"""

    def __init__(self, name="DynamicTemperatureVariationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.add_attribute(Attribute("allElements","boolean","All elements",default=False))
        self.add_attribute(Attribute("startTime","number","Start time for temperature variation",default=0.0))
        self.add_attribute(Attribute("endTime","number","End time for temperature variation",default=0.0))
        self.add_attribute(Attribute("lastTemperature","number","Temperature at end of temperature variation",default=0.0))