# This an autogenerated file
# 
# Generated with ExportBlueprintCommand
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.exportblueprintcommand import ExportBlueprintCommandBlueprint
from typing import Dict
from ..sima import Command
from ..sima import Property
from ..sima import ScriptableValue

class ExportBlueprintCommand(Command):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    parameters : List[Property]
         Additional parameters
    output : str
         Optional output directory. If not specified the blueprints will be imported into the current workspace(default None)
    delete : bool
         Delete the content of the output folder before exporting(default False)
    """

    def __init__(self , description="", delete=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.parameters = list()
        self.output = None
        self.delete = delete
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExportBlueprintCommandBlueprint()


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
    def parameters(self) -> List[Property]:
        """Additional parameters"""
        return self.__parameters

    @parameters.setter
    def parameters(self, value: List[Property]):
        """Set parameters"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__parameters = value

    @property
    def output(self) -> str:
        """Optional output directory. If not specified the blueprints will be imported into the current workspace"""
        return self.__output

    @output.setter
    def output(self, value: str):
        """Set output"""
        self.__output = value

    @property
    def delete(self) -> bool:
        """Delete the content of the output folder before exporting"""
        return self.__delete

    @delete.setter
    def delete(self, value: bool):
        """Set delete"""
        self.__delete = bool(value)
