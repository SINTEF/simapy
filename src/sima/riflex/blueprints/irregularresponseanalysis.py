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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("waveTimeSeriesFile","boolean","Wave time series read from file",default=False))
        self.add_attribute(Attribute("simulationLength","number","Length of simulation",default=11000.0))
        self.add_attribute(Attribute("timeStep","number","Simulation time step",default=0.1))
        self.add_attribute(EnumAttribute("irrWaveIndicator","sima/riflex/IrregularWaveIndicator","Irregular wave indicator"))
        self.add_attribute(EnumAttribute("irrMotionIndicator","sima/riflex/IrregularMotionIndicator","Irregular motion indicator"))
        self.add_attribute(EnumAttribute("lowFrequencyMotionIndicator","sima/riflex/LowFrequencyMotionIndicator","Low frequency motion indicator"))
        self.add_attribute(Attribute("simulationStartTime","number","Time (in generated time series) that dynamic simulation will start from",default=0.0))
        self.add_attribute(Attribute("motionScaling","boolean","Switch for scaling of terminal point motions",default=False))
        self.add_attribute(BlueprintAttribute("supportVesselMotionScalingItems","sima/riflex/SupportVesselMotionScalingItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("irregularWaveProcedure","sima/riflex/IrregularWaveProcedure","",True))
        self.add_attribute(BlueprintAttribute("waveTimeSeries","sima/riflex/WaveTimeSeries","",True))
        self.add_attribute(BlueprintAttribute("wfMotionTimeSeries","sima/riflex/WFMotionTimeSeries","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("lfMotionTimeSeries","sima/riflex/LFMotionTimeSeries","",True,Dimension("*")))