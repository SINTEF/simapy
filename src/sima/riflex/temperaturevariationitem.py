# This an autogenerated file
# 
# Generated with TemperatureVariationItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.temperaturevariationitem import TemperatureVariationItemBlueprint
from typing import Dict
from sima.riflex.elementreference import ElementReference
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class TemperatureVariationItem(ElementReference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    elementNumber : int
         Local element number on actual segment(default 1)
    allElements : bool
         All elements(default False)
    temperature : float
         Temperature at end of temperature variation(default 0.0)
    """

    def __init__(self , description="", segment=1, allSegments=False, elementNumber=1, allElements=False, temperature=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.elementNumber = elementNumber
        self.allElements = allElements
        self.temperature = temperature
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TemperatureVariationItemBlueprint()


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
    def line(self) -> ARLine:
        """Line"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def segment(self) -> int:
        """Segment on given line"""
        return self.__segment

    @segment.setter
    def segment(self, value: int):
        """Set segment"""
        self.__segment = int(value)

    @property
    def allSegments(self) -> bool:
        """All segments"""
        return self.__allSegments

    @allSegments.setter
    def allSegments(self, value: bool):
        """Set allSegments"""
        self.__allSegments = bool(value)

    @property
    def elementNumber(self) -> int:
        """Local element number on actual segment"""
        return self.__elementNumber

    @elementNumber.setter
    def elementNumber(self, value: int):
        """Set elementNumber"""
        self.__elementNumber = int(value)

    @property
    def allElements(self) -> bool:
        """All elements"""
        return self.__allElements

    @allElements.setter
    def allElements(self, value: bool):
        """Set allElements"""
        self.__allElements = bool(value)

    @property
    def temperature(self) -> float:
        """Temperature at end of temperature variation"""
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        """Set temperature"""
        self.__temperature = float(value)
