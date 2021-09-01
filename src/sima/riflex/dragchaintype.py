# This an autogenerated file
# 
# Generated with DragChainType
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dragchaintype import DragChainTypeBlueprint
from sima.riflex.nodalcomponenttype import NodalComponentType
from sima.sima.scriptablevalue import ScriptableValue

class DragChainType(NodalComponentType):
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
    length : float
         Drag chain length.(default 0.0)
    unitWeight : float
         Drag chain weight.(default 0.0)
    friction : float
         Chain / seafloor friction coefficient.(default 0.0)
    cableLength : float
         Cable length.(default 0.0)
    cableWeight : float
         Cable weight.(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", length:float=0.0, unitWeight:float=0.0, friction:float=0.0, cableLength:float=0.0, cableWeight:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__length = length
        self.__unitWeight = unitWeight
        self.__friction = friction
        self.__cableLength = cableLength
        self.__cableWeight = cableWeight
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DragChainTypeBlueprint()


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
    def length(self) -> float:
        """Drag chain length."""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def unitWeight(self) -> float:
        """Drag chain weight."""
        return self.__unitWeight

    @unitWeight.setter
    def unitWeight(self, value: float):
        """Set unitWeight"""
        self.__unitWeight = float(value)

    @property
    def friction(self) -> float:
        """Chain / seafloor friction coefficient."""
        return self.__friction

    @friction.setter
    def friction(self, value: float):
        """Set friction"""
        self.__friction = float(value)

    @property
    def cableLength(self) -> float:
        """Cable length."""
        return self.__cableLength

    @cableLength.setter
    def cableLength(self, value: float):
        """Set cableLength"""
        self.__cableLength = float(value)

    @property
    def cableWeight(self) -> float:
        """Cable weight."""
        return self.__cableWeight

    @cableWeight.setter
    def cableWeight(self, value: float):
        """Set cableWeight"""
        self.__cableWeight = float(value)
