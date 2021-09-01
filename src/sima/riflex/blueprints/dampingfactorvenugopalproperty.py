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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("stillWaterDampingContribution","number","Factor Venugopal still water damping contribution",default=1.0))
        self.attributes.append(Attribute("lowVelocityRegion","number","Factor Venugopal low velocity region",default=1.0))
        self.attributes.append(Attribute("highVelocityRegion","number","Factor Venugopal high velocity region",default=1.0))