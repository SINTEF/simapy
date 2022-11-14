# This an autogenerated file
# 
# Generated with VerticalAxisWindTurbineController
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.verticalaxiswindturbinecontroller import VerticalAxisWindTurbineControllerBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.windturbine.gainschedulingitem import GainSchedulingItem
from sima.windturbine.tableformat import TableFormat
from sima.windturbine.windrotorspeeditem import WindRotorSpeedItem

class VerticalAxisWindTurbineController(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    sampleInterval : float
         Controller sample interval(default 0.0)
    startupLength : float
         Length of time for using start-up control logic(default 0.0)
    filterPeriodRotorSpeed : float
         Filter period for 1st order LP filter for rotor speed(default 0.0)
    filterPeriodWindSpeed : float
         Filter period for 1st order LP filter for wind speed(default 0.0)
    filterRadialFrequency : float
         Radial frequency removed by notch filter. For value < 0 no notch filter will be applied(default 0.0)
    notchFilterWidth : float
         Width parameter in notch filter(default 0.0)
    gearBoxRatio : float
         Gear box ratio (N rotations of high speed shaft for one roation of the low speed shaft, i.e. generator versus rotor)(default 0.0)
    maxTorque : float
         Maximum torque(default 0.0)
    maxTorqueRate : float
         Maximum torque rate(default 0.0)
    proportionalGain : float
         Proportional gain K that will be used for zero blade pitch angle(default 0.0)
    initialIntegratorGainRatio : float
         Initial value of integrator gain(default 0.0)
    finalIntegratorGainRatio : float
         Final value of integrator gain(default 0.0)
    integratorRelaxationTime : float
         Time period for relaxing the integrator gain after the startup period(default 0.0)
    windRotorSpeed : TableFormat
         Wind speed / rotor speed table
    gainScheduling : TableFormat
    windRotorSpeedItems : List[WindRotorSpeedItem]
    gainSchedulingItems : List[GainSchedulingItem]
    """

    def __init__(self , description="", _id=None, sampleInterval=0.0, startupLength=0.0, filterPeriodRotorSpeed=0.0, filterPeriodWindSpeed=0.0, filterRadialFrequency=0.0, notchFilterWidth=0.0, gearBoxRatio=0.0, maxTorque=0.0, maxTorqueRate=0.0, proportionalGain=0.0, initialIntegratorGainRatio=0.0, finalIntegratorGainRatio=0.0, integratorRelaxationTime=0.0, windRotorSpeed=TableFormat.DEFAULT, gainScheduling=TableFormat.DEFAULT, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.sampleInterval = sampleInterval
        self.startupLength = startupLength
        self.filterPeriodRotorSpeed = filterPeriodRotorSpeed
        self.filterPeriodWindSpeed = filterPeriodWindSpeed
        self.filterRadialFrequency = filterRadialFrequency
        self.notchFilterWidth = notchFilterWidth
        self.gearBoxRatio = gearBoxRatio
        self.maxTorque = maxTorque
        self.maxTorqueRate = maxTorqueRate
        self.proportionalGain = proportionalGain
        self.initialIntegratorGainRatio = initialIntegratorGainRatio
        self.finalIntegratorGainRatio = finalIntegratorGainRatio
        self.integratorRelaxationTime = integratorRelaxationTime
        self.windRotorSpeed = windRotorSpeed
        self.gainScheduling = gainScheduling
        self.windRotorSpeedItems = list()
        self.gainSchedulingItems = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VerticalAxisWindTurbineControllerBlueprint()


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
    def sampleInterval(self) -> float:
        """Controller sample interval"""
        return self.__sampleInterval

    @sampleInterval.setter
    def sampleInterval(self, value: float):
        """Set sampleInterval"""
        self.__sampleInterval = float(value)

    @property
    def startupLength(self) -> float:
        """Length of time for using start-up control logic"""
        return self.__startupLength

    @startupLength.setter
    def startupLength(self, value: float):
        """Set startupLength"""
        self.__startupLength = float(value)

    @property
    def filterPeriodRotorSpeed(self) -> float:
        """Filter period for 1st order LP filter for rotor speed"""
        return self.__filterPeriodRotorSpeed

    @filterPeriodRotorSpeed.setter
    def filterPeriodRotorSpeed(self, value: float):
        """Set filterPeriodRotorSpeed"""
        self.__filterPeriodRotorSpeed = float(value)

    @property
    def filterPeriodWindSpeed(self) -> float:
        """Filter period for 1st order LP filter for wind speed"""
        return self.__filterPeriodWindSpeed

    @filterPeriodWindSpeed.setter
    def filterPeriodWindSpeed(self, value: float):
        """Set filterPeriodWindSpeed"""
        self.__filterPeriodWindSpeed = float(value)

    @property
    def filterRadialFrequency(self) -> float:
        """Radial frequency removed by notch filter. For value < 0 no notch filter will be applied"""
        return self.__filterRadialFrequency

    @filterRadialFrequency.setter
    def filterRadialFrequency(self, value: float):
        """Set filterRadialFrequency"""
        self.__filterRadialFrequency = float(value)

    @property
    def notchFilterWidth(self) -> float:
        """Width parameter in notch filter"""
        return self.__notchFilterWidth

    @notchFilterWidth.setter
    def notchFilterWidth(self, value: float):
        """Set notchFilterWidth"""
        self.__notchFilterWidth = float(value)

    @property
    def gearBoxRatio(self) -> float:
        """Gear box ratio (N rotations of high speed shaft for one roation of the low speed shaft, i.e. generator versus rotor)"""
        return self.__gearBoxRatio

    @gearBoxRatio.setter
    def gearBoxRatio(self, value: float):
        """Set gearBoxRatio"""
        self.__gearBoxRatio = float(value)

    @property
    def maxTorque(self) -> float:
        """Maximum torque"""
        return self.__maxTorque

    @maxTorque.setter
    def maxTorque(self, value: float):
        """Set maxTorque"""
        self.__maxTorque = float(value)

    @property
    def maxTorqueRate(self) -> float:
        """Maximum torque rate"""
        return self.__maxTorqueRate

    @maxTorqueRate.setter
    def maxTorqueRate(self, value: float):
        """Set maxTorqueRate"""
        self.__maxTorqueRate = float(value)

    @property
    def proportionalGain(self) -> float:
        """Proportional gain K that will be used for zero blade pitch angle"""
        return self.__proportionalGain

    @proportionalGain.setter
    def proportionalGain(self, value: float):
        """Set proportionalGain"""
        self.__proportionalGain = float(value)

    @property
    def initialIntegratorGainRatio(self) -> float:
        """Initial value of integrator gain"""
        return self.__initialIntegratorGainRatio

    @initialIntegratorGainRatio.setter
    def initialIntegratorGainRatio(self, value: float):
        """Set initialIntegratorGainRatio"""
        self.__initialIntegratorGainRatio = float(value)

    @property
    def finalIntegratorGainRatio(self) -> float:
        """Final value of integrator gain"""
        return self.__finalIntegratorGainRatio

    @finalIntegratorGainRatio.setter
    def finalIntegratorGainRatio(self, value: float):
        """Set finalIntegratorGainRatio"""
        self.__finalIntegratorGainRatio = float(value)

    @property
    def integratorRelaxationTime(self) -> float:
        """Time period for relaxing the integrator gain after the startup period"""
        return self.__integratorRelaxationTime

    @integratorRelaxationTime.setter
    def integratorRelaxationTime(self, value: float):
        """Set integratorRelaxationTime"""
        self.__integratorRelaxationTime = float(value)

    @property
    def windRotorSpeed(self) -> TableFormat:
        """Wind speed / rotor speed table"""
        return self.__windRotorSpeed

    @windRotorSpeed.setter
    def windRotorSpeed(self, value: TableFormat):
        """Set windRotorSpeed"""
        self.__windRotorSpeed = value

    @property
    def gainScheduling(self) -> TableFormat:
        """"""
        return self.__gainScheduling

    @gainScheduling.setter
    def gainScheduling(self, value: TableFormat):
        """Set gainScheduling"""
        self.__gainScheduling = value

    @property
    def windRotorSpeedItems(self) -> List[WindRotorSpeedItem]:
        """"""
        return self.__windRotorSpeedItems

    @windRotorSpeedItems.setter
    def windRotorSpeedItems(self, value: List[WindRotorSpeedItem]):
        """Set windRotorSpeedItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__windRotorSpeedItems = value

    @property
    def gainSchedulingItems(self) -> List[GainSchedulingItem]:
        """"""
        return self.__gainSchedulingItems

    @gainSchedulingItems.setter
    def gainSchedulingItems(self, value: List[GainSchedulingItem]):
        """Set gainSchedulingItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__gainSchedulingItems = value
