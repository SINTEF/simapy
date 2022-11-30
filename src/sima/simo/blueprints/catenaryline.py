# 
# Generated with CatenaryLineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class CatenaryLineBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="CatenaryLine", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attachmentPoint","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(Attribute("direction","number","Direction of line in horizontal plane",default=0.0))
        self.add_attribute(Attribute("xglobal","number","X-coordinate of the anchor in global coordinate\nsystem",default=0.0))
        self.add_attribute(Attribute("yglobal","number","Y-coordinate of the anchor in global coordinate\nsystem",default=0.0))
        self.add_attribute(Attribute("xwinch","number","Run length of winch",default=0.0))
        self.add_attribute(Attribute("xhor","number","Horizontal distance from attachment point\nto anchor",default=0.0))
        self.add_attribute(Attribute("pretension","number","Pretension",default=0.0))
        self.add_attribute(BlueprintAttribute("lineType","sima/simo/LineType","",False))
        self.add_attribute(EnumAttribute("inputMethod","sima/simo/InputMethodType","Method for initialization of line"))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/FailureMode","Failure mode of positioning element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))