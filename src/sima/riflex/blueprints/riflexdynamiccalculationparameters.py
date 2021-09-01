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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("irregularTimeSeries","sima/riflex/IrregularTimeSeriesParameters","",True))
        self.attributes.append(BlueprintAttribute("irregularResponseAnalysis","sima/riflex/IrregularResponseAnalysis","",True))
        self.attributes.append(BlueprintAttribute("timeDomainProcedure","sima/riflex/TimeDomainProcedure","",True))
        self.attributes.append(BlueprintAttribute("envelopeCurveSpecification","sima/riflex/EnvelopeCurveSpecification","",True))
        self.attributes.append(BlueprintAttribute("displacementResponseStorage","sima/riflex/DisplacementResponseStorage","",True))
        self.attributes.append(BlueprintAttribute("forceResponseStorage","sima/riflex/ForceResponseStorage","",True))
        self.attributes.append(BlueprintAttribute("sumForceResponseStorage","sima/riflex/SumForceResponseStorage","",True))
        self.attributes.append(BlueprintAttribute("curvatureResponseStorage","sima/riflex/CurvatureResponseStorage","",True))
        self.attributes.append(BlueprintAttribute("stressStorage","sima/riflex/StressStorage","",True))
        self.attributes.append(BlueprintAttribute("turbineResponseStorage","sima/riflex/TurbineResponseStorage","",True))
        self.attributes.append(BlueprintAttribute("turbineBladeResponseStorage","sima/riflex/TurbineBladeResponseStorage","",True))
        self.attributes.append(BlueprintAttribute("supportVesselForceStorage","sima/riflex/SupportVesselForceStorage","",True))
        self.attributes.append(BlueprintAttribute("bodyForceStorage","sima/riflex/BodyForceStorage","",True))
        self.attributes.append(BlueprintAttribute("hlaElementForces","sima/riflex/HLAElementForce","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("hlaImportedBodies","sima/riflex/ImportVesselItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("segmentLengthVariations","sima/riflex/SegmentLengthVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("temperatureVariations","sima/riflex/DynamicTemperatureVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("pressureVariations","sima/riflex/DynamicPressureVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("winchVariations","sima/riflex/DynamicWinchVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("dynamicWindChange","sima/riflex/DynamicWindChange","",True))
        self.attributes.append(BlueprintAttribute("windTurbineShutdown","sima/riflex/WindTurbineShutdown","",True))
        self.attributes.append(BlueprintAttribute("bladePitchFault","sima/riflex/BladePitchFault","",True))
        self.attributes.append(BlueprintAttribute("boundaryChangeGroups","sima/riflex/BoundaryChangeGroup","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("visualisationResponses","sima/riflex/DynmodVisualisationResponses","",True))
        self.attributes.append(BlueprintAttribute("regularWaveAnalysis","sima/riflex/RegularWaveAnalaysis","",True))
        self.attributes.append(BlueprintAttribute("regularWaveLoading","sima/riflex/RegularWaveLoading","",True))
        self.attributes.append(BlueprintAttribute("regularVesselMotions","sima/riflex/RegularVesselMotion","",True,Dimension("size","")))
        self.attributes.append(Attribute("volumeForcesScaling","number","Scaling of volume forces.",default=1.0))
        self.attributes.append(Attribute("specifiedForcesScaling","number","Scaling of specified (nodal) forces.",default=1.0))
        self.attributes.append(Attribute("currentVelocitiesScaling","number","Scaling of current velocities.",default=1.0))
        self.attributes.append(Attribute("changeStaticLoads","boolean","Change applied static loads at the start of the dynamic analysis",default=False))
        self.attributes.append(BlueprintAttribute("dynamicLoads","sima/riflex/DynamicLoads","",True))