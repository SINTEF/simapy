# This an autogenerated file
# 
# Generated with ConstraintItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.constraintitem import ConstraintItemBlueprint
from typing import Dict
from sima.post.constrainttype import ConstraintType
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ConstraintItem(MOAO):
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
    path : str
         (default "")
    _type : ConstraintType
    value : float
         (default 0.0)
    """

    def __init__(self , name="", description="", _id="", path="", _type=ConstraintType.LE, value=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.path = path
        self._type = _type
        self.value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ConstraintItemBlueprint()


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
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = str(value)

    @property
    def _type(self) -> ConstraintType:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: ConstraintType):
        """Set _type"""
        self.___type = value

    @property
    def value(self) -> float:
        """"""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Set value"""
        self.__value = float(value)
