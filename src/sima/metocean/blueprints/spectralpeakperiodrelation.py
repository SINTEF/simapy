# 
# Generated with SpectralPeakPeriodRelationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SpectralPeakPeriodRelationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SpectralPeakPeriodRelation", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("hs","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("interval5","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("mean","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("interval95","number","",Dimension("*"),default=0.0))