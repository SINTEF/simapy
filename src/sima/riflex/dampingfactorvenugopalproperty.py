# This an autogenerated file
# 
# Generated with DampingFactorVenugopalProperty
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dampingfactorvenugopalproperty import DampingFactorVenugopalPropertyBlueprint
from typing import Dict
from sima.riflex.dampingfactorproperty import DampingFactorProperty
from sima.sima.scriptablevalue import ScriptableValue

class DampingFactorVenugopalProperty(DampingFactorProperty):
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
    stillWaterDampingContribution : float
         Factor Venugopal still water damping contribution(default 1.0)
    lowVelocityRegion : float
         Factor Venugopal low velocity region(default 1.0)
    highVelocityRegion : float
         Factor Venugopal high velocity region(default 1.0)
    """

    def __init__(self , description="", _id=None, name=None, stillWaterDampingContribution=1.0, lowVelocityRegion=1.0, highVelocityRegion=1.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.stillWaterDampingContribution = stillWaterDampingContribution
        self.lowVelocityRegion = lowVelocityRegion
        self.highVelocityRegion = highVelocityRegion
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DampingFactorVenugopalPropertyBlueprint()


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
    def stillWaterDampingContribution(self) -> float:
        """Factor Venugopal still water damping contribution"""
        return self.__stillWaterDampingContribution

    @stillWaterDampingContribution.setter
    def stillWaterDampingContribution(self, value: float):
        """Set stillWaterDampingContribution"""
        self.__stillWaterDampingContribution = float(value)

    @property
    def lowVelocityRegion(self) -> float:
        """Factor Venugopal low velocity region"""
        return self.__lowVelocityRegion

    @lowVelocityRegion.setter
    def lowVelocityRegion(self, value: float):
        """Set lowVelocityRegion"""
        self.__lowVelocityRegion = float(value)

    @property
    def highVelocityRegion(self) -> float:
        """Factor Venugopal high velocity region"""
        return self.__highVelocityRegion

    @highVelocityRegion.setter
    def highVelocityRegion(self, value: float):
        """Set highVelocityRegion"""
        self.__highVelocityRegion = float(value)
