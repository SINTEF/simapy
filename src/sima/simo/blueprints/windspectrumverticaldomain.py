# 
# Generated with WindSpectrumVerticalDomainBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WindSpectrumVerticalDomainBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WindSpectrumVerticalDomain", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("specifyVerticalDomain","boolean","Should a vertical grid for interpolation of wind velocity be specified?",default=False))
        self.add_attribute(Attribute("numberOfLevels","integer","Number of vertical levels to pre-generate wind time series for",default=0))
        self.add_attribute(Attribute("zMinimum","number","Lower limit of vertical domain",default=0.0))
        self.add_attribute(Attribute("zMaximum","number","Upper limit of vertical domain",default=0.0))
        self.add_attribute(Attribute("allowOutsideDomain","boolean","Should computation of wind velocity outside specified limits be allowed?",default=False))