# This an autogenerated file
# 
# Generated with WindTurbine
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.windturbine import WindTurbineBlueprint
from typing import Dict
from sima.riflex.bladeitem import BladeItem
from sima.riflex.horizontalaxiscontroller import HorizontalAxisController
from sima.riflex.horizontalaxisyawcontroller import HorizontalAxisYawController
from sima.riflex.measurementelement import MeasurementElement
from sima.riflex.measurementnode import MeasurementNode
from sima.riflex.turbineorientation import TurbineOrientation
from sima.riflex.windturbineloadoption import WindTurbineLoadOption
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine
    from sima.sima.body import Body

class WindTurbine(NamedObject):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    shaftLine : ARLine
         Reference to the line that is used for shaft modelling
    blades : List[BladeItem]
    controller : HorizontalAxisController
    body : Body
         Reference to SIMO body with wind
    towerLine : ARLine
         Reference to the line that is used for tower modelling.\nIf specified the incoming wind acting on the blades will be modified due to the presence of the tower.
    windLoadOption : WindTurbineLoadOption
         If the aerodynamic moment is removed, Cm is treated as zero and the distance between aerodynamic and structural axes is ignored.
    turbineOrientation : TurbineOrientation
         Turbine orientation
    bakFactor : float
         Bak correction in tower shadow(default 0.1)
    dragEffect : bool
         Drag correction in tower shadow(default True)
    advancedOptions : bool
         Use advanced aerodynamic options(default True)
    inductionCalculation : bool
         It is recommended to turn off the induction calculation for a parked or idling wind turbine.(default True)
    prandtlTip : bool
         The correction for tip loss due to the finite number of blades may be applied or removed.(default True)
    prandtlRoot : bool
         The correction for hub loss due to the finite number of blades may be applied or removed.(default True)
    prandtlYaw : bool
         If yaw correction is selected, the Prandtl factor is modified based on the angle between the incoming wind and the rotor plane.(default True)
    measurementNodes : List[MeasurementNode]
    measurementElements : List[MeasurementElement]
    yawController : HorizontalAxisYawController
    """

    def __init__(self , _id="", name="", windLoadOption=WindTurbineLoadOption.INCLUDE, turbineOrientation=TurbineOrientation.UPWIND, bakFactor=0.1, dragEffect=True, advancedOptions=True, inductionCalculation=True, prandtlTip=True, prandtlRoot=True, prandtlYaw=True, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.shaftLine = None
        self.blades = list()
        self.controller = None
        self.body = None
        self.towerLine = None
        self.windLoadOption = windLoadOption
        self.turbineOrientation = turbineOrientation
        self.bakFactor = bakFactor
        self.dragEffect = dragEffect
        self.advancedOptions = advancedOptions
        self.inductionCalculation = inductionCalculation
        self.prandtlTip = prandtlTip
        self.prandtlRoot = prandtlRoot
        self.prandtlYaw = prandtlYaw
        self.measurementNodes = list()
        self.measurementElements = list()
        self.yawController = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WindTurbineBlueprint()


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
    def shaftLine(self) -> ARLine:
        """Reference to the line that is used for shaft modelling"""
        return self.__shaftLine

    @shaftLine.setter
    def shaftLine(self, value: ARLine):
        """Set shaftLine"""
        self.__shaftLine = value

    @property
    def blades(self) -> List[BladeItem]:
        """"""
        return self.__blades

    @blades.setter
    def blades(self, value: List[BladeItem]):
        """Set blades"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__blades = value

    @property
    def controller(self) -> HorizontalAxisController:
        """"""
        return self.__controller

    @controller.setter
    def controller(self, value: HorizontalAxisController):
        """Set controller"""
        self.__controller = value

    @property
    def body(self) -> Body:
        """Reference to SIMO body with wind"""
        return self.__body

    @body.setter
    def body(self, value: Body):
        """Set body"""
        self.__body = value

    @property
    def towerLine(self) -> ARLine:
        """Reference to the line that is used for tower modelling.
If specified the incoming wind acting on the blades will be modified due to the presence of the tower."""
        return self.__towerLine

    @towerLine.setter
    def towerLine(self, value: ARLine):
        """Set towerLine"""
        self.__towerLine = value

    @property
    def windLoadOption(self) -> WindTurbineLoadOption:
        """If the aerodynamic moment is removed, Cm is treated as zero and the distance between aerodynamic and structural axes is ignored."""
        return self.__windLoadOption

    @windLoadOption.setter
    def windLoadOption(self, value: WindTurbineLoadOption):
        """Set windLoadOption"""
        self.__windLoadOption = value

    @property
    def turbineOrientation(self) -> TurbineOrientation:
        """Turbine orientation"""
        return self.__turbineOrientation

    @turbineOrientation.setter
    def turbineOrientation(self, value: TurbineOrientation):
        """Set turbineOrientation"""
        self.__turbineOrientation = value

    @property
    def bakFactor(self) -> float:
        """Bak correction in tower shadow"""
        return self.__bakFactor

    @bakFactor.setter
    def bakFactor(self, value: float):
        """Set bakFactor"""
        self.__bakFactor = float(value)

    @property
    def dragEffect(self) -> bool:
        """Drag correction in tower shadow"""
        return self.__dragEffect

    @dragEffect.setter
    def dragEffect(self, value: bool):
        """Set dragEffect"""
        self.__dragEffect = bool(value)

    @property
    def advancedOptions(self) -> bool:
        """Use advanced aerodynamic options"""
        return self.__advancedOptions

    @advancedOptions.setter
    def advancedOptions(self, value: bool):
        """Set advancedOptions"""
        self.__advancedOptions = bool(value)

    @property
    def inductionCalculation(self) -> bool:
        """It is recommended to turn off the induction calculation for a parked or idling wind turbine."""
        return self.__inductionCalculation

    @inductionCalculation.setter
    def inductionCalculation(self, value: bool):
        """Set inductionCalculation"""
        self.__inductionCalculation = bool(value)

    @property
    def prandtlTip(self) -> bool:
        """The correction for tip loss due to the finite number of blades may be applied or removed."""
        return self.__prandtlTip

    @prandtlTip.setter
    def prandtlTip(self, value: bool):
        """Set prandtlTip"""
        self.__prandtlTip = bool(value)

    @property
    def prandtlRoot(self) -> bool:
        """The correction for hub loss due to the finite number of blades may be applied or removed."""
        return self.__prandtlRoot

    @prandtlRoot.setter
    def prandtlRoot(self, value: bool):
        """Set prandtlRoot"""
        self.__prandtlRoot = bool(value)

    @property
    def prandtlYaw(self) -> bool:
        """If yaw correction is selected, the Prandtl factor is modified based on the angle between the incoming wind and the rotor plane."""
        return self.__prandtlYaw

    @prandtlYaw.setter
    def prandtlYaw(self, value: bool):
        """Set prandtlYaw"""
        self.__prandtlYaw = bool(value)

    @property
    def measurementNodes(self) -> List[MeasurementNode]:
        """"""
        return self.__measurementNodes

    @measurementNodes.setter
    def measurementNodes(self, value: List[MeasurementNode]):
        """Set measurementNodes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__measurementNodes = value

    @property
    def measurementElements(self) -> List[MeasurementElement]:
        """"""
        return self.__measurementElements

    @measurementElements.setter
    def measurementElements(self, value: List[MeasurementElement]):
        """Set measurementElements"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__measurementElements = value

    @property
    def yawController(self) -> HorizontalAxisYawController:
        """"""
        return self.__yawController

    @yawController.setter
    def yawController(self, value: HorizontalAxisYawController):
        """Set yawController"""
        self.__yawController = value
