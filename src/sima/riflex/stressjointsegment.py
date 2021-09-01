# This an autogenerated file
# 
# Generated with StressJointSegment
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.stressjointsegment import StressJointSegmentBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class StressJointSegment(MOAO):
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
         Length of the segment.(default 0.0)
    numElements : int
         Number of elements(default 10)
    extDiameterEnd2 : float
         External diameter at second end of actual segment.(default 0.0)
    wallThicknessEnd2 : float
         Wall thickness at second end.(default 0.0)
    elasticModulus : float
         Elastic modulus.(default 0.0)
    materialDensity : float
         Density of pipe material.(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", length:float=0.0, numElements:int=10, extDiameterEnd2:float=0.0, wallThicknessEnd2:float=0.0, elasticModulus:float=0.0, materialDensity:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__length = length
        self.__numElements = numElements
        self.__extDiameterEnd2 = extDiameterEnd2
        self.__wallThicknessEnd2 = wallThicknessEnd2
        self.__elasticModulus = elasticModulus
        self.__materialDensity = materialDensity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StressJointSegmentBlueprint()


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
        """Length of the segment."""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def numElements(self) -> int:
        """Number of elements"""
        return self.__numElements

    @numElements.setter
    def numElements(self, value: int):
        """Set numElements"""
        self.__numElements = int(value)

    @property
    def extDiameterEnd2(self) -> float:
        """External diameter at second end of actual segment."""
        return self.__extDiameterEnd2

    @extDiameterEnd2.setter
    def extDiameterEnd2(self, value: float):
        """Set extDiameterEnd2"""
        self.__extDiameterEnd2 = float(value)

    @property
    def wallThicknessEnd2(self) -> float:
        """Wall thickness at second end."""
        return self.__wallThicknessEnd2

    @wallThicknessEnd2.setter
    def wallThicknessEnd2(self, value: float):
        """Set wallThicknessEnd2"""
        self.__wallThicknessEnd2 = float(value)

    @property
    def elasticModulus(self) -> float:
        """Elastic modulus."""
        return self.__elasticModulus

    @elasticModulus.setter
    def elasticModulus(self, value: float):
        """Set elasticModulus"""
        self.__elasticModulus = float(value)

    @property
    def materialDensity(self) -> float:
        """Density of pipe material."""
        return self.__materialDensity

    @materialDensity.setter
    def materialDensity(self, value: float):
        """Set materialDensity"""
        self.__materialDensity = float(value)
