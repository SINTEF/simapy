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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("hs","number","",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("interval5","number","",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("mean","number","",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("interval95","number","",Dimension("size",""),default=0.0))