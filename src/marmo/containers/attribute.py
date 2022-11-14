# This an autogenerated file
# Represents a key/value entry
# Generated with Attribute
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.attribute import AttributeBlueprint
from typing import Dict
from dmt.namedentity import NamedEntity

class Attribute(NamedEntity):
    """
    Represents a key/value entry
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         (default None)
    value : str
         (default None)
    """

    def __init__(self , description="", name=None, value=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = name
        self.value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AttributeBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def value(self) -> str:
        """"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = str(value)
