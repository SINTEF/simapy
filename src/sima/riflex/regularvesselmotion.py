# This an autogenerated file
# 
# Generated with RegularVesselMotion
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.regularvesselmotion import RegularVesselMotionBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.supportvessel import SupportVessel

class RegularVesselMotion(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    supportVessel : SupportVessel
    amplitudeX : float
         Motion amplitude, x-direction(default 0.0)
    amplitudeY : float
         Motion amplitude, y-direction(default 0.0)
    amplitudeZ : float
         Motion amplitude, z-direction(default 0.0)
    amplitudeXR : float
         Motion amplitude, x-rotation(default 0.0)
    amplitudeYR : float
         Motion amplitude, y-rotation(default 0.0)
    amplitudeZR : float
         Motion amplitude, z-rotation(default 0.0)
    period : float
         Period of motion(default 0.0)
    phaseX : float
         Phase angle, x-motion(default 0.0)
    phaseY : float
         Phase angle, y-motion(default 0.0)
    phaseZ : float
         Phase angle, z-motion(default 0.0)
    phaseXR : float
         Phase angle, x-rotation(default 0.0)
    phaseYR : float
         Phase angle, y-rotation(default 0.0)
    phaseZR : float
         Phase angle, z-rotation(default 0.0)
    """

    def __init__(self , description="", _id=None, amplitudeX=0.0, amplitudeY=0.0, amplitudeZ=0.0, amplitudeXR=0.0, amplitudeYR=0.0, amplitudeZR=0.0, period=0.0, phaseX=0.0, phaseY=0.0, phaseZ=0.0, phaseXR=0.0, phaseYR=0.0, phaseZR=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.supportVessel = None
        self.amplitudeX = amplitudeX
        self.amplitudeY = amplitudeY
        self.amplitudeZ = amplitudeZ
        self.amplitudeXR = amplitudeXR
        self.amplitudeYR = amplitudeYR
        self.amplitudeZR = amplitudeZR
        self.period = period
        self.phaseX = phaseX
        self.phaseY = phaseY
        self.phaseZ = phaseZ
        self.phaseXR = phaseXR
        self.phaseYR = phaseYR
        self.phaseZR = phaseZR
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RegularVesselMotionBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

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
    def supportVessel(self) -> SupportVessel:
        """"""
        return self.__supportVessel

    @supportVessel.setter
    def supportVessel(self, value: SupportVessel):
        """Set supportVessel"""
        self.__supportVessel = value

    @property
    def amplitudeX(self) -> float:
        """Motion amplitude, x-direction"""
        return self.__amplitudeX

    @amplitudeX.setter
    def amplitudeX(self, value: float):
        """Set amplitudeX"""
        self.__amplitudeX = float(value)

    @property
    def amplitudeY(self) -> float:
        """Motion amplitude, y-direction"""
        return self.__amplitudeY

    @amplitudeY.setter
    def amplitudeY(self, value: float):
        """Set amplitudeY"""
        self.__amplitudeY = float(value)

    @property
    def amplitudeZ(self) -> float:
        """Motion amplitude, z-direction"""
        return self.__amplitudeZ

    @amplitudeZ.setter
    def amplitudeZ(self, value: float):
        """Set amplitudeZ"""
        self.__amplitudeZ = float(value)

    @property
    def amplitudeXR(self) -> float:
        """Motion amplitude, x-rotation"""
        return self.__amplitudeXR

    @amplitudeXR.setter
    def amplitudeXR(self, value: float):
        """Set amplitudeXR"""
        self.__amplitudeXR = float(value)

    @property
    def amplitudeYR(self) -> float:
        """Motion amplitude, y-rotation"""
        return self.__amplitudeYR

    @amplitudeYR.setter
    def amplitudeYR(self, value: float):
        """Set amplitudeYR"""
        self.__amplitudeYR = float(value)

    @property
    def amplitudeZR(self) -> float:
        """Motion amplitude, z-rotation"""
        return self.__amplitudeZR

    @amplitudeZR.setter
    def amplitudeZR(self, value: float):
        """Set amplitudeZR"""
        self.__amplitudeZR = float(value)

    @property
    def period(self) -> float:
        """Period of motion"""
        return self.__period

    @period.setter
    def period(self, value: float):
        """Set period"""
        self.__period = float(value)

    @property
    def phaseX(self) -> float:
        """Phase angle, x-motion"""
        return self.__phaseX

    @phaseX.setter
    def phaseX(self, value: float):
        """Set phaseX"""
        self.__phaseX = float(value)

    @property
    def phaseY(self) -> float:
        """Phase angle, y-motion"""
        return self.__phaseY

    @phaseY.setter
    def phaseY(self, value: float):
        """Set phaseY"""
        self.__phaseY = float(value)

    @property
    def phaseZ(self) -> float:
        """Phase angle, z-motion"""
        return self.__phaseZ

    @phaseZ.setter
    def phaseZ(self, value: float):
        """Set phaseZ"""
        self.__phaseZ = float(value)

    @property
    def phaseXR(self) -> float:
        """Phase angle, x-rotation"""
        return self.__phaseXR

    @phaseXR.setter
    def phaseXR(self, value: float):
        """Set phaseXR"""
        self.__phaseXR = float(value)

    @property
    def phaseYR(self) -> float:
        """Phase angle, y-rotation"""
        return self.__phaseYR

    @phaseYR.setter
    def phaseYR(self, value: float):
        """Set phaseYR"""
        self.__phaseYR = float(value)

    @property
    def phaseZR(self) -> float:
        """Phase angle, z-rotation"""
        return self.__phaseZR

    @phaseZR.setter
    def phaseZR(self, value: float):
        """Set phaseZR"""
        self.__phaseZR = float(value)
