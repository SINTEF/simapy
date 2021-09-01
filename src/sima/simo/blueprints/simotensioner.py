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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("pretension","number","Pretension in tensioner",default=0.0))
        self.attributes.append(Attribute("maxRate","number","Max. rate of change in pretension",default=0.0))
        self.attributes.append(Attribute("stiffness","number","Stiffness at specified pretension",default=0.0))
        self.attributes.append(Attribute("strokeLength","number","Stiffness at specified pretension",default=0.0))