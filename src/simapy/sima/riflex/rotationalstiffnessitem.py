# This an autogenerated file
# 
# Generated with RotationalStiffnessItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.rotationalstiffnessitem import RotationalStiffnessItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class RotationalStiffnessItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    moment : float
         Moment corresponding to rotational angle(default 0.0)
    angle : float
         Rotational angle(default 0.0)
    """

    def __init__(self , description="", moment=0.0, angle=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.moment = moment
        self.angle = angle
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RotationalStiffnessItemBlueprint()


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
    def moment(self) -> float:
        """Moment corresponding to rotational angle"""
        return self.__moment

    @moment.setter
    def moment(self, value: float):
        """Set moment"""
        self.__moment = float(value)

    @property
    def angle(self) -> float:
        """Rotational angle"""
        return self.__angle

    @angle.setter
    def angle(self, value: float):
        """Set angle"""
        self.__angle = float(value)
