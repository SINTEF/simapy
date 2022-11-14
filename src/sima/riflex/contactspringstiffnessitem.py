# This an autogenerated file
# 
# Generated with ContactSpringStiffnessItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.contactspringstiffnessitem import ContactSpringStiffnessItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ContactSpringStiffnessItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    force : float
         Pressure force per unit length(default 0.0)
    compression : float
         Spring compression(default 0.0)
    """

    def __init__(self , description="", _id=None, force=0.0, compression=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.force = force
        self.compression = compression
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ContactSpringStiffnessItemBlueprint()


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
    def force(self) -> float:
        """Pressure force per unit length"""
        return self.__force

    @force.setter
    def force(self, value: float):
        """Set force"""
        self.__force = float(value)

    @property
    def compression(self) -> float:
        """Spring compression"""
        return self.__compression

    @compression.setter
    def compression(self, value: float):
        """Set compression"""
        self.__compression = float(value)
