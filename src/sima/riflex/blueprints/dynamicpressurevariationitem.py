# 
# Generated with DynamicPressureVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .pressurevariationitem import PressureVariationItemBlueprint

class DynamicPressureVariationItemBlueprint(PressureVariationItemBlueprint):
    """"""

    def __init__(self, name="DynamicPressureVariationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("mainRiserLine","sima/riflex/MainRiserLine","Main riser line",False))
        self.add_attribute(Attribute("inletPressure","number","Final pressure at inlet end",default=0.0))
        self.add_attribute(Attribute("pressureDrop","number","Final pressure drop",default=0.0))
        self.add_attribute(Attribute("fluidVelocity","number","Final fluid velocity",default=0.0))
        self.add_attribute(Attribute("startTime","number","Start time for pressure variation",default=0.0))
        self.add_attribute(Attribute("endTime","number","End time for pressure variation",default=0.0))