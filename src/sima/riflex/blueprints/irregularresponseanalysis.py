# 
# Generated with IrregularResponseAnalysisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class IrregularResponseAnalysisBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="IrregularResponseAnalysis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("waveTimeSeriesFile","boolean","Wave time series read from file",default=False))
        self.attributes.append(Attribute("simulationLength","number","Length of simulation",default=11000.0))
        self.attributes.append(Attribute("timeStep","number","Simulation time step",default=0.1))
        self.attributes.append(EnumAttribute("irrWaveIndicator","sima/riflex/IrregularWaveIndicator","Irregular wave indicator"))
        self.attributes.append(EnumAttribute("irrMotionIndicator","sima/riflex/IrregularMotionIndicator","Irregular motion indicator"))
        self.attributes.append(EnumAttribute("lowFrequencyMotionIndicator","sima/riflex/LowFrequencyMotionIndicator","Low frequency motion indicator"))
        self.attributes.append(Attribute("simulationStartTime","number","Time (in generated time series) that dynamic simulation will start from",default=0.0))
        self.attributes.append(Attribute("motionScaling","boolean","Switch for scaling of terminal point motions",default=False))
        self.attributes.append(BlueprintAttribute("supportVesselMotionScalingItems","sima/riflex/SupportVesselMotionScalingItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("irregularWaveProcedure","sima/riflex/IrregularWaveProcedure","",True))
        self.attributes.append(BlueprintAttribute("waveTimeSeries","sima/riflex/WaveTimeSeries","",True))
        self.attributes.append(BlueprintAttribute("wfMotionTimeSeries","sima/riflex/WFMotionTimeSeries","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("lfMotionTimeSeries","sima/riflex/LFMotionTimeSeries","",True,Dimension("*")))