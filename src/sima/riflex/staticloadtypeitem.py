# This an autogenerated file
# 
# Generated with StaticLoadTypeItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.staticloadtypeitem import StaticLoadTypeItemBlueprint
from typing import Dict
from sima.riflex.boundarychangegroup import BoundaryChangeGroup
from sima.riflex.convergencenorm import ConvergenceNorm
from sima.riflex.pressurevariationitem import PressureVariationItem
from sima.riflex.staticloadtype import StaticLoadType
from sima.riflex.temperaturevariationitem import TemperatureVariationItem
from sima.riflex.winchvariationitem import WinchVariationItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class StaticLoadTypeItem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    runWithPrevious : bool
         Run the load group together with the last(default False)
    boundaryChangeGroup : BoundaryChangeGroup
    loadType : StaticLoadType
         Load Type
    nStep : int
         Number of load steps(default 10)
    maxIterations : int
         Maximum number of iterations during application of load(default 10)
    accuracy : float
         Required accuracy measured by displacement norm(default 1e-05)
    convergenceNorm : ConvergenceNorm
    energyAccuracy : float
          Required accuracy measured by energy norm. Value is not used if convergence norm is 'Displacement'.(default 1e-05)
    entered : bool
         start condition for pipe-in-pipe contact(default True)
    temperatureVariations : List[TemperatureVariationItem]
    pressureVariations : List[PressureVariationItem]
    winchVariations : List[WinchVariationItem]
    growthFactor : float
         Scaling factor for growth profile(default 1.0)
    windOnTurbineBlades : bool
         Enables wind force on turbine blades(default True)
    """

    def __init__(self , _id="", runWithPrevious=False, loadType=StaticLoadType.VOLU, nStep=10, maxIterations=10, accuracy=1e-05, convergenceNorm=ConvergenceNorm.DISP, energyAccuracy=1e-05, entered=True, growthFactor=1.0, windOnTurbineBlades=True, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.runWithPrevious = runWithPrevious
        self.boundaryChangeGroup = None
        self.loadType = loadType
        self.nStep = nStep
        self.maxIterations = maxIterations
        self.accuracy = accuracy
        self.convergenceNorm = convergenceNorm
        self.energyAccuracy = energyAccuracy
        self.entered = entered
        self.temperatureVariations = list()
        self.pressureVariations = list()
        self.winchVariations = list()
        self.growthFactor = growthFactor
        self.windOnTurbineBlades = windOnTurbineBlades
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StaticLoadTypeItemBlueprint()


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
    def runWithPrevious(self) -> bool:
        """Run the load group together with the last"""
        return self.__runWithPrevious

    @runWithPrevious.setter
    def runWithPrevious(self, value: bool):
        """Set runWithPrevious"""
        self.__runWithPrevious = bool(value)

    @property
    def boundaryChangeGroup(self) -> BoundaryChangeGroup:
        """"""
        return self.__boundaryChangeGroup

    @boundaryChangeGroup.setter
    def boundaryChangeGroup(self, value: BoundaryChangeGroup):
        """Set boundaryChangeGroup"""
        self.__boundaryChangeGroup = value

    @property
    def loadType(self) -> StaticLoadType:
        """Load Type"""
        return self.__loadType

    @loadType.setter
    def loadType(self, value: StaticLoadType):
        """Set loadType"""
        self.__loadType = value

    @property
    def nStep(self) -> int:
        """Number of load steps"""
        return self.__nStep

    @nStep.setter
    def nStep(self, value: int):
        """Set nStep"""
        self.__nStep = int(value)

    @property
    def maxIterations(self) -> int:
        """Maximum number of iterations during application of load"""
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, value: int):
        """Set maxIterations"""
        self.__maxIterations = int(value)

    @property
    def accuracy(self) -> float:
        """Required accuracy measured by displacement norm"""
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, value: float):
        """Set accuracy"""
        self.__accuracy = float(value)

    @property
    def convergenceNorm(self) -> ConvergenceNorm:
        """"""
        return self.__convergenceNorm

    @convergenceNorm.setter
    def convergenceNorm(self, value: ConvergenceNorm):
        """Set convergenceNorm"""
        self.__convergenceNorm = value

    @property
    def energyAccuracy(self) -> float:
        """ Required accuracy measured by energy norm. Value is not used if convergence norm is 'Displacement'."""
        return self.__energyAccuracy

    @energyAccuracy.setter
    def energyAccuracy(self, value: float):
        """Set energyAccuracy"""
        self.__energyAccuracy = float(value)

    @property
    def entered(self) -> bool:
        """start condition for pipe-in-pipe contact"""
        return self.__entered

    @entered.setter
    def entered(self, value: bool):
        """Set entered"""
        self.__entered = bool(value)

    @property
    def temperatureVariations(self) -> List[TemperatureVariationItem]:
        """"""
        return self.__temperatureVariations

    @temperatureVariations.setter
    def temperatureVariations(self, value: List[TemperatureVariationItem]):
        """Set temperatureVariations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__temperatureVariations = value

    @property
    def pressureVariations(self) -> List[PressureVariationItem]:
        """"""
        return self.__pressureVariations

    @pressureVariations.setter
    def pressureVariations(self, value: List[PressureVariationItem]):
        """Set pressureVariations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__pressureVariations = value

    @property
    def winchVariations(self) -> List[WinchVariationItem]:
        """"""
        return self.__winchVariations

    @winchVariations.setter
    def winchVariations(self, value: List[WinchVariationItem]):
        """Set winchVariations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__winchVariations = value

    @property
    def growthFactor(self) -> float:
        """Scaling factor for growth profile"""
        return self.__growthFactor

    @growthFactor.setter
    def growthFactor(self, value: float):
        """Set growthFactor"""
        self.__growthFactor = float(value)

    @property
    def windOnTurbineBlades(self) -> bool:
        """Enables wind force on turbine blades"""
        return self.__windOnTurbineBlades

    @windOnTurbineBlades.setter
    def windOnTurbineBlades(self, value: bool):
        """Set windOnTurbineBlades"""
        self.__windOnTurbineBlades = bool(value)
