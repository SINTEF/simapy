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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("seaBedX","number","Global x-coordinate of the line end point anchored at the sea bed",default=0.0))
        self.add_attribute(Attribute("seaBedY","number","Global y-coordinate of the line end point anchored at the sea bed",default=0.0))
        self.add_attribute(Attribute("vesselX","number","X-coordinate of the line end point attached to the vessel (given in the body fixed coordinate system)",default=0.0))
        self.add_attribute(Attribute("vesselY","number","Y-coordinate of the line end point attached to the vessel (given in the body fixed coordinate system)",default=0.0))
        self.add_attribute(BlueprintAttribute("lineTensionItems","sima/simo/LineTensionItem","",True,Dimension("*")))