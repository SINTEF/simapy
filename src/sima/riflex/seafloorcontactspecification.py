# This an autogenerated file
# 
# Generated with SeafloorContactSpecification
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.seafloorcontactspecification import SeafloorContactSpecificationBlueprint
from typing import Dict
from .seafloorcontactlinespecification import SeafloorContactLineSpecification
from sima.sima import MOAO
from sima.sima import ScriptableValue

class SeafloorContactSpecification(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    lineContacts : List[SeafloorContactLineSpecification]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.lineContacts = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SeafloorContactSpecificationBlueprint()


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
    def lineContacts(self) -> List[SeafloorContactLineSpecification]:
        """"""
        return self.__lineContacts

    @lineContacts.setter
    def lineContacts(self, value: List[SeafloorContactLineSpecification]):
        """Set lineContacts"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__lineContacts = value
