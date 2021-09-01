# This an autogenerated file
# 
# Generated with Tensioner
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.tensioner import TensionerBlueprint
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class Tensioner(NamedObject):
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

    def __init__(self , name:str="", description:str="", _id:str="", appliedLoad:float=0.0, maxLoad:float=0.0, minLoad:float=0.0, pipelineDisplacement:float=0.0, direction:float=1.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__appliedLoad = appliedLoad
        self.__maxLoad = maxLoad
        self.__minLoad = minLoad
        self.__pipelineDisplacement = pipelineDisplacement
        self.__direction = direction
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TensionerBlueprint()


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
