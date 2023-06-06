# This an autogenerated file
# 
# Generated with FileOutputSlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fileoutputslot import FileOutputSlotBlueprint
from typing import Dict
from ..post import OutputSlot
from ..sima import ScriptableValue

class FileOutputSlot(OutputSlot):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    filename : str
         Name of file to be imported(default None)
    pathOnly : bool
         Import the path to the specified file and not the content(default False)
    """

    def __init__(self , description="", pathOnly=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.filename = None
        self.pathOnly = pathOnly
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FileOutputSlotBlueprint()


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
    def filename(self) -> str:
        """Name of file to be imported"""
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        """Set filename"""
        self.__filename = value

    @property
    def pathOnly(self) -> bool:
        """Import the path to the specified file and not the content"""
        return self.__pathOnly

    @pathOnly.setter
    def pathOnly(self, value: bool):
        """Set pathOnly"""
        self.__pathOnly = bool(value)
