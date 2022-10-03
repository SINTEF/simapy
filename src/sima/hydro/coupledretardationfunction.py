# This an autogenerated file
# 
# Generated with CoupledRetardationFunction
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.coupledretardationfunction import CoupledRetardationFunctionBlueprint
from typing import Dict
from sima.hydro.lineardampingmatrix import LinearDampingMatrix
from sima.hydro.retardationelementdata import RetardationElementData
from sima.hydro.retardationfunction import RetardationFunction
from sima.sima.scriptablevalue import ScriptableValue

class CoupledRetardationFunction(RetardationFunction):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    retardationElements : List[RetardationElementData]
    timeDelay : float
         (default 0.0)
    additionalDamping : LinearDampingMatrix
    """

    def __init__(self , _id="", timeDelay=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.retardationElements = list()
        self.timeDelay = timeDelay
        self.additionalDamping = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CoupledRetardationFunctionBlueprint()


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
    def retardationElements(self) -> List[RetardationElementData]:
        """"""
        return self.__retardationElements

    @retardationElements.setter
    def retardationElements(self, value: List[RetardationElementData]):
        """Set retardationElements"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__retardationElements = value

    @property
    def timeDelay(self) -> float:
        """"""
        return self.__timeDelay

    @timeDelay.setter
    def timeDelay(self, value: float):
        """Set timeDelay"""
        self.__timeDelay = float(value)

    @property
    def additionalDamping(self) -> LinearDampingMatrix:
        """"""
        return self.__additionalDamping

    @additionalDamping.setter
    def additionalDamping(self, value: LinearDampingMatrix):
        """Set additionalDamping"""
        self.__additionalDamping = value
