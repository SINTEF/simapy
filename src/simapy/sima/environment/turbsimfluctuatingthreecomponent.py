# This an autogenerated file
# 
# Generated with TurbSimFluctuatingThreeComponent
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.turbsimfluctuatingthreecomponent import TurbSimFluctuatingThreeComponentBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .wind import Wind

class TurbSimFluctuatingThreeComponent(Wind):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Wind propagation direction(default 0.0)
    numSlices : int
         Buffer size: Number of cross-sectional planes (slices) in memory(default 800)
    windFileName : str
         Path and filename for the binary wind file(default None)
    sumFileName : str
         Path and filename for the summary file from TurbSim(default None)
    """

    def __init__(self , description="", direction=0.0, numSlices=800, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.direction = direction
        self.numSlices = numSlices
        self.windFileName = None
        self.sumFileName = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TurbSimFluctuatingThreeComponentBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def direction(self) -> float:
        """Wind propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def numSlices(self) -> int:
        """Buffer size: Number of cross-sectional planes (slices) in memory"""
        return self.__numSlices

    @numSlices.setter
    def numSlices(self, value: int):
        """Set numSlices"""
        self.__numSlices = int(value)

    @property
    def windFileName(self) -> str:
        """Path and filename for the binary wind file"""
        return self.__windFileName

    @windFileName.setter
    def windFileName(self, value: str):
        """Set windFileName"""
        self.__windFileName = value

    @property
    def sumFileName(self) -> str:
        """Path and filename for the summary file from TurbSim"""
        return self.__sumFileName

    @sumFileName.setter
    def sumFileName(self, value: str):
        """Set sumFileName"""
        self.__sumFileName = value
