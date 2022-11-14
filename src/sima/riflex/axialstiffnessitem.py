# This an autogenerated file
# 
# Generated with AxialStiffnessItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.axialstiffnessitem import AxialStiffnessItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class AxialStiffnessItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    axialForce : float
         Axial force corresponding to relative elongation.(default 0.0)
    relativeElongation : float
         Relative elongation(default 0.0)
    """

    def __init__(self , description="", _id=None, axialForce=0.0, relativeElongation=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.axialForce = axialForce
        self.relativeElongation = relativeElongation
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AxialStiffnessItemBlueprint()


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
    def axialForce(self) -> float:
        """Axial force corresponding to relative elongation."""
        return self.__axialForce

    @axialForce.setter
    def axialForce(self, value: float):
        """Set axialForce"""
        self.__axialForce = float(value)

    @property
    def relativeElongation(self) -> float:
        """Relative elongation"""
        return self.__relativeElongation

    @relativeElongation.setter
    def relativeElongation(self, value: float):
        """Set relativeElongation"""
        self.__relativeElongation = float(value)
