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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("elongationCharacteristics","sima/simo/ElongationCharacteristic","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("lines","sima/simo/CatenaryLine","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("segmentedLineTypes","sima/simo/SegmentedLineType","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("buoys","sima/simo/BuoyType","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("directInputLineTypes","sima/simo/DirectInputLineType","",True,Dimension("*")))