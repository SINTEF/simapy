# This an autogenerated file
# 
# Generated with HorizontalAxisYawController
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.horizontalaxisyawcontroller import HorizontalAxisYawControllerBlueprint
from sima.sima.scriptablevalue import ScriptableValue
from sima.windturbine.yawcontroller import YawController
from sima.windturbine.yawcontrollertype import YawControllerType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class HorizontalAxisYawController(YawController):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    yawControllerType : YawControllerType
    timeStep : float
         (default 0.0)
    setPoint : float
         Desired yaw misalignment(default 0.0)
    yawRate : float
         (default 0.0)
    errorThreshold : float
         Yaw misalignment integrated error threshold(default 0.0)
    fastLowPassFilterPeriod : float
         Filter period for yaw misalignment signal. Used for determining if 'error threshold' has been passed(default 0.0)
    slowLowPassFilterPeriod : float
         Filter period for yaw misalignment signal. Used to determine end time for yawing back to set point(default 0.0)
    referenceLine : ARLine
         Line where end 2 is the fixed reference for the applied yaw angle
    yawLine : ARLine
         Line where yaw angle is applied in end 1
    """

    def __init__(self , name:str="", description:str="", _id:str="", yawControllerType:YawControllerType=YawControllerType.NONE, timeStep:float=0.0, setPoint:float=0.0, yawRate:float=0.0, errorThreshold:float=0.0, fastLowPassFilterPeriod:float=0.0, slowLowPassFilterPeriod:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__yawControllerType = yawControllerType
        self.__timeStep = timeStep
        self.__setPoint = setPoint
        self.__yawRate = yawRate
        self.__errorThreshold = errorThreshold
        self.__fastLowPassFilterPeriod = fastLowPassFilterPeriod
        self.__slowLowPassFilterPeriod = slowLowPassFilterPeriod
        self.__referenceLine = None
        self.__yawLine = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HorizontalAxisYawControllerBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def yawControllerType(self) -> YawControllerType:
        """"""
        return self.__yawControllerType

    @yawControllerType.setter
    def yawControllerType(self, value: YawControllerType):
        """Set yawControllerType"""
        self.__yawControllerType = value

    @property
    def timeStep(self) -> float:
        """"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def setPoint(self) -> float:
        """Desired yaw misalignment"""
        return self.__setPoint

    @setPoint.setter
    def setPoint(self, value: float):
        """Set setPoint"""
        self.__setPoint = float(value)

    @property
    def yawRate(self) -> float:
        """"""
        return self.__yawRate

    @yawRate.setter
    def yawRate(self, value: float):
        """Set yawRate"""
        self.__yawRate = float(value)

    @property
    def errorThreshold(self) -> float:
        """Yaw misalignment integrated error threshold"""
        return self.__errorThreshold

    @errorThreshold.setter
    def errorThreshold(self, value: float):
        """Set errorThreshold"""
        self.__errorThreshold = float(value)

    @property
    def fastLowPassFilterPeriod(self) -> float:
        """Filter period for yaw misalignment signal. Used for determining if 'error threshold' has been passed"""
        return self.__fastLowPassFilterPeriod

    @fastLowPassFilterPeriod.setter
    def fastLowPassFilterPeriod(self, value: float):
        """Set fastLowPassFilterPeriod"""
        self.__fastLowPassFilterPeriod = float(value)

    @property
    def slowLowPassFilterPeriod(self) -> float:
        """Filter period for yaw misalignment signal. Used to determine end time for yawing back to set point"""
        return self.__slowLowPassFilterPeriod

    @slowLowPassFilterPeriod.setter
    def slowLowPassFilterPeriod(self, value: float):
        """Set slowLowPassFilterPeriod"""
        self.__slowLowPassFilterPeriod = float(value)

    @property
    def referenceLine(self) -> ARLine:
        """Line where end 2 is the fixed reference for the applied yaw angle"""
        return self.__referenceLine

    @referenceLine.setter
    def referenceLine(self, value: ARLine):
        """Set referenceLine"""
        self.__referenceLine = value

    @property
    def yawLine(self) -> ARLine:
        """Line where yaw angle is applied in end 1"""
        return self.__yawLine

    @yawLine.setter
    def yawLine(self, value: ARLine):
        """Set yawLine"""
        self.__yawLine = value
