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
        self.add_attribute(Attribute("cutFactor","number","factor for cut of fft. Default 200",default=200.0))
        self.add_attribute(Attribute("powerOfTwo","integer","Length of array used for fft/ifft. Default 2**13.",default=13))
        self.add_attribute(Attribute("massCutFactor","number","Factor used together with structural mass to cut a degree of freedom.  Small factor means larger chance of cutting",default=100000.0))