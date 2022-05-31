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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("customSafetyClassResistanceFactor","number","Safety class resistance factor (ɣ SC)",default=0.0))
        self.attributes.append(Attribute("useCustomSafetyClassResistanceFactor","boolean","",default=True))
        self.attributes.append(Attribute("customLoadEffectFactorForEnvironmentalLoads","number","Load effect factor for environmental loads (ɣ E)",default=0.0))
        self.attributes.append(Attribute("useCustomLoadEffectFactorForEnvironmentalLoads","boolean","",default=True))
        self.attributes.append(Attribute("customLoadEffectFactorForFunctionalLoads","number","Load effect factor for functional loads (ɣ F)",default=0.0))
        self.attributes.append(Attribute("useCustomLoadEffectFactorForFunctionalLoads","boolean","",default=True))
        self.attributes.append(Attribute("customLoadFactorForAccidentalLoads","number","Load factor for accidental loads (ɣ A)",default=0.0))
        self.attributes.append(Attribute("useCustomLoadFactorForAccidentalLoads","boolean","",default=True))
        self.attributes.append(Attribute("customMaterialResistanceFactor","number","Material resistance factor (ɣ m)",default=0.0))
        self.attributes.append(Attribute("useCustomMaterialResistanceFactor","boolean","",default=True))
        self.attributes.append(Attribute("fabricationFactor","number","Fabrication factor (α fab)",default=0.85))
        self.attributes.append(Attribute("youngsFactor","number","Young's modulus",default=210000000000.0))
        self.attributes.append(Attribute("poissonsRatio","number","Poisson's ratio for pipe wall material",default=0.3))
        self.attributes.append(Attribute("yieldStrength","number","Yield strength to be used in design",default=400000000.0))
        self.attributes.append(Attribute("tensileStrength","number","Tensile strength to be used in design",default=700000000.0))
        self.attributes.append(Attribute("nomOD","number","Nominal outside diameter",default=0.2967))
        self.attributes.append(Attribute("pipeThickness","number","Thickness of pipe",default=0.05))
        self.attributes.append(Attribute("ovality","number","Ovality",default=0.005))
        self.attributes.append(Attribute("extFluidDensity","number","Density of external fluid (e.g. sea water)",default=1025.0))
        self.attributes.append(Attribute("intFluidDensity","number","Density of internal fluid (contents)",default=900.0))
        self.attributes.append(Attribute("refPointPressure","number","Design pressure at reference point",default=500000.0))
        self.attributes.append(Attribute("corrosionAllowance","number","Internal and external corrosion allowance",default=0.001))
        self.attributes.append(EnumAttribute("safetyClass","sima/post/SafetyClass",""))
        self.attributes.append(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.attributes.append(Attribute("useWeibullDistributionFitting","boolean","Calculate characteristic extreme values of utilization factors using Weibull distribution fitting",default=False))
        self.attributes.append(Attribute("lowerThresholdForTailFitting","number","Sample points with probability of non-exceedance below this threshold will not be used when fitting the Weibull distribution",default=0.87))
        self.attributes.append(Attribute("seastateReturnPeriod","number","Return period used for estimating the characteristic extreme value",default=3.0))
        self.attributes.append(Attribute("accelerationOfGravity","number","Acceleration of gravity",default=9.81))