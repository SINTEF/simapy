# This an autogenerated file
# 
# Generated with ColumnLayoutContainer
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.columnlayoutcontainer import ColumnLayoutContainerBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue

class ColumnLayoutContainer(CustomComponent):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    children : List[CustomComponent]
    """

    def __init__(self , description="", _id=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.children = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ColumnLayoutContainerBlueprint()


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
    def children(self) -> List[CustomComponent]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[CustomComponent]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__children = value
