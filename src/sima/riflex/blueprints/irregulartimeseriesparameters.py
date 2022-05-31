# 
# Generated with IrregularTimeSeriesParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class IrregularTimeSeriesParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="IrregularTimeSeriesParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("randomSeedWaves","integer","Starting parameter of random number generator",default=1))
        self.attributes.append(Attribute("useStochasticAmplitudes","boolean","",default=False))
        self.attributes.append(Attribute("waveLength","number","Length of generated time series",default=16384.0))
        self.attributes.append(Attribute("timeIncrement","number","Time increment for time series generation",default=0.5))
        self.attributes.append(EnumAttribute("waveComputationMethod","sima/riflex/WaveComputationMethod","Method parameter for computation of prescribed waves"))
        self.attributes.append(EnumAttribute("waveAmplitudeComputation","sima/riflex/WaveAmplitudeComputation","Option for amplitude computation of waves (The phace is always stochastic)"))
        self.attributes.append(Attribute("numWindWaveFreqComponents","integer","Wind waves: Number of frequency components in the wind wave frequency range. The min and max frequencies are determined by the actual wind wave spectrum.",default=0))
        self.attributes.append(Attribute("numSwellFreqComponents","integer","Swell: Number of frequency components in the swell frequency range. The min and max frequencies are determined by the actual swell spectrum",default=0))
        self.attributes.append(Attribute("waveCutFactor","number","Cut factor for wave components.",default=0.0))
        self.attributes.append(Attribute("largePatchPoints","integer","Number of points in one dimension in the large patch.",default=0))
        self.attributes.append(Attribute("largePatchLength","number","Length of large patch.",default=0.0))
        self.attributes.append(Attribute("smallPatchPoints","integer","Number of points in one dimension in the small patch.",default=0))
        self.attributes.append(Attribute("patchRatio","integer","Ratio between length of small patch and length of large patch.",default=0))