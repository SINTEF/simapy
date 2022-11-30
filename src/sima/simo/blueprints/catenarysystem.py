# 
# Generated with CatenarySystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CatenarySystemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CatenarySystem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("elongationCharacteristics","sima/simo/ElongationCharacteristic","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("lines","sima/simo/CatenaryLine","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("segmentedLineTypes","sima/simo/SegmentedLineType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("buoys","sima/simo/BuoyType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("directInputLineTypes","sima/simo/DirectInputLineType","",True,Dimension("*")))