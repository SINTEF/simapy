# This an autogenerated file
# 
# Generated with MainRiserLine
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.mainriserline import MainRiserLineBlueprint
from typing import Dict
from sima.riflex.arlineitem import ARLineItem
from sima.riflex.end import End
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class MainRiserLine(NamedObject):
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
    riserLines : List[ARLineItem]
    flowRho : float
         Density of contents(default 0.0)
    flowPressure : float
         Pressure at specified end(default 0.0)
    flowPressureEnd : End
         End for which flow data is specified.
    flowPressureDrop : float
         Pressure drop(default 0.0)
    """

    def __init__(self , name="", description="", _id="", flowRho=0.0, flowPressure=0.0, flowPressureEnd=End.ONE, flowPressureDrop=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.riserLines = list()
        self.flowRho = flowRho
        self.flowPressure = flowPressure
        self.flowPressureEnd = flowPressureEnd
        self.flowPressureDrop = flowPressureDrop
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MainRiserLineBlueprint()


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
    def riserLines(self) -> List[ARLineItem]:
        """"""
        return self.__riserLines

    @riserLines.setter
    def riserLines(self, value: List[ARLineItem]):
        """Set riserLines"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__riserLines = value

    @property
    def flowRho(self) -> float:
        """Density of contents"""
        return self.__flowRho

    @flowRho.setter
    def flowRho(self, value: float):
        """Set flowRho"""
        self.__flowRho = float(value)

    @property
    def flowPressure(self) -> float:
        """Pressure at specified end"""
        return self.__flowPressure

    @flowPressure.setter
    def flowPressure(self, value: float):
        """Set flowPressure"""
        self.__flowPressure = float(value)

    @property
    def flowPressureEnd(self) -> End:
        """End for which flow data is specified."""
        return self.__flowPressureEnd

    @flowPressureEnd.setter
    def flowPressureEnd(self, value: End):
        """Set flowPressureEnd"""
        self.__flowPressureEnd = value

    @property
    def flowPressureDrop(self) -> float:
        """Pressure drop"""
        return self.__flowPressureDrop

    @flowPressureDrop.setter
    def flowPressureDrop(self, value: float):
        """Set flowPressureDrop"""
        self.__flowPressureDrop = float(value)
