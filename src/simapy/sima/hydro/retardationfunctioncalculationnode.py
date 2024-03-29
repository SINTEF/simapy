# This an autogenerated file
# 
# Generated with RetardationFunctionCalculationNode
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.retardationfunctioncalculationnode import RetardationFunctionCalculationNodeBlueprint
from typing import Dict
from ..post import ControlSignalInputSlot
from ..post import InputSlot
from ..post import OutputSlot
from ..post import RunNode
from ..sima import ScriptableValue

class RetardationFunctionCalculationNode(RunNode):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    radiationData : InputSlot
    structuralMass : InputSlot
    extraDamping : InputSlot
    outputSlot : OutputSlot
    timeStep : float
         Retardation function timeStep(default 0.5)
    powerOfTwo : int
         Length of array used for fft/ifft. Default 2**13.(default 13)
    cutFactor : float
         factor for cut of fft. Default 200(default 200.0)
    useStructuralMass : bool
         Use structural mass together with a cut factor for removing certain degrees of freedom(default True)
    massCutFactor : float
         Factor used together with structural mass to cut a degree of freedom.  Small factor means larger chance of cutting(default 100000.0)
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, timeStep=0.5, powerOfTwo=13, cutFactor=200.0, useStructuralMass=True, massCutFactor=100000.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.radiationData = None
        self.structuralMass = None
        self.extraDamping = None
        self.outputSlot = None
        self.timeStep = timeStep
        self.powerOfTwo = powerOfTwo
        self.cutFactor = cutFactor
        self.useStructuralMass = useStructuralMass
        self.massCutFactor = massCutFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RetardationFunctionCalculationNodeBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def radiationData(self) -> InputSlot:
        """"""
        return self.__radiationData

    @radiationData.setter
    def radiationData(self, value: InputSlot):
        """Set radiationData"""
        self.__radiationData = value

    @property
    def structuralMass(self) -> InputSlot:
        """"""
        return self.__structuralMass

    @structuralMass.setter
    def structuralMass(self, value: InputSlot):
        """Set structuralMass"""
        self.__structuralMass = value

    @property
    def extraDamping(self) -> InputSlot:
        """"""
        return self.__extraDamping

    @extraDamping.setter
    def extraDamping(self, value: InputSlot):
        """Set extraDamping"""
        self.__extraDamping = value

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value

    @property
    def timeStep(self) -> float:
        """Retardation function timeStep"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def powerOfTwo(self) -> int:
        """Length of array used for fft/ifft. Default 2**13."""
        return self.__powerOfTwo

    @powerOfTwo.setter
    def powerOfTwo(self, value: int):
        """Set powerOfTwo"""
        self.__powerOfTwo = int(value)

    @property
    def cutFactor(self) -> float:
        """factor for cut of fft. Default 200"""
        return self.__cutFactor

    @cutFactor.setter
    def cutFactor(self, value: float):
        """Set cutFactor"""
        self.__cutFactor = float(value)

    @property
    def useStructuralMass(self) -> bool:
        """Use structural mass together with a cut factor for removing certain degrees of freedom"""
        return self.__useStructuralMass

    @useStructuralMass.setter
    def useStructuralMass(self, value: bool):
        """Set useStructuralMass"""
        self.__useStructuralMass = bool(value)

    @property
    def massCutFactor(self) -> float:
        """Factor used together with structural mass to cut a degree of freedom.  Small factor means larger chance of cutting"""
        return self.__massCutFactor

    @massCutFactor.setter
    def massCutFactor(self, value: float):
        """Set massCutFactor"""
        self.__massCutFactor = float(value)
