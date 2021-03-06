# This an autogenerated file
# 
# Generated with CustomWizard
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.customwizard import CustomWizardBlueprint
from typing import Dict
from sima.custom.customwizardpage import CustomWizardPage
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CustomWizard(MOAO):
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
    title : str
         (default "")
    selectionType : str
         When an object of the given type is selected a popup menu will be enabled,(default "")
    menuLabel : str
         Menu label shown in the popup(default "")
    pages : List[CustomWizardPage]
    inline : bool
         Use inline script or external(default True)
    path : str
         Path to the output file.(default "")
    finishScript : str
         This script will be run when finishing the wizard. Use the variable selection to get hold of the object selected in the navigator(default "")
    """

    def __init__(self , name="", description="", _id="", title="", selectionType="", menuLabel="", inline=True, path="", finishScript="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.title = title
        self.selectionType = selectionType
        self.menuLabel = menuLabel
        self.pages = list()
        self.inline = inline
        self.path = path
        self.finishScript = finishScript
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomWizardBlueprint()


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
    def title(self) -> str:
        """"""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = str(value)

    @property
    def selectionType(self) -> str:
        """When an object of the given type is selected a popup menu will be enabled,"""
        return self.__selectionType

    @selectionType.setter
    def selectionType(self, value: str):
        """Set selectionType"""
        self.__selectionType = str(value)

    @property
    def menuLabel(self) -> str:
        """Menu label shown in the popup"""
        return self.__menuLabel

    @menuLabel.setter
    def menuLabel(self, value: str):
        """Set menuLabel"""
        self.__menuLabel = str(value)

    @property
    def pages(self) -> List[CustomWizardPage]:
        """"""
        return self.__pages

    @pages.setter
    def pages(self, value: List[CustomWizardPage]):
        """Set pages"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__pages = value

    @property
    def inline(self) -> bool:
        """Use inline script or external"""
        return self.__inline

    @inline.setter
    def inline(self, value: bool):
        """Set inline"""
        self.__inline = bool(value)

    @property
    def path(self) -> str:
        """Path to the output file."""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = str(value)

    @property
    def finishScript(self) -> str:
        """This script will be run when finishing the wizard. Use the variable selection to get hold of the object selected in the navigator"""
        return self.__finishScript

    @finishScript.setter
    def finishScript(self, value: str):
        """Set finishScript"""
        self.__finishScript = str(value)
