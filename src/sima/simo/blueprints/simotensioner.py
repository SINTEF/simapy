# 
# Generated with SIMOTensionerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class SIMOTensionerBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="SIMOTensioner", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("pretension","number","Pretension in tensioner",default=0.0))
        self.add_attribute(Attribute("maxRate","number","Max. rate of change in pretension",default=0.0))
        self.add_attribute(Attribute("stiffness","number","Stiffness at specified pretension",default=0.0))
        self.add_attribute(Attribute("strokeLength","number","Stiffness at specified pretension",default=0.0))