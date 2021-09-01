# This an autogenerated file
# 
# Generated with ControlParameter
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.controlparameter import ControlParameterBlueprint
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue

class ControlParameter(CustomComponent):
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
    label : str
         (default "")
    tooltip : str
         (default "")
    hlaObjectId : str
         (default "")
    """

    def __init__(self , name:str="", description:str="", _id:str="", label:str="", tooltip:str="", hlaObjectId:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__label = label
        self.__tooltip = tooltip
        self.__hlaObjectId = hlaObjectId
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ControlParameterBlueprint()


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
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = str(value)

    @property
    def hlaObjectId(self) -> str:
        """"""
        return self.__hlaObjectId

    @hlaObjectId.setter
    def hlaObjectId(self, value: str):
        """Set hlaObjectId"""
        self.__hlaObjectId = str(value)
