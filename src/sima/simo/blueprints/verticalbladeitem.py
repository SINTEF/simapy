# 
# Generated with VerticalBladeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class VerticalBladeItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="VerticalBladeItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("airfoil","sima/windturbine/Airfoil","",False))
        self.add_attribute(Attribute("radius","number","Radius of the second node of the element",default=0.0))
        self.add_attribute(Attribute("elevation","number","Elevation of the second node of the element",default=0.0))
        self.add_attribute(Attribute("offset","number","Offset of the second node of the element from the R-Z plane",default=0.0))
        self.add_attribute(Attribute("chordLength","number","Chord length of the foil profile",default=0.0))
        self.add_attribute(Attribute("twist","number","Static twist angle",default=0.0))