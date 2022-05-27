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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("airfoil","sima/windturbine/Airfoil","",False))
        self.attributes.append(Attribute("elementLength","number","Element length",default=0.0))
        self.attributes.append(Attribute("chordLength","number","Chord length",default=0.0))
        self.attributes.append(Attribute("twist","number","Airfoil twist",default=0.0))