# This an autogenerated file
# 
# Generated with DOFControlConfiguration
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dofcontrolconfiguration import DOFControlConfigurationBlueprint
from typing import Dict
from .controldof import ControlDOF
from sima.sima import MOAO
from sima.sima import ScriptableValue

class DOFControlConfiguration(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    dof : ControlDOF
         Degree Of Freedom
    mass : float
         Total Mass(default 0.0)
    drag : float
         drag coefficient(default 0.0)
    stiffness : float
         Linear stiffness in global direction (not from DP system)(default 0.0)
    naturalPeriod : float
         Wanted natural period(default 100.0)
    dampingFactor : float
         Damping factors rel. to critical damping(default 0.7)
    integrationTime : float
         Integration time, small time means heavy use of integral effect \n(Discontinuity in 0, 0 means no integral effect)(default 0.0)
    cutOffPeriod : float
         Cut-off period for LP-filtering(default 0.0)
    filterDampingFactor : float
         Damping factors rel. to critical damping(default 0.0)
    integralLF : float
         Integral LF estimation gain:\n\n* LF_surge_integralgain=0.00001*mass_surge 	[N/m] (where the mass is in [kg])\n* LF_sway_integralgain=0.00001*mass_sway [N/m] (where the mass is in [kg])\n* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (where the mass is in [kg.m^2])\n* For Current bias estimation (see point 11), the default values are:\n* LF_surge_integralgain=0.0025 [1/s] \n* LF_sway_integralgain=0.0025 [1/s]\n* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (as for the force estimation)(default 0.0)
    proportionalHF : float
         Proportional HF estimation gain(default 0.1)
    dampingOnly : bool
         Turn off proportional control and use damping only(default False)
    """

    def __init__(self , description="", dof=ControlDOF.NONE, mass=0.0, drag=0.0, stiffness=0.0, naturalPeriod=100.0, dampingFactor=0.7, integrationTime=0.0, cutOffPeriod=0.0, filterDampingFactor=0.0, integralLF=0.0, proportionalHF=0.1, dampingOnly=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.dof = dof
        self.mass = mass
        self.drag = drag
        self.stiffness = stiffness
        self.naturalPeriod = naturalPeriod
        self.dampingFactor = dampingFactor
        self.integrationTime = integrationTime
        self.cutOffPeriod = cutOffPeriod
        self.filterDampingFactor = filterDampingFactor
        self.integralLF = integralLF
        self.proportionalHF = proportionalHF
        self.dampingOnly = dampingOnly
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DOFControlConfigurationBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def dof(self) -> ControlDOF:
        """Degree Of Freedom"""
        return self.__dof

    @dof.setter
    def dof(self, value: ControlDOF):
        """Set dof"""
        self.__dof = value

    @property
    def mass(self) -> float:
        """Total Mass"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def drag(self) -> float:
        """drag coefficient"""
        return self.__drag

    @drag.setter
    def drag(self, value: float):
        """Set drag"""
        self.__drag = float(value)

    @property
    def stiffness(self) -> float:
        """Linear stiffness in global direction (not from DP system)"""
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """Set stiffness"""
        self.__stiffness = float(value)

    @property
    def naturalPeriod(self) -> float:
        """Wanted natural period"""
        return self.__naturalPeriod

    @naturalPeriod.setter
    def naturalPeriod(self, value: float):
        """Set naturalPeriod"""
        self.__naturalPeriod = float(value)

    @property
    def dampingFactor(self) -> float:
        """Damping factors rel. to critical damping"""
        return self.__dampingFactor

    @dampingFactor.setter
    def dampingFactor(self, value: float):
        """Set dampingFactor"""
        self.__dampingFactor = float(value)

    @property
    def integrationTime(self) -> float:
        """Integration time, small time means heavy use of integral effect 
(Discontinuity in 0, 0 means no integral effect)"""
        return self.__integrationTime

    @integrationTime.setter
    def integrationTime(self, value: float):
        """Set integrationTime"""
        self.__integrationTime = float(value)

    @property
    def cutOffPeriod(self) -> float:
        """Cut-off period for LP-filtering"""
        return self.__cutOffPeriod

    @cutOffPeriod.setter
    def cutOffPeriod(self, value: float):
        """Set cutOffPeriod"""
        self.__cutOffPeriod = float(value)

    @property
    def filterDampingFactor(self) -> float:
        """Damping factors rel. to critical damping"""
        return self.__filterDampingFactor

    @filterDampingFactor.setter
    def filterDampingFactor(self, value: float):
        """Set filterDampingFactor"""
        self.__filterDampingFactor = float(value)

    @property
    def integralLF(self) -> float:
        """Integral LF estimation gain:

* LF_surge_integralgain=0.00001*mass_surge 	[N/m] (where the mass is in [kg])
* LF_sway_integralgain=0.00001*mass_sway [N/m] (where the mass is in [kg])
* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (where the mass is in [kg.m^2])
* For Current bias estimation (see point 11), the default values are:
* LF_surge_integralgain=0.0025 [1/s] 
* LF_sway_integralgain=0.0025 [1/s]
* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (as for the force estimation)"""
        return self.__integralLF

    @integralLF.setter
    def integralLF(self, value: float):
        """Set integralLF"""
        self.__integralLF = float(value)

    @property
    def proportionalHF(self) -> float:
        """Proportional HF estimation gain"""
        return self.__proportionalHF

    @proportionalHF.setter
    def proportionalHF(self, value: float):
        """Set proportionalHF"""
        self.__proportionalHF = float(value)

    @property
    def dampingOnly(self) -> bool:
        """Turn off proportional control and use damping only"""
        return self.__dampingOnly

    @dampingOnly.setter
    def dampingOnly(self, value: bool):
        """Set dampingOnly"""
        self.__dampingOnly = bool(value)