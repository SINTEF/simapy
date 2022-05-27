# 
# Generated with LineCharacteristicItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LineCharacteristicItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LineCharacteristicItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("seaBedX","number","Global x-coordinate of the line end point anchored at the sea bed",default=0.0))
        self.attributes.append(Attribute("seaBedY","number","Global y-coordinate of the line end point anchored at the sea bed",default=0.0))
        self.attributes.append(Attribute("vesselX","number","X-coordinate of the line end point attached to the vessel (given in the body fixed coordinate system)",default=0.0))
        self.attributes.append(Attribute("vesselY","number","Y-coordinate of the line end point attached to the vessel (given in the body fixed coordinate system)",default=0.0))
        self.attributes.append(BlueprintAttribute("lineTensionItems","sima/simo/LineTensionItem","",True,Dimension("*")))