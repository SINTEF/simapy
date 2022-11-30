# 
# Generated with BladeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BladeItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BladeItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("airfoil","sima/windturbine/Airfoil","",False))
        self.add_attribute(Attribute("elementLength","number","Element length",default=0.0))
        self.add_attribute(Attribute("chordLength","number","Chord length",default=0.0))
        self.add_attribute(Attribute("twist","number","Airfoil twist",default=0.0))