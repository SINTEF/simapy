# 
# Generated with SesamResultExportBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class SesamResultExportBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SesamResultExport", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("floaterBody","sima/simo/SIMOBody","",False))
        self.add_attribute(BlueprintAttribute("pointForces","sima/simo/BodyForceComponentReference","",True,Dimension("*")))