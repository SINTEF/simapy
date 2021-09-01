# This an autogenerated file
# 
# Generated with ExternalWrappingType
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.externalwrappingtype import ExternalWrappingTypeBlueprint
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class ExternalWrappingType(NamedObject):
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
    mass : float
         Mass per unit length(default 0.0)
    buoyancy : float
         Buoyancy volume/length(default 0.0)
    gyrationRadius : float
         Radius of gyration around x-axis(default 0.0)
    coveredFraction : float
         Fraction of the segment that is covered. 0 < FRAC < 1.0.(default 0.0)
    wrappingItemLength : float
         Length of wrapping item. Only used for graphics.(default 1.0)
    tangentialDrag : float
         Drag force coefficient in tangential direction(default 0.0)
    normalDrag : float
         Drag force coefficient in normal direction(default 0.0)
    tangentialAddedMass : float
         Added mass per length in tangential direction(default 0.0)
    normalAddedMass : float
         Added mass per length in normal direction(default 0.0)
    tangentialLinearDrag : float
         Linear drag force coefficients in tangential direction(default 0.0)
    normalLinearDrag : float
         Linear drag force coefficients in tangential direction(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", mass:float=0.0, buoyancy:float=0.0, gyrationRadius:float=0.0, coveredFraction:float=0.0, wrappingItemLength:float=1.0, tangentialDrag:float=0.0, normalDrag:float=0.0, tangentialAddedMass:float=0.0, normalAddedMass:float=0.0, tangentialLinearDrag:float=0.0, normalLinearDrag:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__mass = mass
        self.__buoyancy = buoyancy
        self.__gyrationRadius = gyrationRadius
        self.__coveredFraction = coveredFraction
        self.__wrappingItemLength = wrappingItemLength
        self.__tangentialDrag = tangentialDrag
        self.__normalDrag = normalDrag
        self.__tangentialAddedMass = tangentialAddedMass
        self.__normalAddedMass = normalAddedMass
        self.__tangentialLinearDrag = tangentialLinearDrag
        self.__normalLinearDrag = normalLinearDrag
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExternalWrappingTypeBlueprint()


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
    def mass(self) -> float:
        """Mass per unit length"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def buoyancy(self) -> float:
        """Buoyancy volume/length"""
        return self.__buoyancy

    @buoyancy.setter
    def buoyancy(self, value: float):
        """Set buoyancy"""
        self.__buoyancy = float(value)

    @property
    def gyrationRadius(self) -> float:
        """Radius of gyration around x-axis"""
        return self.__gyrationRadius

    @gyrationRadius.setter
    def gyrationRadius(self, value: float):
        """Set gyrationRadius"""
        self.__gyrationRadius = float(value)

    @property
    def coveredFraction(self) -> float:
        """Fraction of the segment that is covered. 0 < FRAC < 1.0."""
        return self.__coveredFraction

    @coveredFraction.setter
    def coveredFraction(self, value: float):
        """Set coveredFraction"""
        self.__coveredFraction = float(value)

    @property
    def wrappingItemLength(self) -> float:
        """Length of wrapping item. Only used for graphics."""
        return self.__wrappingItemLength

    @wrappingItemLength.setter
    def wrappingItemLength(self, value: float):
        """Set wrappingItemLength"""
        self.__wrappingItemLength = float(value)

    @property
    def tangentialDrag(self) -> float:
        """Drag force coefficient in tangential direction"""
        return self.__tangentialDrag

    @tangentialDrag.setter
    def tangentialDrag(self, value: float):
        """Set tangentialDrag"""
        self.__tangentialDrag = float(value)

    @property
    def normalDrag(self) -> float:
        """Drag force coefficient in normal direction"""
        return self.__normalDrag

    @normalDrag.setter
    def normalDrag(self, value: float):
        """Set normalDrag"""
        self.__normalDrag = float(value)

    @property
    def tangentialAddedMass(self) -> float:
        """Added mass per length in tangential direction"""
        return self.__tangentialAddedMass

    @tangentialAddedMass.setter
    def tangentialAddedMass(self, value: float):
        """Set tangentialAddedMass"""
        self.__tangentialAddedMass = float(value)

    @property
    def normalAddedMass(self) -> float:
        """Added mass per length in normal direction"""
        return self.__normalAddedMass

    @normalAddedMass.setter
    def normalAddedMass(self, value: float):
        """Set normalAddedMass"""
        self.__normalAddedMass = float(value)

    @property
    def tangentialLinearDrag(self) -> float:
        """Linear drag force coefficients in tangential direction"""
        return self.__tangentialLinearDrag

    @tangentialLinearDrag.setter
    def tangentialLinearDrag(self, value: float):
        """Set tangentialLinearDrag"""
        self.__tangentialLinearDrag = float(value)

    @property
    def normalLinearDrag(self) -> float:
        """Linear drag force coefficients in tangential direction"""
        return self.__normalLinearDrag

    @normalLinearDrag.setter
    def normalLinearDrag(self, value: float):
        """Set normalLinearDrag"""
        self.__normalLinearDrag = float(value)
