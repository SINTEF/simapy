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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("body","string","Result body",default=""))
        self.attributes.append(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.attributes.append(BlueprintAttribute("staticPosition","sima/sima/Position","",True))
        self.attributes.append(BlueprintAttribute("bodyForces","sima/simo/ForceResult","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("positioningElementResults","sima/simo/PositioningElementResult","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("couplingResults","sima/simo/CouplingElementResult","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("specifiedForces","sima/simo/ForceResult","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("thrusterForces","sima/simo/ForceResult","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("externalForces","sima/simo/ForceResult","",True,Dimension("*")))