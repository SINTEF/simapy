# 
# Generated with BladeElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class BladeElementBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="BladeElement", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("elementLength","number","Blade element length",default=0.0))
        self.add_attribute(Attribute("chordLength","number","Chord length of the foil profile",default=0.0))
        self.add_attribute(Attribute("twist","number","Twist angle",default=0.0))