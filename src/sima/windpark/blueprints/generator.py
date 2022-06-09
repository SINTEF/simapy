# 
# Generated with GeneratorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class GeneratorBlueprint(ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="Generator", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("airDensity","number","",default=1.3))
        self.attributes.append(Attribute("kinematicViscosity","number","",default=1.824e-05))
        self.attributes.append(EnumAttribute("meanderingOption","sima/windpark/MeanderingAnalysisOption","Compute or skip computation of dynamic wake meandering"))
        self.attributes.append(EnumAttribute("powerOption","sima/windpark/PowerOption","Compute or skip computation of power"))
        self.attributes.append(EnumAttribute("deficitOption","sima/windpark/DeficitAnalysisOption","Compute or read near field deficit"))
        self.attributes.append(EnumAttribute("focusOption","sima/windpark/Focus","Compute for a specific turbine or for the whole park"))
        self.attributes.append(Attribute("angleChange","number","Rotor angle change pr step",default=3.0))
        self.attributes.append(Attribute("maxLaps","integer","Maximum number of rotor laps for profile convergence",default=30))
        self.attributes.append(EnumAttribute("deficitFileContents","sima/windpark/DeficitFileContents",""))
        self.attributes.append(Attribute("deficitFileName","string","",default=""))
        self.attributes.append(Attribute("ambientMixingParameter","number","Ambient mixing parameters",default=0.0))
        self.attributes.append(Attribute("deficitParameter","number","Deficit parameter",default=0.0))
        self.attributes.append(EnumAttribute("multipleDeficitMethod","sima/windpark/MultipleDeficitMethod","Option for choosing the best approach for handling multiple deficits"))
        self.attributes.append(EnumAttribute("nearWakeLengthModel","sima/windpark/NearWakeLengthModel",""))
        self.attributes.append(EnumAttribute("viscosityFilter","sima/windpark/ViscosityFilter",""))
        self.attributes.append(EnumAttribute("incomingWind","sima/windpark/IncomingWind",""))
        self.attributes.append(Attribute("speedIncrement","number","Speed increment for calculation of deficits",default=0.25))
        self.attributes.append(Attribute("deficitDepthFactor","number","Factor on deficit depth",default=0.6))
        self.attributes.append(Attribute("deficitGradientFactor","number","Factor on depth derivative",default=0.35))
        self.attributes.append(Attribute("cutOffFilterLengthFactor","number","Cut off filter length in rotor diameter",default=2.0))
        self.attributes.append(BlueprintAttribute("windTurbineTypes","sima/windpark/WindTurbineType","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("windParkLayout","sima/windpark/WindParkTurbine","",True,Dimension("*")))
        self.attributes.append(Attribute("windVelocity","number","Wind velocity (Constant wind)",default=0.0))
        self.attributes.append(Attribute("windDirection","number","Wind direction in global system (propagation direction)\n0 deg is along global X-direction\n90 deg is along global Y-direction",default=0.0))
        self.attributes.append(Attribute("turbulenceIntencity","number","Turbulence intencity ambient wind (fine mesh)",default=0.0))
        self.attributes.append(EnumAttribute("stabilityClass","sima/windpark/StabilityClass",""))
        self.attributes.append(Attribute("coarseMeshFilename","string","",default=""))
        self.attributes.append(Attribute("fineMeshFilename","string","",default=""))
        self.attributes.append(Attribute("ambientWindFieldFilename","string","",default=""))
        self.attributes.append(EnumAttribute("turbulenceBoxOption","sima/windpark/TurbulenceBoxOption","Option for choosing whether turbulence boxes are made using DTU Mann (IECWind format) or TurbSim (Turbsim Bladed style format)"))
        self.attributes.append(Attribute("outputPrefix","string","Prefix in name of resulting wind files. File types are according to specified 'Turbulence Box Option'.  See the 'Wind specification' tab.",default='diwa'))
        self.attributes.append(Attribute("includePowerResult","boolean","",default=False))
        self.attributes.append(EnumAttribute("powerResultFormat","sima/windpark/FileFormat",""))
        self.attributes.append(Attribute("includeVisualization","boolean","",default=False))
        self.attributes.append(EnumAttribute("visualizationFormat","sima/windpark/FileFormat",""))
        self.attributes.append(Attribute("animationTime","number","",default=0.0))
        self.attributes.append(EnumAttribute("areaAveragingOption","sima/windpark/AreaAveragingOption","Option for selecting type of area averaging integration"))
        self.attributes.append(EnumAttribute("filterLengthOption","sima/windpark/FilterLengthOption","Option for selecting filter length type"))
        self.attributes.append(EnumAttribute("weightOption","sima/windpark/WeightOption","Weighting function option for calculating the meandering velocities"))
        self.attributes.append(Attribute("weightConst","number","",default=1.0))
        self.attributes.append(BlueprintAttribute("meanderingScaling","sima/windpark/TurbulenceBoxScaling","",True))
        self.attributes.append(BlueprintAttribute("addedWakeScaling","sima/windpark/TurbulenceBoxScaling","",True))
        self.attributes.append(BlueprintAttribute("ambientScaling","sima/windpark/TurbulenceBoxScaling","",True))
        self.attributes.append(Attribute("applyLowPassFilter","boolean","",default=True))
        self.attributes.append(Attribute("applyAreaAveraging","boolean","",default=True))
        self.attributes.append(EnumAttribute("lowPassFrequencyOption","sima/windpark/LowPassFrequencyOption","Lowpass cutoff frequency option"))
        self.attributes.append(Attribute("lowPassFrequency","number","Cutoff frequency",default=0.0))