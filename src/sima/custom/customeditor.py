# This an autogenerated file
# 
# Generated with CustomEditor
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.customeditor import CustomEditorBlueprint
from typing import Dict
from .customcomponent import CustomComponent
from sima.sima import MOAO
from sima.sima import ScriptableValue

class CustomEditor(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    children : List[CustomComponent]
    title : str
         (default None)
    editMode : bool
         When checked the custom editor will always be opened in edit mode and child elements will be added to the navigator (default False)
    showDescription : bool
         (default False)
    """

    def __init__(self , description="", editMode=False, showDescription=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.children = list()
        self.title = None
        self.editMode = editMode
        self.showDescription = showDescription
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomEditorBlueprint()


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
    def children(self) -> List[CustomComponent]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[CustomComponent]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__children = value

    @property
    def title(self) -> str:
        """"""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = value

    @property
    def editMode(self) -> bool:
        """When checked the custom editor will always be opened in edit mode and child elements will be added to the navigator """
        return self.__editMode

    @editMode.setter
    def editMode(self, value: bool):
        """Set editMode"""
        self.__editMode = bool(value)

    @property
    def showDescription(self) -> bool:
        """"""
        return self.__showDescription

    @showDescription.setter
    def showDescription(self, value: bool):
        """Set showDescription"""
        self.__showDescription = bool(value)