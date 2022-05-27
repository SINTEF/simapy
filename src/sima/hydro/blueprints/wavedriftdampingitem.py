# 
# Generated with WaveDriftDampingItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WaveDriftDampingItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WaveDriftDampingItem", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("period","number","Period",default=0.0))
        self.attributes.append(Attribute("wd1","number","Wave drift damping coefficient surge. Relative change in drift force for unit velocity.",default=0.0))
        self.attributes.append(Attribute("wd2","number","Wave drift damping coefficient sway. Relative change in drift force for unit velocity.",default=0.0))
        self.attributes.append(Attribute("wd3","number","Wave drift damping coefficient heave. Relative change in drift force for unit velocity.",default=0.0))
        self.attributes.append(Attribute("wd4","number","Wave drift damping coefficient roll. Relative change in drift force for unit velocity.",default=0.0))
        self.attributes.append(Attribute("wd5","number","Wave drift damping coefficient pitch. Relative change in drift force for unit velocity.",default=0.0))
        self.attributes.append(Attribute("wd6","number","Wave drift damping coefficient yaw. Relative change in drift force for unit velocity.",default=0.0))