# This an autogenerated file
# 
# Generated with MannWindGenerator
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.mannwindgenerator import MannWindGeneratorBlueprint
from sima.sima.conditionselectable import ConditionSelectable
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.windturbine.manninputformat import MannInputFormat

class MannWindGenerator(NamedObject,ConditionSelectable):
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

    def __init__(self , name:str="", description:str="", _id:str="", baseFileName:str='sima', alphaEpsilon:float=0.0, lengthScale:float=0.0, gamma:float=3.9, seed:int=0, gridPointsX:int=0, gridPointsY:int=0, gridPointsZ:int=0, pointDistanceX:float=0.0, pointDistanceY:float=0.0, pointDistanceZ:float=0.0, hfCompensation:bool=True, turbulenceIntensity:float=0.0, meanWindSpeed:float=0.0, transient:float=0.0, inputFormat:MannInputFormat=MannInputFormat.DIRECT, windSeriesDuration:float=0.0, gridWidth:float=0.0, gridHeight:float=0.0, lengthFactor:float=0.8, longTurbScaleParam:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__baseFileName = baseFileName
        self.__alphaEpsilon = alphaEpsilon
        self.__lengthScale = lengthScale
        self.__gamma = gamma
        self.__seed = seed
        self.__gridPointsX = gridPointsX
        self.__gridPointsY = gridPointsY
        self.__gridPointsZ = gridPointsZ
        self.__pointDistanceX = pointDistanceX
        self.__pointDistanceY = pointDistanceY
        self.__pointDistanceZ = pointDistanceZ
        self.__hfCompensation = hfCompensation
        self.__turbulenceIntensity = turbulenceIntensity
        self.__meanWindSpeed = meanWindSpeed
        self.__transient = transient
        self.__inputFormat = inputFormat
        self.__windSeriesDuration = windSeriesDuration
        self.__gridWidth = gridWidth
        self.__gridHeight = gridHeight
        self.__lengthFactor = lengthFactor
        self.__longTurbScaleParam = longTurbScaleParam
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MannWindGeneratorBlueprint()


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
    def baseFileName(self) -> str:
        """"""
        return self.__baseFileName

    @baseFileName.setter
    def baseFileName(self, value: str):
        """Set baseFileName"""
        self.__baseFileName = str(value)

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
