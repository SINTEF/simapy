# This an autogenerated file
# 
# Generated with BoundaryChangeGroup
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.boundarychangegroup import BoundaryChangeGroupBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .nodeboundarychangeitem import NodeBoundaryChangeItem

class BoundaryChangeGroup(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    timeChange : float
         Time for boundary change(default 0.0)
    nodeBoundaryChanges : List[NodeBoundaryChangeItem]
    """

    def __init__(self , description="", timeChange=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.timeChange = timeChange
        self.nodeBoundaryChanges = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BoundaryChangeGroupBlueprint()


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
    def timeChange(self) -> float:
        """Time for boundary change"""
        return self.__timeChange

    @timeChange.setter
    def timeChange(self, value: float):
        """Set timeChange"""
        self.__timeChange = float(value)

    @property
    def nodeBoundaryChanges(self) -> List[NodeBoundaryChangeItem]:
        """"""
        return self.__nodeBoundaryChanges

    @nodeBoundaryChanges.setter
    def nodeBoundaryChanges(self, value: List[NodeBoundaryChangeItem]):
        """Set nodeBoundaryChanges"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__nodeBoundaryChanges = value
