# 
# Generated with RetardationFunctionCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class RetardationFunctionCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RetardationFunctionCalculationParameters", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("timeStep","number","Retardation function timeStep",default=0.5))
        self.add_attribute(Attribute("useLimitingFrequencies","boolean","Use added mass zero and/or added mass infinite if these exist",default=True))
        self.add_attribute(Attribute("cutFactor","number","Factor determining the duration of the significant part of the retardation function; the near-zero tail is truncated from the right. Large cut factor means longer duration (less truncation). Default 200.",default=200.0))
        self.add_attribute(Attribute("powerOfTwo","integer","Exponent n: the FFT uses 2^n samples, and the retardation function has at most 2^(n-1) samples before the near-zero tail is truncated (see Cut factor). Default 13.",default=13))
        self.add_attribute(Attribute("massCutFactor","number","Factor used together with structural mass to determine which coupling terms in the retardation function matrix are close to zero at all t and can be neglected. Small factor means larger chance of neglecting coupling terms. Only used when structural mass is available.",default=100000.0))