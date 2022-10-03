# This an autogenerated file
# 
# Generated with DNV_OS_F201Filter
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dnv_os_f201filter import DNV_OS_F201FilterBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.limitstatecategory import LimitStateCategory
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.post.safetyclass import SafetyClass
from sima.sima.scriptablevalue import ScriptableValue

class DNV_OS_F201Filter(OperationNode):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    filterInputSlots : List[InputSlot]
    filterOutputSlots : List[OutputSlot]
    customSafetyClassResistanceFactor : float
         Safety class resistance factor (ɣ SC)(default 0.0)
    useCustomSafetyClassResistanceFactor : bool
         (default True)
    customLoadEffectFactorForEnvironmentalLoads : float
         Load effect factor for environmental loads (ɣ E)(default 0.0)
    useCustomLoadEffectFactorForEnvironmentalLoads : bool
         (default True)
    customLoadEffectFactorForFunctionalLoads : float
         Load effect factor for functional loads (ɣ F)(default 0.0)
    useCustomLoadEffectFactorForFunctionalLoads : bool
         (default True)
    customLoadFactorForAccidentalLoads : float
         Load factor for accidental loads (ɣ A)(default 0.0)
    useCustomLoadFactorForAccidentalLoads : bool
         (default True)
    customMaterialResistanceFactor : float
         Material resistance factor (ɣ m)(default 0.0)
    useCustomMaterialResistanceFactor : bool
         (default True)
    fabricationFactor : float
         Fabrication factor (α fab)(default 0.85)
    youngsFactor : float
         Young's modulus(default 210000000000.0)
    poissonsRatio : float
         Poisson's ratio for pipe wall material(default 0.3)
    yieldStrength : float
         Yield strength to be used in design(default 400000000.0)
    tensileStrength : float
         Tensile strength to be used in design(default 700000000.0)
    nomOD : float
         Nominal outside diameter(default 0.2967)
    pipeThickness : float
         Thickness of pipe(default 0.05)
    ovality : float
         Ovality(default 0.005)
    extFluidDensity : float
         Density of external fluid (e.g. sea water)(default 1025.0)
    intFluidDensity : float
         Density of internal fluid (contents)(default 900.0)
    refPointPressure : float
         Design pressure at reference point(default 500000.0)
    corrosionAllowance : float
         Internal and external corrosion allowance(default 0.001)
    safetyClass : SafetyClass
    limitStateCategory : LimitStateCategory
    useWeibullDistributionFitting : bool
         Calculate characteristic extreme values of utilization factors using Weibull distribution fitting(default False)
    lowerThresholdForTailFitting : float
         Sample points with probability of non-exceedance below this threshold will not be used when fitting the Weibull distribution(default 0.87)
    seastateReturnPeriod : float
         Return period used for estimating the characteristic extreme value(default 3.0)
    accelerationOfGravity : float
         Acceleration of gravity(default 9.81)
    """

    def __init__(self , _id="", name="", x=0, y=0, h=0, w=0, customSafetyClassResistanceFactor=0.0, useCustomSafetyClassResistanceFactor=True, customLoadEffectFactorForEnvironmentalLoads=0.0, useCustomLoadEffectFactorForEnvironmentalLoads=True, customLoadEffectFactorForFunctionalLoads=0.0, useCustomLoadEffectFactorForFunctionalLoads=True, customLoadFactorForAccidentalLoads=0.0, useCustomLoadFactorForAccidentalLoads=True, customMaterialResistanceFactor=0.0, useCustomMaterialResistanceFactor=True, fabricationFactor=0.85, youngsFactor=210000000000.0, poissonsRatio=0.3, yieldStrength=400000000.0, tensileStrength=700000000.0, nomOD=0.2967, pipeThickness=0.05, ovality=0.005, extFluidDensity=1025.0, intFluidDensity=900.0, refPointPressure=500000.0, corrosionAllowance=0.001, safetyClass=SafetyClass.LOW, limitStateCategory=LimitStateCategory.SLS, useWeibullDistributionFitting=False, lowerThresholdForTailFitting=0.87, seastateReturnPeriod=3.0, accelerationOfGravity=9.81, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.filterInputSlots = list()
        self.filterOutputSlots = list()
        self.customSafetyClassResistanceFactor = customSafetyClassResistanceFactor
        self.useCustomSafetyClassResistanceFactor = useCustomSafetyClassResistanceFactor
        self.customLoadEffectFactorForEnvironmentalLoads = customLoadEffectFactorForEnvironmentalLoads
        self.useCustomLoadEffectFactorForEnvironmentalLoads = useCustomLoadEffectFactorForEnvironmentalLoads
        self.customLoadEffectFactorForFunctionalLoads = customLoadEffectFactorForFunctionalLoads
        self.useCustomLoadEffectFactorForFunctionalLoads = useCustomLoadEffectFactorForFunctionalLoads
        self.customLoadFactorForAccidentalLoads = customLoadFactorForAccidentalLoads
        self.useCustomLoadFactorForAccidentalLoads = useCustomLoadFactorForAccidentalLoads
        self.customMaterialResistanceFactor = customMaterialResistanceFactor
        self.useCustomMaterialResistanceFactor = useCustomMaterialResistanceFactor
        self.fabricationFactor = fabricationFactor
        self.youngsFactor = youngsFactor
        self.poissonsRatio = poissonsRatio
        self.yieldStrength = yieldStrength
        self.tensileStrength = tensileStrength
        self.nomOD = nomOD
        self.pipeThickness = pipeThickness
        self.ovality = ovality
        self.extFluidDensity = extFluidDensity
        self.intFluidDensity = intFluidDensity
        self.refPointPressure = refPointPressure
        self.corrosionAllowance = corrosionAllowance
        self.safetyClass = safetyClass
        self.limitStateCategory = limitStateCategory
        self.useWeibullDistributionFitting = useWeibullDistributionFitting
        self.lowerThresholdForTailFitting = lowerThresholdForTailFitting
        self.seastateReturnPeriod = seastateReturnPeriod
        self.accelerationOfGravity = accelerationOfGravity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DNV_OS_F201FilterBlueprint()


    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def x(self) -> int:
        """"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """Set x"""
        self.__x = int(value)

    @property
    def y(self) -> int:
        """"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """Set y"""
        self.__y = int(value)

    @property
    def h(self) -> int:
        """"""
        return self.__h

    @h.setter
    def h(self, value: int):
        """Set h"""
        self.__h = int(value)

    @property
    def w(self) -> int:
        """"""
        return self.__w

    @w.setter
    def w(self, value: int):
        """Set w"""
        self.__w = int(value)

    @property
    def controlSignalInputSlots(self) -> List[ControlSignalInputSlot]:
        """"""
        return self.__controlSignalInputSlots

    @controlSignalInputSlots.setter
    def controlSignalInputSlots(self, value: List[ControlSignalInputSlot]):
        """Set controlSignalInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def filterInputSlots(self) -> List[InputSlot]:
        """"""
        return self.__filterInputSlots

    @filterInputSlots.setter
    def filterInputSlots(self, value: List[InputSlot]):
        """Set filterInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__filterInputSlots = value

    @property
    def filterOutputSlots(self) -> List[OutputSlot]:
        """"""
        return self.__filterOutputSlots

    @filterOutputSlots.setter
    def filterOutputSlots(self, value: List[OutputSlot]):
        """Set filterOutputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__filterOutputSlots = value

    @property
    def customSafetyClassResistanceFactor(self) -> float:
        """Safety class resistance factor (ɣ SC)"""
        return self.__customSafetyClassResistanceFactor

    @customSafetyClassResistanceFactor.setter
    def customSafetyClassResistanceFactor(self, value: float):
        """Set customSafetyClassResistanceFactor"""
        self.__customSafetyClassResistanceFactor = float(value)

    @property
    def useCustomSafetyClassResistanceFactor(self) -> bool:
        """"""
        return self.__useCustomSafetyClassResistanceFactor

    @useCustomSafetyClassResistanceFactor.setter
    def useCustomSafetyClassResistanceFactor(self, value: bool):
        """Set useCustomSafetyClassResistanceFactor"""
        self.__useCustomSafetyClassResistanceFactor = bool(value)

    @property
    def customLoadEffectFactorForEnvironmentalLoads(self) -> float:
        """Load effect factor for environmental loads (ɣ E)"""
        return self.__customLoadEffectFactorForEnvironmentalLoads

    @customLoadEffectFactorForEnvironmentalLoads.setter
    def customLoadEffectFactorForEnvironmentalLoads(self, value: float):
        """Set customLoadEffectFactorForEnvironmentalLoads"""
        self.__customLoadEffectFactorForEnvironmentalLoads = float(value)

    @property
    def useCustomLoadEffectFactorForEnvironmentalLoads(self) -> bool:
        """"""
        return self.__useCustomLoadEffectFactorForEnvironmentalLoads

    @useCustomLoadEffectFactorForEnvironmentalLoads.setter
    def useCustomLoadEffectFactorForEnvironmentalLoads(self, value: bool):
        """Set useCustomLoadEffectFactorForEnvironmentalLoads"""
        self.__useCustomLoadEffectFactorForEnvironmentalLoads = bool(value)

    @property
    def customLoadEffectFactorForFunctionalLoads(self) -> float:
        """Load effect factor for functional loads (ɣ F)"""
        return self.__customLoadEffectFactorForFunctionalLoads

    @customLoadEffectFactorForFunctionalLoads.setter
    def customLoadEffectFactorForFunctionalLoads(self, value: float):
        """Set customLoadEffectFactorForFunctionalLoads"""
        self.__customLoadEffectFactorForFunctionalLoads = float(value)

    @property
    def useCustomLoadEffectFactorForFunctionalLoads(self) -> bool:
        """"""
        return self.__useCustomLoadEffectFactorForFunctionalLoads

    @useCustomLoadEffectFactorForFunctionalLoads.setter
    def useCustomLoadEffectFactorForFunctionalLoads(self, value: bool):
        """Set useCustomLoadEffectFactorForFunctionalLoads"""
        self.__useCustomLoadEffectFactorForFunctionalLoads = bool(value)

    @property
    def customLoadFactorForAccidentalLoads(self) -> float:
        """Load factor for accidental loads (ɣ A)"""
        return self.__customLoadFactorForAccidentalLoads

    @customLoadFactorForAccidentalLoads.setter
    def customLoadFactorForAccidentalLoads(self, value: float):
        """Set customLoadFactorForAccidentalLoads"""
        self.__customLoadFactorForAccidentalLoads = float(value)

    @property
    def useCustomLoadFactorForAccidentalLoads(self) -> bool:
        """"""
        return self.__useCustomLoadFactorForAccidentalLoads

    @useCustomLoadFactorForAccidentalLoads.setter
    def useCustomLoadFactorForAccidentalLoads(self, value: bool):
        """Set useCustomLoadFactorForAccidentalLoads"""
        self.__useCustomLoadFactorForAccidentalLoads = bool(value)

    @property
    def customMaterialResistanceFactor(self) -> float:
        """Material resistance factor (ɣ m)"""
        return self.__customMaterialResistanceFactor

    @customMaterialResistanceFactor.setter
    def customMaterialResistanceFactor(self, value: float):
        """Set customMaterialResistanceFactor"""
        self.__customMaterialResistanceFactor = float(value)

    @property
    def useCustomMaterialResistanceFactor(self) -> bool:
        """"""
        return self.__useCustomMaterialResistanceFactor

    @useCustomMaterialResistanceFactor.setter
    def useCustomMaterialResistanceFactor(self, value: bool):
        """Set useCustomMaterialResistanceFactor"""
        self.__useCustomMaterialResistanceFactor = bool(value)

    @property
    def fabricationFactor(self) -> float:
        """Fabrication factor (α fab)"""
        return self.__fabricationFactor

    @fabricationFactor.setter
    def fabricationFactor(self, value: float):
        """Set fabricationFactor"""
        self.__fabricationFactor = float(value)

    @property
    def youngsFactor(self) -> float:
        """Young's modulus"""
        return self.__youngsFactor

    @youngsFactor.setter
    def youngsFactor(self, value: float):
        """Set youngsFactor"""
        self.__youngsFactor = float(value)

    @property
    def poissonsRatio(self) -> float:
        """Poisson's ratio for pipe wall material"""
        return self.__poissonsRatio

    @poissonsRatio.setter
    def poissonsRatio(self, value: float):
        """Set poissonsRatio"""
        self.__poissonsRatio = float(value)

    @property
    def yieldStrength(self) -> float:
        """Yield strength to be used in design"""
        return self.__yieldStrength

    @yieldStrength.setter
    def yieldStrength(self, value: float):
        """Set yieldStrength"""
        self.__yieldStrength = float(value)

    @property
    def tensileStrength(self) -> float:
        """Tensile strength to be used in design"""
        return self.__tensileStrength

    @tensileStrength.setter
    def tensileStrength(self, value: float):
        """Set tensileStrength"""
        self.__tensileStrength = float(value)

    @property
    def nomOD(self) -> float:
        """Nominal outside diameter"""
        return self.__nomOD

    @nomOD.setter
    def nomOD(self, value: float):
        """Set nomOD"""
        self.__nomOD = float(value)

    @property
    def pipeThickness(self) -> float:
        """Thickness of pipe"""
        return self.__pipeThickness

    @pipeThickness.setter
    def pipeThickness(self, value: float):
        """Set pipeThickness"""
        self.__pipeThickness = float(value)

    @property
    def ovality(self) -> float:
        """Ovality"""
        return self.__ovality

    @ovality.setter
    def ovality(self, value: float):
        """Set ovality"""
        self.__ovality = float(value)

    @property
    def extFluidDensity(self) -> float:
        """Density of external fluid (e.g. sea water)"""
        return self.__extFluidDensity

    @extFluidDensity.setter
    def extFluidDensity(self, value: float):
        """Set extFluidDensity"""
        self.__extFluidDensity = float(value)

    @property
    def intFluidDensity(self) -> float:
        """Density of internal fluid (contents)"""
        return self.__intFluidDensity

    @intFluidDensity.setter
    def intFluidDensity(self, value: float):
        """Set intFluidDensity"""
        self.__intFluidDensity = float(value)

    @property
    def refPointPressure(self) -> float:
        """Design pressure at reference point"""
        return self.__refPointPressure

    @refPointPressure.setter
    def refPointPressure(self, value: float):
        """Set refPointPressure"""
        self.__refPointPressure = float(value)

    @property
    def corrosionAllowance(self) -> float:
        """Internal and external corrosion allowance"""
        return self.__corrosionAllowance

    @corrosionAllowance.setter
    def corrosionAllowance(self, value: float):
        """Set corrosionAllowance"""
        self.__corrosionAllowance = float(value)

    @property
    def safetyClass(self) -> SafetyClass:
        """"""
        return self.__safetyClass

    @safetyClass.setter
    def safetyClass(self, value: SafetyClass):
        """Set safetyClass"""
        self.__safetyClass = value

    @property
    def limitStateCategory(self) -> LimitStateCategory:
        """"""
        return self.__limitStateCategory

    @limitStateCategory.setter
    def limitStateCategory(self, value: LimitStateCategory):
        """Set limitStateCategory"""
        self.__limitStateCategory = value

    @property
    def useWeibullDistributionFitting(self) -> bool:
        """Calculate characteristic extreme values of utilization factors using Weibull distribution fitting"""
        return self.__useWeibullDistributionFitting

    @useWeibullDistributionFitting.setter
    def useWeibullDistributionFitting(self, value: bool):
        """Set useWeibullDistributionFitting"""
        self.__useWeibullDistributionFitting = bool(value)

    @property
    def lowerThresholdForTailFitting(self) -> float:
        """Sample points with probability of non-exceedance below this threshold will not be used when fitting the Weibull distribution"""
        return self.__lowerThresholdForTailFitting

    @lowerThresholdForTailFitting.setter
    def lowerThresholdForTailFitting(self, value: float):
        """Set lowerThresholdForTailFitting"""
        self.__lowerThresholdForTailFitting = float(value)

    @property
    def seastateReturnPeriod(self) -> float:
        """Return period used for estimating the characteristic extreme value"""
        return self.__seastateReturnPeriod

    @seastateReturnPeriod.setter
    def seastateReturnPeriod(self, value: float):
        """Set seastateReturnPeriod"""
        self.__seastateReturnPeriod = float(value)

    @property
    def accelerationOfGravity(self) -> float:
        """Acceleration of gravity"""
        return self.__accelerationOfGravity

    @accelerationOfGravity.setter
    def accelerationOfGravity(self, value: float):
        """Set accelerationOfGravity"""
        self.__accelerationOfGravity = float(value)
