# 
# Generated with RIFLEXDynamicCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RIFLEXDynamicCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RIFLEXDynamicCalculationParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("irregularTimeSeries","sima/riflex/IrregularTimeSeriesParameters","",True))
        self.add_attribute(BlueprintAttribute("irregularResponseAnalysis","sima/riflex/IrregularResponseAnalysis","",True))
        self.add_attribute(BlueprintAttribute("timeDomainProcedure","sima/riflex/TimeDomainProcedure","",True))
        self.add_attribute(BlueprintAttribute("envelopeCurveSpecification","sima/riflex/EnvelopeCurveSpecification","",True))
        self.add_attribute(BlueprintAttribute("displacementResponseStorage","sima/riflex/DisplacementResponseStorage","",True))
        self.add_attribute(BlueprintAttribute("forceResponseStorage","sima/riflex/ForceResponseStorage","",True))
        self.add_attribute(BlueprintAttribute("sumForceResponseStorage","sima/riflex/SumForceResponseStorage","",True))
        self.add_attribute(BlueprintAttribute("curvatureResponseStorage","sima/riflex/CurvatureResponseStorage","",True))
        self.add_attribute(BlueprintAttribute("stressStorage","sima/riflex/StressStorage","",True))
        self.add_attribute(BlueprintAttribute("turbineResponseStorage","sima/riflex/TurbineResponseStorage","",True))
        self.add_attribute(BlueprintAttribute("turbineBladeResponseStorage","sima/riflex/TurbineBladeResponseStorage","",True))
        self.add_attribute(BlueprintAttribute("supportVesselForceStorage","sima/riflex/SupportVesselForceStorage","",True))
        self.add_attribute(BlueprintAttribute("bodyForceStorage","sima/riflex/BodyForceStorage","",True))
        self.add_attribute(BlueprintAttribute("hydrodynamicLoadStorage","sima/riflex/HydrodynamicLoadStorage","",True))
        self.add_attribute(BlueprintAttribute("hlaElementForces","sima/riflex/HLAElementForce","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hlaImportedBodies","sima/riflex/ImportVesselItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("segmentLengthVariations","sima/riflex/SegmentLengthVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("temperatureVariations","sima/riflex/DynamicTemperatureVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("pressureVariations","sima/riflex/DynamicPressureVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("winchVariations","sima/riflex/DynamicWinchVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("dynamicWindChange","sima/riflex/DynamicWindChange","",True))
        self.add_attribute(BlueprintAttribute("windTurbineShutdown","sima/riflex/WindTurbineShutdown","",True))
        self.add_attribute(BlueprintAttribute("bladePitchFault","sima/riflex/BladePitchFault","",True))
        self.add_attribute(BlueprintAttribute("boundaryChangeGroups","sima/riflex/BoundaryChangeGroup","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("visualisationResponses","sima/riflex/DynmodVisualisationResponses","",True))
        self.add_attribute(BlueprintAttribute("regularWaveAnalysis","sima/riflex/RegularWaveAnalaysis","",True))
        self.add_attribute(BlueprintAttribute("regularWaveLoading","sima/riflex/RegularWaveLoading","",True))
        self.add_attribute(BlueprintAttribute("regularVesselMotions","sima/riflex/RegularVesselMotion","",True,Dimension("*")))
        self.add_attribute(Attribute("volumeForcesScaling","number","Scaling of volume forces.",default=1.0))
        self.add_attribute(Attribute("specifiedForcesScaling","number","Scaling of specified (nodal) forces.",default=1.0))
        self.add_attribute(Attribute("currentVelocitiesScaling","number","Scaling of current velocities.",default=1.0))
        self.add_attribute(Attribute("changeStaticLoads","boolean","Change applied static loads at the start of the dynamic analysis",default=False))
        self.add_attribute(BlueprintAttribute("dynamicLoads","sima/riflex/DynamicLoads","",True))