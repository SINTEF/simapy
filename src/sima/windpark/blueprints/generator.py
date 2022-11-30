# 
# Generated with GeneratorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class GeneratorBlueprint(NamedBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="Generator", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("airDensity","number","",default=1.3))
        self.add_attribute(Attribute("kinematicViscosity","number","",default=1.824e-05))
        self.add_attribute(EnumAttribute("meanderingOption","sima/windpark/MeanderingAnalysisOption","Compute or skip computation of dynamic wake meandering"))
        self.add_attribute(EnumAttribute("powerOption","sima/windpark/PowerOption","Compute or skip computation of power"))
        self.add_attribute(EnumAttribute("deficitOption","sima/windpark/DeficitAnalysisOption","Compute or read near field deficit"))
        self.add_attribute(EnumAttribute("focusOption","sima/windpark/Focus","Compute for a specific turbine or for the whole park"))
        self.add_attribute(Attribute("angleChange","number","Rotor angle change pr step",default=3.0))
        self.add_attribute(Attribute("maxLaps","integer","Maximum number of rotor laps for profile convergence",default=30))
        self.add_attribute(EnumAttribute("deficitFileContents","sima/windpark/DeficitFileContents",""))
        self.add_attribute(Attribute("deficitFileName","string",""))
        self.add_attribute(Attribute("ambientMixingParameter","number","Ambient mixing parameters",default=0.0))
        self.add_attribute(Attribute("deficitParameter","number","Deficit parameter",default=0.0))
        self.add_attribute(EnumAttribute("multipleDeficitMethod","sima/windpark/MultipleDeficitMethod","Option for choosing the best approach for handling multiple deficits"))
        self.add_attribute(EnumAttribute("nearWakeLengthModel","sima/windpark/NearWakeLengthModel",""))
        self.add_attribute(EnumAttribute("viscosityFilter","sima/windpark/ViscosityFilter",""))
        self.add_attribute(EnumAttribute("incomingWind","sima/windpark/IncomingWind",""))
        self.add_attribute(Attribute("speedIncrement","number","Speed increment for calculation of deficits",default=0.25))
        self.add_attribute(Attribute("deficitDepthFactor","number","Factor on deficit depth",default=0.6))
        self.add_attribute(Attribute("deficitGradientFactor","number","Factor on depth derivative",default=0.35))
        self.add_attribute(Attribute("cutOffFilterLengthFactor","number","Cut off filter length in rotor diameter",default=2.0))
        self.add_attribute(BlueprintAttribute("windTurbineTypes","sima/windpark/WindTurbineType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("windParkLayout","sima/windpark/WindParkTurbine","",True,Dimension("*")))
        self.add_attribute(Attribute("windVelocity","number","Wind velocity (Constant wind)",default=0.0))
        self.add_attribute(Attribute("windDirection","number","Wind direction in global system (propagation direction)\n0 deg is along global X-direction\n90 deg is along global Y-direction",default=0.0))
        self.add_attribute(Attribute("turbulenceIntencity","number","Turbulence intencity ambient wind (fine mesh)",default=0.0))
        self.add_attribute(EnumAttribute("stabilityClass","sima/windpark/StabilityClass",""))
        self.add_attribute(Attribute("coarseMeshFilename","string",""))
        self.add_attribute(Attribute("fineMeshFilename","string",""))
        self.add_attribute(Attribute("ambientWindFieldFilename","string",""))
        self.add_attribute(EnumAttribute("turbulenceBoxOption","sima/windpark/TurbulenceBoxOption","Option for choosing whether turbulence boxes are made using DTU Mann (IECWind format) or TurbSim (Turbsim Bladed style format)"))
        self.add_attribute(Attribute("outputPrefix","string","Prefix in name of resulting wind files. File types are according to specified 'Turbulence Box Option'.  See the 'Wind specification' tab.",default='diwa'))
        self.add_attribute(Attribute("includePowerResult","boolean","",default=False))
        self.add_attribute(EnumAttribute("powerResultFormat","sima/windpark/FileFormat",""))
        self.add_attribute(Attribute("includeVisualization","boolean","",default=False))
        self.add_attribute(EnumAttribute("visualizationFormat","sima/windpark/FileFormat",""))
        self.add_attribute(Attribute("animationTime","number","",default=0.0))
        self.add_attribute(EnumAttribute("areaAveragingOption","sima/windpark/AreaAveragingOption","Option for selecting type of area averaging integration"))
        self.add_attribute(EnumAttribute("filterLengthOption","sima/windpark/FilterLengthOption","Option for selecting filter length type"))
        self.add_attribute(EnumAttribute("weightOption","sima/windpark/WeightOption","Weighting function option for calculating the meandering velocities"))
        self.add_attribute(Attribute("weightConst","number","",default=1.0))
        self.add_attribute(BlueprintAttribute("meanderingScaling","sima/windpark/TurbulenceBoxScaling","",True))
        self.add_attribute(BlueprintAttribute("addedWakeScaling","sima/windpark/TurbulenceBoxScaling","",True))
        self.add_attribute(BlueprintAttribute("ambientScaling","sima/windpark/TurbulenceBoxScaling","",True))
        self.add_attribute(Attribute("applyLowPassFilter","boolean","",default=True))
        self.add_attribute(Attribute("applyAreaAveraging","boolean","",default=False))
        self.add_attribute(EnumAttribute("lowPassFrequencyOption","sima/windpark/LowPassFrequencyOption","Lowpass cutoff frequency option"))
        self.add_attribute(Attribute("lowPassFrequency","number","Cutoff frequency",default=0.0))