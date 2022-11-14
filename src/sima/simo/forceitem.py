# This an autogenerated file
# 
# Generated with ForceItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.forceitem import ForceItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ForceItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    distance : float
         i'th vertical position in the force vs. vertical position table, (L) For NFZ=1, ZBUOY is dummy, but must be given(default 0.0)
    force : float
         Corresponding vertical force, positive upwards, (F)(default 0.0)
    """

    def __init__(self , description="", _id=None, distance=0.0, force=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.distance = distance
        self.force = force
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ForceItemBlueprint()


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
    def distance(self) -> float:
        """i'th vertical position in the force vs. vertical position table, (L) For NFZ=1, ZBUOY is dummy, but must be given"""
        return self.__distance

    @distance.setter
    def distance(self, value: float):
        """Set distance"""
        self.__distance = float(value)

    @property
    def force(self) -> float:
        """Corresponding vertical force, positive upwards, (F)"""
        return self.__force

    @force.setter
    def force(self, value: float):
        """Set force"""
        self.__force = float(value)
