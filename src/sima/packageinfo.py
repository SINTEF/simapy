# This an autogenerated file
# 
# Generated with PackageInfo
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.packageinfo import PackageInfoBlueprint
from typing import Dict

class PackageInfo(Entity):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    version : int
         (default 0)
    """

    def __init__(self , name="", description="", version=0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.version = version
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PackageInfoBlueprint()


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
    def version(self) -> int:
        """"""
        return self.__version

    @version.setter
    def version(self, value: int):
        """Set version"""
        self.__version = int(value)
