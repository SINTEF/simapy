# This an autogenerated file
# 
# Generated with Regular3DBottom
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.regular3dbottom import Regular3DBottomBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class Regular3DBottom(MOAO):
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
    fileName : str
         File with seabed geometry data(default "")
    x : float
         (default 0.0)
    y : float
         (default 0.0)
    zos : float
         Z-coordinate of the origin of the seabed file reference system, in the global reference system(default 0.0)
    angos : float
         Angle between the X-axis of the seabed file reference system and the X-axis of the global reference system(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", fileName:str="", x:float=0.0, y:float=0.0, zos:float=0.0, angos:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__fileName = fileName
        self.__x = x
        self.__y = y
        self.__zos = zos
        self.__angos = angos
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return Regular3DBottomBlueprint()


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
    def fileName(self) -> str:
        """File with seabed geometry data"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = str(value)

    @property
    def x(self) -> float:
        """"""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def zos(self) -> float:
        """Z-coordinate of the origin of the seabed file reference system, in the global reference system"""
        return self.__zos

    @zos.setter
    def zos(self, value: float):
        """Set zos"""
        self.__zos = float(value)

    @property
    def angos(self) -> float:
        """Angle between the X-axis of the seabed file reference system and the X-axis of the global reference system"""
        return self.__angos

    @angos.setter
    def angos(self, value: float):
        """Set angos"""
        self.__angos = float(value)
