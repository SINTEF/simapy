# This an autogenerated file
# 
# Generated with ElongationCharacteristic
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.elongationcharacteristic import ElongationCharacteristicBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.elongationcharacteristictype import ElongationCharacteristicType
from sima.simo.elongationitem import ElongationItem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.fibreropemodel import FibreRopeModel

class ElongationCharacteristic(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    inputType : ElongationCharacteristicType
         Elongation characteristic type. Stress-strain or tension-strain.
    items : List[ElongationItem]
    tensionMax : float
         Historical maximum tension(default 0.0)
    fibreRopeModel : FibreRopeModel
    """

    def __init__(self , description="", inputType=ElongationCharacteristicType.STRESS_STRAIN, tensionMax=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.inputType = inputType
        self.items = list()
        self.tensionMax = tensionMax
        self.fibreRopeModel = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ElongationCharacteristicBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def inputType(self) -> ElongationCharacteristicType:
        """Elongation characteristic type. Stress-strain or tension-strain."""
        return self.__inputType

    @inputType.setter
    def inputType(self, value: ElongationCharacteristicType):
        """Set inputType"""
        self.__inputType = value

    @property
    def items(self) -> List[ElongationItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[ElongationItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value

    @property
    def tensionMax(self) -> float:
        """Historical maximum tension"""
        return self.__tensionMax

    @tensionMax.setter
    def tensionMax(self, value: float):
        """Set tensionMax"""
        self.__tensionMax = float(value)

    @property
    def fibreRopeModel(self) -> FibreRopeModel:
        """"""
        return self.__fibreRopeModel

    @fibreRopeModel.setter
    def fibreRopeModel(self, value: FibreRopeModel):
        """Set fibreRopeModel"""
        self.__fibreRopeModel = value
