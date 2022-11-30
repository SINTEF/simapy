# This an autogenerated file
# 
# Generated with SNCurve
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.sncurve import SNCurveBlueprint
from typing import Dict
from sima.post.fatiguelimitindicator import FatigueLimitIndicator
from sima.post.sncurveitem import SNCurveItem
from sima.post.sncurvetype import SNCurveType
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class SNCurve(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    usePredefinedCurve : bool
         Use predefined SN-curve from selected standard(default False)
    predefinedCurve : SNCurveType
    negativeInverseSlope : float
         Negative inverse slope of the segment (first segment if several segments are given, or total curve if no more are given)(default 0.0)
    interceptStress : float
         Stress range resulting in failure after one cycle(default 0.0)
    thicknessExponent : float
         Thickness exponent on fatigue strength(default 1.0)
    referenceThicknessFactor : float
         t/t_ref:  where t is thickness through which a crack will most likely grow and t_ref i reference thickness(default 1.0)
    curveItems : List[SNCurveItem]
    fatigueLimitIndicator : FatigueLimitIndicator
    fatigueLimitStress : float
         Stress range level for which the SN curve becomes horizontal.(default 0.0)
    fatigueLimitCycles : float
         Logarithm of number of stress cycles for which the SN curve becomes horizontal.(default 0.0)
    """

    def __init__(self , description="", usePredefinedCurve=False, predefinedCurve=SNCurveType.DNV_B1, negativeInverseSlope=0.0, interceptStress=0.0, thicknessExponent=1.0, referenceThicknessFactor=1.0, fatigueLimitIndicator=FatigueLimitIndicator.STRESS_RANGE, fatigueLimitStress=0.0, fatigueLimitCycles=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.usePredefinedCurve = usePredefinedCurve
        self.predefinedCurve = predefinedCurve
        self.negativeInverseSlope = negativeInverseSlope
        self.interceptStress = interceptStress
        self.thicknessExponent = thicknessExponent
        self.referenceThicknessFactor = referenceThicknessFactor
        self.curveItems = list()
        self.fatigueLimitIndicator = fatigueLimitIndicator
        self.fatigueLimitStress = fatigueLimitStress
        self.fatigueLimitCycles = fatigueLimitCycles
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SNCurveBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

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
        self.__name = value

    @property
    def usePredefinedCurve(self) -> bool:
        """Use predefined SN-curve from selected standard"""
        return self.__usePredefinedCurve

    @usePredefinedCurve.setter
    def usePredefinedCurve(self, value: bool):
        """Set usePredefinedCurve"""
        self.__usePredefinedCurve = bool(value)

    @property
    def predefinedCurve(self) -> SNCurveType:
        """"""
        return self.__predefinedCurve

    @predefinedCurve.setter
    def predefinedCurve(self, value: SNCurveType):
        """Set predefinedCurve"""
        self.__predefinedCurve = value

    @property
    def negativeInverseSlope(self) -> float:
        """Negative inverse slope of the segment (first segment if several segments are given, or total curve if no more are given)"""
        return self.__negativeInverseSlope

    @negativeInverseSlope.setter
    def negativeInverseSlope(self, value: float):
        """Set negativeInverseSlope"""
        self.__negativeInverseSlope = float(value)

    @property
    def interceptStress(self) -> float:
        """Stress range resulting in failure after one cycle"""
        return self.__interceptStress

    @interceptStress.setter
    def interceptStress(self, value: float):
        """Set interceptStress"""
        self.__interceptStress = float(value)

    @property
    def thicknessExponent(self) -> float:
        """Thickness exponent on fatigue strength"""
        return self.__thicknessExponent

    @thicknessExponent.setter
    def thicknessExponent(self, value: float):
        """Set thicknessExponent"""
        self.__thicknessExponent = float(value)

    @property
    def referenceThicknessFactor(self) -> float:
        """t/t_ref:  where t is thickness through which a crack will most likely grow and t_ref i reference thickness"""
        return self.__referenceThicknessFactor

    @referenceThicknessFactor.setter
    def referenceThicknessFactor(self, value: float):
        """Set referenceThicknessFactor"""
        self.__referenceThicknessFactor = float(value)

    @property
    def curveItems(self) -> List[SNCurveItem]:
        """"""
        return self.__curveItems

    @curveItems.setter
    def curveItems(self, value: List[SNCurveItem]):
        """Set curveItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__curveItems = value

    @property
    def fatigueLimitIndicator(self) -> FatigueLimitIndicator:
        """"""
        return self.__fatigueLimitIndicator

    @fatigueLimitIndicator.setter
    def fatigueLimitIndicator(self, value: FatigueLimitIndicator):
        """Set fatigueLimitIndicator"""
        self.__fatigueLimitIndicator = value

    @property
    def fatigueLimitStress(self) -> float:
        """Stress range level for which the SN curve becomes horizontal."""
        return self.__fatigueLimitStress

    @fatigueLimitStress.setter
    def fatigueLimitStress(self, value: float):
        """Set fatigueLimitStress"""
        self.__fatigueLimitStress = float(value)

    @property
    def fatigueLimitCycles(self) -> float:
        """Logarithm of number of stress cycles for which the SN curve becomes horizontal."""
        return self.__fatigueLimitCycles

    @fatigueLimitCycles.setter
    def fatigueLimitCycles(self, value: float):
        """Set fatigueLimitCycles"""
        self.__fatigueLimitCycles = float(value)
