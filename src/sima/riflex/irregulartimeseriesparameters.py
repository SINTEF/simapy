# This an autogenerated file
# 
# Generated with IrregularTimeSeriesParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.irregulartimeseriesparameters import IrregularTimeSeriesParametersBlueprint
from typing import Dict
from .waveamplitudecomputation import WaveAmplitudeComputation
from .wavecomputationmethod import WaveComputationMethod
from sima.sima import MOAO
from sima.sima import ScriptableValue

class IrregularTimeSeriesParameters(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    randomSeedWaves : int
         Starting parameter of random number generator(default 1)
    useStochasticAmplitudes : bool
         (default False)
    waveLength : float
         Length of generated time series(default 16384.0)
    timeIncrement : float
         Time increment for time series generation(default 0.5)
    waveComputationMethod : WaveComputationMethod
         Method parameter for computation of prescribed waves
    waveAmplitudeComputation : WaveAmplitudeComputation
         Option for amplitude computation of waves (The phace is always stochastic)
    numWindWaveFreqComponents : int
         Wind waves: Number of frequency components in the wind wave frequency range. The min and max frequencies are determined by the actual wind wave spectrum.(default 0)
    numSwellFreqComponents : int
         Swell: Number of frequency components in the swell frequency range. The min and max frequencies are determined by the actual swell spectrum(default 0)
    waveCutFactor : float
         Cut factor for wave components.(default 0.0)
    largePatchPoints : int
         Number of points in one dimension in the large patch.(default 0)
    largePatchLength : float
         Length of large patch.(default 0.0)
    smallPatchPoints : int
         Number of points in one dimension in the small patch.(default 0)
    patchRatio : int
         Ratio between length of small patch and length of large patch.(default 0)
    """

    def __init__(self , description="", randomSeedWaves=1, useStochasticAmplitudes=False, waveLength=16384.0, timeIncrement=0.5, waveComputationMethod=WaveComputationMethod.FFT, waveAmplitudeComputation=WaveAmplitudeComputation.DETERMINISTIC, numWindWaveFreqComponents=0, numSwellFreqComponents=0, waveCutFactor=0.0, largePatchPoints=0, largePatchLength=0.0, smallPatchPoints=0, patchRatio=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.randomSeedWaves = randomSeedWaves
        self.useStochasticAmplitudes = useStochasticAmplitudes
        self.waveLength = waveLength
        self.timeIncrement = timeIncrement
        self.waveComputationMethod = waveComputationMethod
        self.waveAmplitudeComputation = waveAmplitudeComputation
        self.numWindWaveFreqComponents = numWindWaveFreqComponents
        self.numSwellFreqComponents = numSwellFreqComponents
        self.waveCutFactor = waveCutFactor
        self.largePatchPoints = largePatchPoints
        self.largePatchLength = largePatchLength
        self.smallPatchPoints = smallPatchPoints
        self.patchRatio = patchRatio
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return IrregularTimeSeriesParametersBlueprint()


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
    def randomSeedWaves(self) -> int:
        """Starting parameter of random number generator"""
        return self.__randomSeedWaves

    @randomSeedWaves.setter
    def randomSeedWaves(self, value: int):
        """Set randomSeedWaves"""
        self.__randomSeedWaves = int(value)

    @property
    def useStochasticAmplitudes(self) -> bool:
        """"""
        return self.__useStochasticAmplitudes

    @useStochasticAmplitudes.setter
    def useStochasticAmplitudes(self, value: bool):
        """Set useStochasticAmplitudes"""
        self.__useStochasticAmplitudes = bool(value)

    @property
    def waveLength(self) -> float:
        """Length of generated time series"""
        return self.__waveLength

    @waveLength.setter
    def waveLength(self, value: float):
        """Set waveLength"""
        self.__waveLength = float(value)

    @property
    def timeIncrement(self) -> float:
        """Time increment for time series generation"""
        return self.__timeIncrement

    @timeIncrement.setter
    def timeIncrement(self, value: float):
        """Set timeIncrement"""
        self.__timeIncrement = float(value)

    @property
    def waveComputationMethod(self) -> WaveComputationMethod:
        """Method parameter for computation of prescribed waves"""
        return self.__waveComputationMethod

    @waveComputationMethod.setter
    def waveComputationMethod(self, value: WaveComputationMethod):
        """Set waveComputationMethod"""
        self.__waveComputationMethod = value

    @property
    def waveAmplitudeComputation(self) -> WaveAmplitudeComputation:
        """Option for amplitude computation of waves (The phace is always stochastic)"""
        return self.__waveAmplitudeComputation

    @waveAmplitudeComputation.setter
    def waveAmplitudeComputation(self, value: WaveAmplitudeComputation):
        """Set waveAmplitudeComputation"""
        self.__waveAmplitudeComputation = value

    @property
    def numWindWaveFreqComponents(self) -> int:
        """Wind waves: Number of frequency components in the wind wave frequency range. The min and max frequencies are determined by the actual wind wave spectrum."""
        return self.__numWindWaveFreqComponents

    @numWindWaveFreqComponents.setter
    def numWindWaveFreqComponents(self, value: int):
        """Set numWindWaveFreqComponents"""
        self.__numWindWaveFreqComponents = int(value)

    @property
    def numSwellFreqComponents(self) -> int:
        """Swell: Number of frequency components in the swell frequency range. The min and max frequencies are determined by the actual swell spectrum"""
        return self.__numSwellFreqComponents

    @numSwellFreqComponents.setter
    def numSwellFreqComponents(self, value: int):
        """Set numSwellFreqComponents"""
        self.__numSwellFreqComponents = int(value)

    @property
    def waveCutFactor(self) -> float:
        """Cut factor for wave components."""
        return self.__waveCutFactor

    @waveCutFactor.setter
    def waveCutFactor(self, value: float):
        """Set waveCutFactor"""
        self.__waveCutFactor = float(value)

    @property
    def largePatchPoints(self) -> int:
        """Number of points in one dimension in the large patch."""
        return self.__largePatchPoints

    @largePatchPoints.setter
    def largePatchPoints(self, value: int):
        """Set largePatchPoints"""
        self.__largePatchPoints = int(value)

    @property
    def largePatchLength(self) -> float:
        """Length of large patch."""
        return self.__largePatchLength

    @largePatchLength.setter
    def largePatchLength(self, value: float):
        """Set largePatchLength"""
        self.__largePatchLength = float(value)

    @property
    def smallPatchPoints(self) -> int:
        """Number of points in one dimension in the small patch."""
        return self.__smallPatchPoints

    @smallPatchPoints.setter
    def smallPatchPoints(self, value: int):
        """Set smallPatchPoints"""
        self.__smallPatchPoints = int(value)

    @property
    def patchRatio(self) -> int:
        """Ratio between length of small patch and length of large patch."""
        return self.__patchRatio

    @patchRatio.setter
    def patchRatio(self, value: int):
        """Set patchRatio"""
        self.__patchRatio = int(value)
