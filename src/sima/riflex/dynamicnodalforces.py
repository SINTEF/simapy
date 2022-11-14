# This an autogenerated file
# 
# Generated with DynamicNodalForces
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamicnodalforces import DynamicNodalForcesBlueprint
from typing import Dict
from sima.riflex.dynamicnodalforceitem import DynamicNodalForceItem
from sima.riflex.forcespecificationtype import ForceSpecificationType
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class DynamicNodalForces(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    _type : ForceSpecificationType
         Type of force specification
    fileName : str
         File name for time series of force components\n\nNTDFO: : Number of time instants (given once) \nMDCOMP TIMDFO: Number of load components and \ntime instant for the given loads\nRLMAG:  Magnitude of load component (MDCOMP lines)\n\nThe block {MDCOMP TIMDFO RLMAG} must be given for \neach time instant. \n(default None)
    items : List[DynamicNodalForceItem]
    """

    def __init__(self , description="", _id=None, _type=ForceSpecificationType.SIMPLE_EXPRESSION, fileName=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self._type = _type
        self.fileName = fileName
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicNodalForcesBlueprint()


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
    def _type(self) -> ForceSpecificationType:
        """Type of force specification"""
        return self.___type

    @_type.setter
    def _type(self, value: ForceSpecificationType):
        """Set _type"""
        self.___type = value

    @property
    def fileName(self) -> str:
        """File name for time series of force components

NTDFO: : Number of time instants (given once) 
MDCOMP TIMDFO: Number of load components and 
time instant for the given loads
RLMAG:  Magnitude of load component (MDCOMP lines)

The block {MDCOMP TIMDFO RLMAG} must be given for 
each time instant. 
"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = str(value)

    @property
    def items(self) -> List[DynamicNodalForceItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[DynamicNodalForceItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value
