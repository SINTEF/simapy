# This an autogenerated file
# 
# Generated with SIMAScript
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simascript import SIMAScriptBlueprint
from typing import Dict
from .namedobject import NamedObject
from .scriptablevalue import ScriptableValue
from .simascriptcontext import SIMAScriptContext
from .simascripttrigger import SIMAScriptTrigger

class SIMAScript(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    script : str
         (default None)
    contextItems : List[SIMAScriptContext]
    triggers : List[SIMAScriptTrigger]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.script = None
        self.contextItems = list()
        self.triggers = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMAScriptBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def script(self) -> str:
        """"""
        return self.__script

    @script.setter
    def script(self, value: str):
        """Set script"""
        self.__script = value

    @property
    def contextItems(self) -> List[SIMAScriptContext]:
        """"""
        return self.__contextItems

    @contextItems.setter
    def contextItems(self, value: List[SIMAScriptContext]):
        """Set contextItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__contextItems = value

    @property
    def triggers(self) -> List[SIMAScriptTrigger]:
        """"""
        return self.__triggers

    @triggers.setter
    def triggers(self, value: List[SIMAScriptTrigger]):
        """Set triggers"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__triggers = value
