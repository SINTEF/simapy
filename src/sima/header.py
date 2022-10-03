# This an autogenerated file
# 
# Generated with Header
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.header import HeaderBlueprint
from typing import Dict
from dmt.entity import Entity
from sima.packageinfo import PackageInfo

class Header(Entity):
    """
    Keyword arguments
    -----------------
    packages : List[PackageInfo]
    """

    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        self.packages = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HeaderBlueprint()


    @property
    def packages(self) -> List[PackageInfo]:
        """"""
        return self.__packages

    @packages.setter
    def packages(self, value: List[PackageInfo]):
        """Set packages"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__packages = value
