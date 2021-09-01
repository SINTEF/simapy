# 
# Generated with WinchBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class WinchBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="Winch", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("controlType","sima/simo/WinchControl","Type of coupling winch control"))
        self.attributes.append(Attribute("maximumSpeed","number","Max. run velocity for winch",default=0.0))
        self.attributes.append(Attribute("acceleration","number","Max. run acceleration for winch",default=0.0))
        self.attributes.append(Attribute("maximumLength","number","Max. wire length that can be added to drum",default=0.0))
        self.attributes.append(Attribute("drumLength","number","Initial wire length at drum",default=0.0))
        self.attributes.append(BlueprintAttribute("intervals","sima/simo/WinchRunInterval","",True,Dimension("size","")))