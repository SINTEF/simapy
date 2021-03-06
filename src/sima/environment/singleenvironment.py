# This an autogenerated file
# 
# Generated with SingleEnvironment
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.singleenvironment import SingleEnvironmentBlueprint
from typing import Dict
from sima.environment.current import Current
from sima.environment.environment import Environment
from sima.environment.wave import Wave
from sima.environment.wind import Wind
from sima.sima.scriptablevalue import ScriptableValue

class SingleEnvironment(Environment):
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
    wave : Wave
    swell : Wave
    wind : Wind
    current : Current
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.wave = None
        self.swell = None
        self.wind = None
        self.current = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SingleEnvironmentBlueprint()


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
    def wave(self) -> Wave:
        """"""
        return self.__wave

    @wave.setter
    def wave(self, value: Wave):
        """Set wave"""
        self.__wave = value

    @property
    def swell(self) -> Wave:
        """"""
        return self.__swell

    @swell.setter
    def swell(self, value: Wave):
        """Set swell"""
        self.__swell = value

    @property
    def wind(self) -> Wind:
        """"""
        return self.__wind

    @wind.setter
    def wind(self, value: Wind):
        """Set wind"""
        self.__wind = value

    @property
    def current(self) -> Current:
        """"""
        return self.__current

    @current.setter
    def current(self, value: Current):
        """Set current"""
        self.__current = value
