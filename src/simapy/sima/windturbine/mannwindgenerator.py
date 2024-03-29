# This an autogenerated file
# 
# Generated with MannWindGenerator
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.mannwindgenerator import MannWindGeneratorBlueprint
from typing import Dict
from ..sima import ConditionSelectable
from ..sima import NamedObject
from ..sima import ScriptableValue
from .manninputformat import MannInputFormat

class MannWindGenerator(NamedObject,ConditionSelectable):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    baseFileName : str
         (default 'sima')
    alphaEpsilon : float
         Spectrum scale parameter(default 0.0)
    lengthScale : float
         Length scale(default 0.0)
    gamma : float
         Shear distortion parameter(default 3.9)
    seed : int
         Start seed for random number generator(default 0)
    gridPointsX : int
         Grid points in X-direction (Power of 2)(default 0)
    gridPointsY : int
         Grid points in Y-direction (Power of 2)(default 0)
    gridPointsZ : int
         Grid points in Z-direction (Power of 2)(default 0)
    pointDistanceX : float
         Distance between grid points in X direction(default 0.0)
    pointDistanceY : float
         Distance between grid points in Y direction(default 0.0)
    pointDistanceZ : float
         Distance between grid points in Z direction(default 0.0)
    hfCompensation : bool
         High Frequency Compensation(default True)
    turbulenceIntensity : float
         Turbulence intensity(default 0.0)
    meanWindSpeed : float
         Mean wind speed(default 0.0)
    transient : float
         Starting point in simulation used for calculation of scaling factor(default 0.0)
    inputFormat : MannInputFormat
    windSeriesDuration : float
         Length of simulation(default 0.0)
    gridWidth : float
         Domain size in Y-direction(default 0.0)
    gridHeight : float
         Domain size in Z-direction(default 0.0)
    lengthFactor : float
         (default 0.8)
    longTurbScaleParam : float
         Longitudenal Turbulence Scale Parameter(default 0.0)
    """

    def __init__(self , description="", baseFileName='sima', alphaEpsilon=0.0, lengthScale=0.0, gamma=3.9, seed=0, gridPointsX=0, gridPointsY=0, gridPointsZ=0, pointDistanceX=0.0, pointDistanceY=0.0, pointDistanceZ=0.0, hfCompensation=True, turbulenceIntensity=0.0, meanWindSpeed=0.0, transient=0.0, inputFormat=MannInputFormat.DIRECT, windSeriesDuration=0.0, gridWidth=0.0, gridHeight=0.0, lengthFactor=0.8, longTurbScaleParam=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.baseFileName = baseFileName
        self.alphaEpsilon = alphaEpsilon
        self.lengthScale = lengthScale
        self.gamma = gamma
        self.seed = seed
        self.gridPointsX = gridPointsX
        self.gridPointsY = gridPointsY
        self.gridPointsZ = gridPointsZ
        self.pointDistanceX = pointDistanceX
        self.pointDistanceY = pointDistanceY
        self.pointDistanceZ = pointDistanceZ
        self.hfCompensation = hfCompensation
        self.turbulenceIntensity = turbulenceIntensity
        self.meanWindSpeed = meanWindSpeed
        self.transient = transient
        self.inputFormat = inputFormat
        self.windSeriesDuration = windSeriesDuration
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.lengthFactor = lengthFactor
        self.longTurbScaleParam = longTurbScaleParam
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MannWindGeneratorBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def baseFileName(self) -> str:
        """"""
        return self.__baseFileName

    @baseFileName.setter
    def baseFileName(self, value: str):
        """Set baseFileName"""
        self.__baseFileName = value

    @property
    def alphaEpsilon(self) -> float:
        """Spectrum scale parameter"""
        return self.__alphaEpsilon

    @alphaEpsilon.setter
    def alphaEpsilon(self, value: float):
        """Set alphaEpsilon"""
        self.__alphaEpsilon = float(value)

    @property
    def lengthScale(self) -> float:
        """Length scale"""
        return self.__lengthScale

    @lengthScale.setter
    def lengthScale(self, value: float):
        """Set lengthScale"""
        self.__lengthScale = float(value)

    @property
    def gamma(self) -> float:
        """Shear distortion parameter"""
        return self.__gamma

    @gamma.setter
    def gamma(self, value: float):
        """Set gamma"""
        self.__gamma = float(value)

    @property
    def seed(self) -> int:
        """Start seed for random number generator"""
        return self.__seed

    @seed.setter
    def seed(self, value: int):
        """Set seed"""
        self.__seed = int(value)

    @property
    def gridPointsX(self) -> int:
        """Grid points in X-direction (Power of 2)"""
        return self.__gridPointsX

    @gridPointsX.setter
    def gridPointsX(self, value: int):
        """Set gridPointsX"""
        self.__gridPointsX = int(value)

    @property
    def gridPointsY(self) -> int:
        """Grid points in Y-direction (Power of 2)"""
        return self.__gridPointsY

    @gridPointsY.setter
    def gridPointsY(self, value: int):
        """Set gridPointsY"""
        self.__gridPointsY = int(value)

    @property
    def gridPointsZ(self) -> int:
        """Grid points in Z-direction (Power of 2)"""
        return self.__gridPointsZ

    @gridPointsZ.setter
    def gridPointsZ(self, value: int):
        """Set gridPointsZ"""
        self.__gridPointsZ = int(value)

    @property
    def pointDistanceX(self) -> float:
        """Distance between grid points in X direction"""
        return self.__pointDistanceX

    @pointDistanceX.setter
    def pointDistanceX(self, value: float):
        """Set pointDistanceX"""
        self.__pointDistanceX = float(value)

    @property
    def pointDistanceY(self) -> float:
        """Distance between grid points in Y direction"""
        return self.__pointDistanceY

    @pointDistanceY.setter
    def pointDistanceY(self, value: float):
        """Set pointDistanceY"""
        self.__pointDistanceY = float(value)

    @property
    def pointDistanceZ(self) -> float:
        """Distance between grid points in Z direction"""
        return self.__pointDistanceZ

    @pointDistanceZ.setter
    def pointDistanceZ(self, value: float):
        """Set pointDistanceZ"""
        self.__pointDistanceZ = float(value)

    @property
    def hfCompensation(self) -> bool:
        """High Frequency Compensation"""
        return self.__hfCompensation

    @hfCompensation.setter
    def hfCompensation(self, value: bool):
        """Set hfCompensation"""
        self.__hfCompensation = bool(value)

    @property
    def turbulenceIntensity(self) -> float:
        """Turbulence intensity"""
        return self.__turbulenceIntensity

    @turbulenceIntensity.setter
    def turbulenceIntensity(self, value: float):
        """Set turbulenceIntensity"""
        self.__turbulenceIntensity = float(value)

    @property
    def meanWindSpeed(self) -> float:
        """Mean wind speed"""
        return self.__meanWindSpeed

    @meanWindSpeed.setter
    def meanWindSpeed(self, value: float):
        """Set meanWindSpeed"""
        self.__meanWindSpeed = float(value)

    @property
    def transient(self) -> float:
        """Starting point in simulation used for calculation of scaling factor"""
        return self.__transient

    @transient.setter
    def transient(self, value: float):
        """Set transient"""
        self.__transient = float(value)

    @property
    def inputFormat(self) -> MannInputFormat:
        """"""
        return self.__inputFormat

    @inputFormat.setter
    def inputFormat(self, value: MannInputFormat):
        """Set inputFormat"""
        self.__inputFormat = value

    @property
    def windSeriesDuration(self) -> float:
        """Length of simulation"""
        return self.__windSeriesDuration

    @windSeriesDuration.setter
    def windSeriesDuration(self, value: float):
        """Set windSeriesDuration"""
        self.__windSeriesDuration = float(value)

    @property
    def gridWidth(self) -> float:
        """Domain size in Y-direction"""
        return self.__gridWidth

    @gridWidth.setter
    def gridWidth(self, value: float):
        """Set gridWidth"""
        self.__gridWidth = float(value)

    @property
    def gridHeight(self) -> float:
        """Domain size in Z-direction"""
        return self.__gridHeight

    @gridHeight.setter
    def gridHeight(self, value: float):
        """Set gridHeight"""
        self.__gridHeight = float(value)

    @property
    def lengthFactor(self) -> float:
        """"""
        return self.__lengthFactor

    @lengthFactor.setter
    def lengthFactor(self, value: float):
        """Set lengthFactor"""
        self.__lengthFactor = float(value)

    @property
    def longTurbScaleParam(self) -> float:
        """Longitudenal Turbulence Scale Parameter"""
        return self.__longTurbScaleParam

    @longTurbScaleParam.setter
    def longTurbScaleParam(self, value: float):
        """Set longTurbScaleParam"""
        self.__longTurbScaleParam = float(value)
