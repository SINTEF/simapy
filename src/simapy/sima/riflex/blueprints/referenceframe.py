# 
# Generated with ReferenceFrameBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.namedobject import NamedObjectBlueprint

class ReferenceFrameBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ReferenceFrame", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parent","sima/riflex/ReferenceFrame","",False))
        self.add_attribute(Attribute("xLocal","number","Local (in parent frame) coordinate X",default=0.0))
        self.add_attribute(Attribute("yLocal","number","Local (in parent frame) coordinate Y",default=0.0))
        self.add_attribute(Attribute("zLocal","number","Local (in parent frame) coordinate Z",default=0.0))
        self.add_attribute(Attribute("rxLocal","number","Local (relative to parent frame)  X-axis rotation",default=0.0))
        self.add_attribute(Attribute("ryLocal","number","Local (relative to parent frame)  Y-axis rotation",default=0.0))
        self.add_attribute(Attribute("rzLocal","number","Local (relative to parent frame)  Z-axis rotation",default=0.0))