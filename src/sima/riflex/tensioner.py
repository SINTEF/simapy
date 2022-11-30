# This an autogenerated file
# 
# Generated with Tensioner
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.tensioner import TensionerBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class Tensioner(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    appliedLoad : float
         Applied load during static analysis(default 0.0)
    maxLoad : float
         Maximum load transmitted from the tensioner(default 0.0)
    minLoad : float
         Minimum load transmitted from the tensioner(default 0.0)
    pipelineDisplacement : float
         Pipeline displacement through the tensioner for a load variation of: max load - min load(default 0.0)
    direction : float
         Direction of the applied load referreing to local X-axis of the element going through the tensioner (+1 = The load will act in local X-axis. -1 = The load will act opposite local X-axis).(default 1.0)
    """

    def __init__(self , description="", appliedLoad=0.0, maxLoad=0.0, minLoad=0.0, pipelineDisplacement=0.0, direction=1.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.appliedLoad = appliedLoad
        self.maxLoad = maxLoad
        self.minLoad = minLoad
        self.pipelineDisplacement = pipelineDisplacement
        self.direction = direction
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TensionerBlueprint()


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
    def appliedLoad(self) -> float:
        """Applied load during static analysis"""
        return self.__appliedLoad

    @appliedLoad.setter
    def appliedLoad(self, value: float):
        """Set appliedLoad"""
        self.__appliedLoad = float(value)

    @property
    def maxLoad(self) -> float:
        """Maximum load transmitted from the tensioner"""
        return self.__maxLoad

    @maxLoad.setter
    def maxLoad(self, value: float):
        """Set maxLoad"""
        self.__maxLoad = float(value)

    @property
    def minLoad(self) -> float:
        """Minimum load transmitted from the tensioner"""
        return self.__minLoad

    @minLoad.setter
    def minLoad(self, value: float):
        """Set minLoad"""
        self.__minLoad = float(value)

    @property
    def pipelineDisplacement(self) -> float:
        """Pipeline displacement through the tensioner for a load variation of: max load - min load"""
        return self.__pipelineDisplacement

    @pipelineDisplacement.setter
    def pipelineDisplacement(self, value: float):
        """Set pipelineDisplacement"""
        self.__pipelineDisplacement = float(value)

    @property
    def direction(self) -> float:
        """Direction of the applied load referreing to local X-axis of the element going through the tensioner (+1 = The load will act in local X-axis. -1 = The load will act opposite local X-axis)."""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)
