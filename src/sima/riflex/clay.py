# This an autogenerated file
# 
# Generated with Clay
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.clay import ClayBlueprint
from typing import Dict
from sima.riflex.soil import Soil
from sima.riflex.soildampingitem import SoilDampingItem
from sima.sima.scriptablevalue import ScriptableValue

class Clay(Soil):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    strainVelocityExponent : float
         Strain velocity exponent for damping model(default 1.0)
    calculateDamping : bool
         Calculate damping coefficients(default False)
    dampingItems : List[SoilDampingItem]
    upperWeight : float
         (default 0.0)
    lowerWeight : float
         (default 0.0)
    displacement : float
         Target displacement for generating equivalent damping coefficient(default 0.0)
    frequency : float
         Target frequency for generating equivalent damping coefficient(default 0.0)
    initialShearModulus : float
         Initial shear modulus of soil(default 0.0)
    upperShearStrength : float
         Undrained shear strength(default 0.0)
    upperJConstant : float
         Dimensionless constant(default 0.0)
    upperStrain : float
         Strain at one-half the maximum stress in undrained compression(default 0.0)
    lowerShearStrength : float
         Undrained shear strength(default 0.0)
    lowerJConstant : float
         Dimensionless constant(default 0.0)
    lowerStrain : float
         Strain at one-half the maximum stress in undrained compression(default 0.0)
    """

    def __init__(self , _id="", name="", strainVelocityExponent=1.0, calculateDamping=False, upperWeight=0.0, lowerWeight=0.0, displacement=0.0, frequency=0.0, initialShearModulus=0.0, upperShearStrength=0.0, upperJConstant=0.0, upperStrain=0.0, lowerShearStrength=0.0, lowerJConstant=0.0, lowerStrain=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.strainVelocityExponent = strainVelocityExponent
        self.calculateDamping = calculateDamping
        self.dampingItems = list()
        self.upperWeight = upperWeight
        self.lowerWeight = lowerWeight
        self.displacement = displacement
        self.frequency = frequency
        self.initialShearModulus = initialShearModulus
        self.upperShearStrength = upperShearStrength
        self.upperJConstant = upperJConstant
        self.upperStrain = upperStrain
        self.lowerShearStrength = lowerShearStrength
        self.lowerJConstant = lowerJConstant
        self.lowerStrain = lowerStrain
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ClayBlueprint()


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
    def strainVelocityExponent(self) -> float:
        """Strain velocity exponent for damping model"""
        return self.__strainVelocityExponent

    @strainVelocityExponent.setter
    def strainVelocityExponent(self, value: float):
        """Set strainVelocityExponent"""
        self.__strainVelocityExponent = float(value)

    @property
    def calculateDamping(self) -> bool:
        """Calculate damping coefficients"""
        return self.__calculateDamping

    @calculateDamping.setter
    def calculateDamping(self, value: bool):
        """Set calculateDamping"""
        self.__calculateDamping = bool(value)

    @property
    def dampingItems(self) -> List[SoilDampingItem]:
        """"""
        return self.__dampingItems

    @dampingItems.setter
    def dampingItems(self, value: List[SoilDampingItem]):
        """Set dampingItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__dampingItems = value

    @property
    def upperWeight(self) -> float:
        """"""
        return self.__upperWeight

    @upperWeight.setter
    def upperWeight(self, value: float):
        """Set upperWeight"""
        self.__upperWeight = float(value)

    @property
    def lowerWeight(self) -> float:
        """"""
        return self.__lowerWeight

    @lowerWeight.setter
    def lowerWeight(self, value: float):
        """Set lowerWeight"""
        self.__lowerWeight = float(value)

    @property
    def displacement(self) -> float:
        """Target displacement for generating equivalent damping coefficient"""
        return self.__displacement

    @displacement.setter
    def displacement(self, value: float):
        """Set displacement"""
        self.__displacement = float(value)

    @property
    def frequency(self) -> float:
        """Target frequency for generating equivalent damping coefficient"""
        return self.__frequency

    @frequency.setter
    def frequency(self, value: float):
        """Set frequency"""
        self.__frequency = float(value)

    @property
    def initialShearModulus(self) -> float:
        """Initial shear modulus of soil"""
        return self.__initialShearModulus

    @initialShearModulus.setter
    def initialShearModulus(self, value: float):
        """Set initialShearModulus"""
        self.__initialShearModulus = float(value)

    @property
    def upperShearStrength(self) -> float:
        """Undrained shear strength"""
        return self.__upperShearStrength

    @upperShearStrength.setter
    def upperShearStrength(self, value: float):
        """Set upperShearStrength"""
        self.__upperShearStrength = float(value)

    @property
    def upperJConstant(self) -> float:
        """Dimensionless constant"""
        return self.__upperJConstant

    @upperJConstant.setter
    def upperJConstant(self, value: float):
        """Set upperJConstant"""
        self.__upperJConstant = float(value)

    @property
    def upperStrain(self) -> float:
        """Strain at one-half the maximum stress in undrained compression"""
        return self.__upperStrain

    @upperStrain.setter
    def upperStrain(self, value: float):
        """Set upperStrain"""
        self.__upperStrain = float(value)

    @property
    def lowerShearStrength(self) -> float:
        """Undrained shear strength"""
        return self.__lowerShearStrength

    @lowerShearStrength.setter
    def lowerShearStrength(self, value: float):
        """Set lowerShearStrength"""
        self.__lowerShearStrength = float(value)

    @property
    def lowerJConstant(self) -> float:
        """Dimensionless constant"""
        return self.__lowerJConstant

    @lowerJConstant.setter
    def lowerJConstant(self, value: float):
        """Set lowerJConstant"""
        self.__lowerJConstant = float(value)

    @property
    def lowerStrain(self) -> float:
        """Strain at one-half the maximum stress in undrained compression"""
        return self.__lowerStrain

    @lowerStrain.setter
    def lowerStrain(self, value: float):
        """Set lowerStrain"""
        self.__lowerStrain = float(value)
