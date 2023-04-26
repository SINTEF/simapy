# This an autogenerated file
# 
# Generated with LiftLineCoupling
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.liftlinecoupling import LiftLineCouplingBlueprint
from typing import Dict
from .activationfailuremode import ActivationFailureMode
from .simplecoupling import SimpleCoupling
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simobodypoint import SIMOBodyPoint

class LiftLineCoupling(SimpleCoupling):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    endPoint1 : SIMOBodyPoint
    endPoint2 : SIMOBodyPoint
    failureMode : ActivationFailureMode
         Failure mode of coupling element
    failureTime : float
         Earliest possible time of failure(default 0.0)
    breakingStrength : float
         Breaking strength(default 0.0)
    numElements : int
         Number of elements(default 0)
    accIncluded : bool
         Flag for including acceleration of the line(default False)
    diameter : float
         Segment diameter(default 0.0)
    eMod : float
         Modulus of elasticity(default 0.0)
    emFac : int
         Factor of elasticity - 2 for chains - 1 for other segment types(default 1)
    length : float
         Initial, unstretched wire length(default 0.0)
    flexibility : float
         Connection flexibility(default 0.0)
    damping : float
         Material damping(default 0.0)
    uwia : float
         Unit weight in air(default 0.0)
    watfac : float
         The ratio of weight in water to weight in air(default 0.0)
    transverseDrag : float
         Transverse drag coefficient(default 0.0)
    longitudinalDrag : float
         Longitudinal drag coefficient(default 0.0)
    """

    def __init__(self , description="", failureMode=ActivationFailureMode.NONE, failureTime=0.0, breakingStrength=0.0, numElements=0, accIncluded=False, diameter=0.0, eMod=0.0, emFac=1, length=0.0, flexibility=0.0, damping=0.0, uwia=0.0, watfac=0.0, transverseDrag=0.0, longitudinalDrag=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.endPoint1 = None
        self.endPoint2 = None
        self.failureMode = failureMode
        self.failureTime = failureTime
        self.breakingStrength = breakingStrength
        self.numElements = numElements
        self.accIncluded = accIncluded
        self.diameter = diameter
        self.eMod = eMod
        self.emFac = emFac
        self.length = length
        self.flexibility = flexibility
        self.damping = damping
        self.uwia = uwia
        self.watfac = watfac
        self.transverseDrag = transverseDrag
        self.longitudinalDrag = longitudinalDrag
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LiftLineCouplingBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
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
    def endPoint1(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint1

    @endPoint1.setter
    def endPoint1(self, value: SIMOBodyPoint):
        """Set endPoint1"""
        self.__endPoint1 = value

    @property
    def endPoint2(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint2

    @endPoint2.setter
    def endPoint2(self, value: SIMOBodyPoint):
        """Set endPoint2"""
        self.__endPoint2 = value

    @property
    def failureMode(self) -> ActivationFailureMode:
        """Failure mode of coupling element"""
        return self.__failureMode

    @failureMode.setter
    def failureMode(self, value: ActivationFailureMode):
        """Set failureMode"""
        self.__failureMode = value

    @property
    def failureTime(self) -> float:
        """Earliest possible time of failure"""
        return self.__failureTime

    @failureTime.setter
    def failureTime(self, value: float):
        """Set failureTime"""
        self.__failureTime = float(value)

    @property
    def breakingStrength(self) -> float:
        """Breaking strength"""
        return self.__breakingStrength

    @breakingStrength.setter
    def breakingStrength(self, value: float):
        """Set breakingStrength"""
        self.__breakingStrength = float(value)

    @property
    def numElements(self) -> int:
        """Number of elements"""
        return self.__numElements

    @numElements.setter
    def numElements(self, value: int):
        """Set numElements"""
        self.__numElements = int(value)

    @property
    def accIncluded(self) -> bool:
        """Flag for including acceleration of the line"""
        return self.__accIncluded

    @accIncluded.setter
    def accIncluded(self, value: bool):
        """Set accIncluded"""
        self.__accIncluded = bool(value)

    @property
    def diameter(self) -> float:
        """Segment diameter"""
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float):
        """Set diameter"""
        self.__diameter = float(value)

    @property
    def eMod(self) -> float:
        """Modulus of elasticity"""
        return self.__eMod

    @eMod.setter
    def eMod(self, value: float):
        """Set eMod"""
        self.__eMod = float(value)

    @property
    def emFac(self) -> int:
        """Factor of elasticity - 2 for chains - 1 for other segment types"""
        return self.__emFac

    @emFac.setter
    def emFac(self, value: int):
        """Set emFac"""
        self.__emFac = int(value)

    @property
    def length(self) -> float:
        """Initial, unstretched wire length"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def flexibility(self) -> float:
        """Connection flexibility"""
        return self.__flexibility

    @flexibility.setter
    def flexibility(self, value: float):
        """Set flexibility"""
        self.__flexibility = float(value)

    @property
    def damping(self) -> float:
        """Material damping"""
        return self.__damping

    @damping.setter
    def damping(self, value: float):
        """Set damping"""
        self.__damping = float(value)

    @property
    def uwia(self) -> float:
        """Unit weight in air"""
        return self.__uwia

    @uwia.setter
    def uwia(self, value: float):
        """Set uwia"""
        self.__uwia = float(value)

    @property
    def watfac(self) -> float:
        """The ratio of weight in water to weight in air"""
        return self.__watfac

    @watfac.setter
    def watfac(self, value: float):
        """Set watfac"""
        self.__watfac = float(value)

    @property
    def transverseDrag(self) -> float:
        """Transverse drag coefficient"""
        return self.__transverseDrag

    @transverseDrag.setter
    def transverseDrag(self, value: float):
        """Set transverseDrag"""
        self.__transverseDrag = float(value)

    @property
    def longitudinalDrag(self) -> float:
        """Longitudinal drag coefficient"""
        return self.__longitudinalDrag

    @longitudinalDrag.setter
    def longitudinalDrag(self, value: float):
        """Set longitudinalDrag"""
        self.__longitudinalDrag = float(value)