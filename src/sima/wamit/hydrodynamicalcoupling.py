# This an autogenerated file
# 
# Generated with HydrodynamicalCoupling
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hydrodynamicalcoupling import HydrodynamicalCouplingBlueprint
from typing import Dict
from sima.hydro.coupledradiationdatagroup import CoupledRadiationDataGroup
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.wamit.wamitmodel import WamitModel
    from sima.wamit.wamitbodyresult import WamitBodyResult

class HydrodynamicalCoupling(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    model : WamitModel
    body1 : WamitBodyResult
    body2 : WamitBodyResult
    radiationData : CoupledRadiationDataGroup
    """

    def __init__(self , description="", _id=None, name=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.model = None
        self.body1 = None
        self.body2 = None
        self.radiationData = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HydrodynamicalCouplingBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def model(self) -> WamitModel:
        """"""
        return self.__model

    @model.setter
    def model(self, value: WamitModel):
        """Set model"""
        self.__model = value

    @property
    def body1(self) -> WamitBodyResult:
        """"""
        return self.__body1

    @body1.setter
    def body1(self, value: WamitBodyResult):
        """Set body1"""
        self.__body1 = value

    @property
    def body2(self) -> WamitBodyResult:
        """"""
        return self.__body2

    @body2.setter
    def body2(self, value: WamitBodyResult):
        """Set body2"""
        self.__body2 = value

    @property
    def radiationData(self) -> CoupledRadiationDataGroup:
        """"""
        return self.__radiationData

    @radiationData.setter
    def radiationData(self, value: CoupledRadiationDataGroup):
        """Set radiationData"""
        self.__radiationData = value
