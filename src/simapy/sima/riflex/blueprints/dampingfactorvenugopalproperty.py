# 
# Generated with DampingFactorVenugopalPropertyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .dampingfactorproperty import DampingFactorPropertyBlueprint

class DampingFactorVenugopalPropertyBlueprint(DampingFactorPropertyBlueprint):
    """"""

    def __init__(self, name="DampingFactorVenugopalProperty", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("stillWaterDampingContribution","number","Factor Venugopal still water damping contribution",default=1.0))
        self.add_attribute(Attribute("lowVelocityRegion","number","Factor Venugopal low velocity region",default=1.0))
        self.add_attribute(Attribute("highVelocityRegion","number","Factor Venugopal high velocity region",default=1.0))