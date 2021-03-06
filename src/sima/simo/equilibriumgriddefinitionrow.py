# This an autogenerated file
# 
# Generated with EquilibriumGridDefinitionRow
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.equilibriumgriddefinitionrow import EquilibriumGridDefinitionRowBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class EquilibriumGridDefinitionRow(MOAO):
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
    minimumValue : float
         (default -10.0)
    maximumValue : float
         (default 10.0)
    numberOfValues : int
         (default 11)
    """

    def __init__(self , name="", description="", _id="", minimumValue=-10.0, maximumValue=10.0, numberOfValues=11, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.minimumValue = minimumValue
        self.maximumValue = maximumValue
        self.numberOfValues = numberOfValues
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return EquilibriumGridDefinitionRowBlueprint()


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
    def minimumValue(self) -> float:
        """"""
        return self.__minimumValue

    @minimumValue.setter
    def minimumValue(self, value: float):
        """Set minimumValue"""
        self.__minimumValue = float(value)

    @property
    def maximumValue(self) -> float:
        """"""
        return self.__maximumValue

    @maximumValue.setter
    def maximumValue(self, value: float):
        """Set maximumValue"""
        self.__maximumValue = float(value)

    @property
    def numberOfValues(self) -> int:
        """"""
        return self.__numberOfValues

    @numberOfValues.setter
    def numberOfValues(self, value: int):
        """Set numberOfValues"""
        self.__numberOfValues = int(value)
