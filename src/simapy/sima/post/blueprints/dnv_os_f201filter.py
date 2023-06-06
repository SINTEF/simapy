# 
# Generated with DNV_OS_F201FilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class DNV_OS_F201FilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="DNV_OS_F201Filter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("customSafetyClassResistanceFactor","number","Safety class resistance factor (ɣ SC)",default=0.0))
        self.add_attribute(Attribute("useCustomSafetyClassResistanceFactor","boolean","",default=False))
        self.add_attribute(Attribute("customLoadEffectFactorForEnvironmentalLoads","number","Load effect factor for environmental loads (ɣ E)",default=0.0))
        self.add_attribute(Attribute("useCustomLoadEffectFactorForEnvironmentalLoads","boolean","",default=False))
        self.add_attribute(Attribute("customLoadEffectFactorForFunctionalLoads","number","Load effect factor for functional loads (ɣ F)",default=0.0))
        self.add_attribute(Attribute("useCustomLoadEffectFactorForFunctionalLoads","boolean","",default=False))
        self.add_attribute(Attribute("customLoadFactorForAccidentalLoads","number","Load factor for accidental loads (ɣ A)",default=0.0))
        self.add_attribute(Attribute("useCustomLoadFactorForAccidentalLoads","boolean","",default=False))
        self.add_attribute(Attribute("customMaterialResistanceFactor","number","Material resistance factor (ɣ m)",default=0.0))
        self.add_attribute(Attribute("useCustomMaterialResistanceFactor","boolean","",default=False))
        self.add_attribute(Attribute("fabricationFactor","number","Fabrication factor (α fab)",default=0.85))
        self.add_attribute(Attribute("youngsFactor","number","Young's modulus",default=210000000000.0))
        self.add_attribute(Attribute("poissonsRatio","number","Poisson's ratio for pipe wall material",default=0.3))
        self.add_attribute(Attribute("yieldStrength","number","Yield strength to be used in design",default=400000000.0))
        self.add_attribute(Attribute("tensileStrength","number","Tensile strength to be used in design",default=700000000.0))
        self.add_attribute(Attribute("nomOD","number","Nominal outside diameter",default=0.2967))
        self.add_attribute(Attribute("pipeThickness","number","Thickness of pipe",default=0.05))
        self.add_attribute(Attribute("ovality","number","Ovality",default=0.005))
        self.add_attribute(Attribute("extFluidDensity","number","Density of external fluid (e.g. sea water)",default=1025.0))
        self.add_attribute(Attribute("intFluidDensity","number","Density of internal fluid (contents)",default=900.0))
        self.add_attribute(Attribute("refPointPressure","number","Design pressure at reference point",default=500000.0))
        self.add_attribute(Attribute("corrosionAllowance","number","Internal and external corrosion allowance",default=0.001))
        self.add_attribute(EnumAttribute("safetyClass","sima/post/SafetyClass",""))
        self.add_attribute(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.add_attribute(Attribute("useWeibullDistributionFitting","boolean","Calculate characteristic extreme values of utilization factors using Weibull distribution fitting",default=False))
        self.add_attribute(Attribute("lowerThresholdForTailFitting","number","Sample points with probability of non-exceedance below this threshold will not be used when fitting the Weibull distribution",default=0.87))
        self.add_attribute(Attribute("seastateReturnPeriod","number","Return period used for estimating the characteristic extreme value",default=3.0))
        self.add_attribute(Attribute("accelerationOfGravity","number","Acceleration of gravity",default=9.81))