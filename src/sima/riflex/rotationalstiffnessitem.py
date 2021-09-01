# This an autogenerated file
# 
# Generated with RotationalStiffnessItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.rotationalstiffnessitem import RotationalStiffnessItemBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class RotationalStiffnessItem(MOAO):
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
    moment : float
         Moment corresponding to rotational angle(default 0.0)
    angle : float
         Rotational angle(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", moment:float=0.0, angle:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__moment = moment
        self.__angle = angle
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RotationalStiffnessItemBlueprint()


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
