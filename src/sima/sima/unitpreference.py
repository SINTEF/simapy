# This an autogenerated file
# 
# Generated with UnitPreference
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.unitpreference import UnitPreferenceBlueprint
from typing import Dict
from sima.sima.forceunit import ForceUnit
from sima.sima.frequency import Frequency
from sima.sima.lengthunit import LengthUnit
from sima.sima.massunit import MassUnit
from sima.sima.powerunit import PowerUnit
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simapreference import SIMAPreference

class UnitPreference(SIMAPreference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    frequency : Frequency
    forceUnit : ForceUnit
    massUnit : MassUnit
    lengthUnit : LengthUnit
    powerUnit : PowerUnit
    """

    def __init__(self , description="", frequency=Frequency.PERIOD, forceUnit=ForceUnit.NEWTON, massUnit=MassUnit.KILOGRAM, lengthUnit=LengthUnit.METER, powerUnit=PowerUnit.WATT, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.frequency = frequency
        self.forceUnit = forceUnit
        self.massUnit = massUnit
        self.lengthUnit = lengthUnit
        self.powerUnit = powerUnit
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return UnitPreferenceBlueprint()


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
    def frequency(self) -> Frequency:
        """"""
        return self.__frequency

    @frequency.setter
    def frequency(self, value: Frequency):
        """Set frequency"""
        self.__frequency = value

    @property
    def forceUnit(self) -> ForceUnit:
        """"""
        return self.__forceUnit

    @forceUnit.setter
    def forceUnit(self, value: ForceUnit):
        """Set forceUnit"""
        self.__forceUnit = value

    @property
    def massUnit(self) -> MassUnit:
        """"""
        return self.__massUnit

    @massUnit.setter
    def massUnit(self, value: MassUnit):
        """Set massUnit"""
        self.__massUnit = value

    @property
    def lengthUnit(self) -> LengthUnit:
        """"""
        return self.__lengthUnit

    @lengthUnit.setter
    def lengthUnit(self, value: LengthUnit):
        """Set lengthUnit"""
        self.__lengthUnit = value

    @property
    def powerUnit(self) -> PowerUnit:
        """"""
        return self.__powerUnit

    @powerUnit.setter
    def powerUnit(self, value: PowerUnit):
        """Set powerUnit"""
        self.__powerUnit = value
