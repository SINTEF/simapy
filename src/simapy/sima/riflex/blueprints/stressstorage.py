# 
# Generated with StressStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class StressStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StressStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("elements","sima/riflex/ElementStressStorage","Elements to calculate pipe wall stress for. RIFLEX calculates it from the element forces stored in HDF5",True,Dimension("*")))