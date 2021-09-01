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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("airfoil","sima/windturbine/Airfoil","",False))
        self.attributes.append(Attribute("radius","number","Radius of the second node of the element",default=0.0))
        self.attributes.append(Attribute("elevation","number","Elevation of the second node of the element",default=0.0))
        self.attributes.append(Attribute("offset","number","Offset of the second node of the element from the R-Z plane",default=0.0))
        self.attributes.append(Attribute("chordLength","number","Chord length of the foil profile",default=0.0))
        self.attributes.append(Attribute("twist","number","Static twist angle",default=0.0))