# 
# Generated with BodyResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BodyResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BodyResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("body","string","Result body"))
        self.add_attribute(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.add_attribute(BlueprintAttribute("staticPosition","sima/sima/Position","",True))
        self.add_attribute(BlueprintAttribute("bodyForces","sima/simo/ForceResult","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("positioningElementResults","sima/simo/PositioningElementResult","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("couplingResults","sima/simo/CouplingElementResult","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("specifiedForces","sima/simo/ForceResult","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("thrusterForces","sima/simo/ForceResult","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("externalForces","sima/simo/ForceResult","",True,Dimension("*")))