# This an autogenerated file
# 
# Generated with GuidanceSystem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.guidancesystem import GuidanceSystemBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.guidance import Guidance
from sima.simo.headingreference import HeadingReference
from sima.simo.waypoint import Waypoint
from sima.simo.waypointreference import WaypointReference

class GuidanceSystem(MOAO):
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
    guidance : Guidance
    waypointReference : WaypointReference
    headingReference : HeadingReference
    startTime : float
         Start time for guidance system(default 200.0)
    maxAccelerationX : float
         Max. acceleration in local x-direction(default 0.0)
    maxAccelerationY : float
         Max. acceleration in local y-direction(default 0.0)
    waypoints : List[Waypoint]
    """

    def __init__(self , name:str="", description:str="", _id:str="", guidance:Guidance=Guidance.STRAIGHT_LINES, waypointReference:WaypointReference=WaypointReference.LOCAL, headingReference:HeadingReference=HeadingReference.TANGENTIAL, startTime:float=200.0, maxAccelerationX:float=0.0, maxAccelerationY:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__guidance = guidance
        self.__waypointReference = waypointReference
        self.__headingReference = headingReference
        self.__startTime = startTime
        self.__maxAccelerationX = maxAccelerationX
        self.__maxAccelerationY = maxAccelerationY
        self.__waypoints = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GuidanceSystemBlueprint()


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
    def guidance(self) -> Guidance:
        """"""
        return self.__guidance

    @guidance.setter
    def guidance(self, value: Guidance):
        """Set guidance"""
        self.__guidance = value

    @property
    def waypointReference(self) -> WaypointReference:
        """"""
        return self.__waypointReference

    @waypointReference.setter
    def waypointReference(self, value: WaypointReference):
        """Set waypointReference"""
        self.__waypointReference = value

    @property
    def headingReference(self) -> HeadingReference:
        """"""
        return self.__headingReference

    @headingReference.setter
    def headingReference(self, value: HeadingReference):
        """Set headingReference"""
        self.__headingReference = value

    @property
    def startTime(self) -> float:
        """Start time for guidance system"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def maxAccelerationX(self) -> float:
        """Max. acceleration in local x-direction"""
        return self.__maxAccelerationX

    @maxAccelerationX.setter
    def maxAccelerationX(self, value: float):
        """Set maxAccelerationX"""
        self.__maxAccelerationX = float(value)

    @property
    def maxAccelerationY(self) -> float:
        """Max. acceleration in local y-direction"""
        return self.__maxAccelerationY

    @maxAccelerationY.setter
    def maxAccelerationY(self, value: float):
        """Set maxAccelerationY"""
        self.__maxAccelerationY = float(value)

    @property
    def waypoints(self) -> List[Waypoint]:
        """"""
        return self.__waypoints

    @waypoints.setter
    def waypoints(self, value: List[Waypoint]):
        """Set waypoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__waypoints = value
