# 
# Generated with BladeElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BladeElementBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BladeElement", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("elementLength","number","Blade element length",default=0.0))
        self.attributes.append(Attribute("chordLength","number","Chord length of the foil profile",default=0.0))
        self.attributes.append(Attribute("twist","number","Twist angle",default=0.0))