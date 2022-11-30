# 
# Generated with WamitWaveBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WamitWaveBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WamitWave", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("periods","number","Wave periods",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("headings","number","Wave headings",Dimension("*"),default=0.0))