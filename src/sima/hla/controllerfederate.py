# This an autogenerated file
# 
# Generated with ControllerFederate
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.controllerfederate import ControllerFederateBlueprint
from typing import Dict
from sima.hla.hlacontrolconfiguration import HLAControlConfiguration
from sima.hla.hlafederate import HLAFederate
from sima.hla.hlawinchgroup import HLAWinchGroup
from sima.sima.scriptablevalue import ScriptableValue

class ControllerFederate(HLAFederate):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    timeStep : float
         (default 0.0)
    allHLAControlConfigurations : List[HLAControlConfiguration]
    winchGroups : List[HLAWinchGroup]
    """

    def __init__(self , description="", timeStep=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.timeStep = timeStep
        self.allHLAControlConfigurations = list()
        self.winchGroups = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ControllerFederateBlueprint()


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
    def timeStep(self) -> float:
        """"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def allHLAControlConfigurations(self) -> List[HLAControlConfiguration]:
        """"""
        return self.__allHLAControlConfigurations

    @allHLAControlConfigurations.setter
    def allHLAControlConfigurations(self, value: List[HLAControlConfiguration]):
        """Set allHLAControlConfigurations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__allHLAControlConfigurations = value

    @property
    def winchGroups(self) -> List[HLAWinchGroup]:
        """"""
        return self.__winchGroups

    @winchGroups.setter
    def winchGroups(self, value: List[HLAWinchGroup]):
        """Set winchGroups"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__winchGroups = value
