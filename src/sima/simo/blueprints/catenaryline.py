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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("attachmentPoint","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(Attribute("direction","number","Direction of line in horizontal plane",default=0.0))
        self.attributes.append(Attribute("xglobal","number","X-coordinate of the anchor in global coordinate\nsystem",default=0.0))
        self.attributes.append(Attribute("yglobal","number","Y-coordinate of the anchor in global coordinate\nsystem",default=0.0))
        self.attributes.append(Attribute("xwinch","number","Run length of winch",default=0.0))
        self.attributes.append(Attribute("xhor","number","Horizontal distance from attachment point\nto anchor",default=0.0))
        self.attributes.append(Attribute("pretension","number","Pretension",default=0.0))
        self.attributes.append(BlueprintAttribute("lineType","sima/simo/LineType","",False))
        self.attributes.append(EnumAttribute("inputMethod","sima/simo/InputMethodType","Method for initialization of line"))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/FailureMode","Failure mode of positioning element"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))