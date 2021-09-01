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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("specifyVerticalDomain","boolean","Should a vertical grid for interpolation of wind velocity be specified?",default=False))
        self.attributes.append(Attribute("numberOfLevels","integer","Number of vertical levels to pre-generate wind time series for",default=0))
        self.attributes.append(Attribute("zMinimum","number","Lower limit of vertical domain",default=0.0))
        self.attributes.append(Attribute("zMaximum","number","Upper limit of vertical domain",default=0.0))
        self.attributes.append(Attribute("allowOutsideDomain","boolean","Should computation of wind velocity outside specified limits be allowed?",default=False))