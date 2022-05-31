# 
# Generated with WamitCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WamitCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WamitCalculationParameters", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("solveRadiationProblem","sima/wamit/YesNoOption","IRAD"))
        self.attributes.append(EnumAttribute("solveDiffractionProblem","sima/wamit/PotenProblemOption","IDIFF"))
        self.attributes.append(EnumAttribute("calculateAddedMassAndDampingCoefficients","sima/wamit/YesNoOption","Corresponds to IOPTN(1)"))
        self.attributes.append(EnumAttribute("calculateExcitingForcesFromHaskindRelations","sima/wamit/CalculateExcitingForcesOption","Corresponds to IOPTN(2)"))
        self.attributes.append(EnumAttribute("calculateExcitingForcesFromDiffractionPotential","sima/wamit/CalculateExcitingForcesOption","Corresponds to IOPTN(3)"))
        self.attributes.append(EnumAttribute("calculateResponseAmplitudeOperator","sima/wamit/CalculateResponseAmplitudeOperatorOption","Corresponds to IOPTN(4)"))
        self.attributes.append(EnumAttribute("useMomentumIntegration","sima/wamit/CalculateMeanForceAndMomentIntegrationOption","Corresponds to IOPTN(8)"))
        self.attributes.append(EnumAttribute("usePressureIntegration","sima/wamit/CalculateMeanForceAndMomentIntegrationOption","Corresponds to IOPTN(9)"))
        self.attributes.append(BlueprintAttribute("pointField","sima/wamit/PointField","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("useControlSurfaceIntegration","sima/wamit/CalculateMeanForceAndMomentIntegrationOption","Corresponds to IOPTN(7)"))
        self.attributes.append(EnumAttribute("methodForSolvingLinearSystems","sima/wamit/LinearSystemSolvingMethod","ISOLVE"))
        self.attributes.append(Attribute("numberOfBlocksInBlockIterativeSolver","integer","",default=2))
        self.attributes.append(EnumAttribute("geometryMethod","sima/wamit/GeometryOrderOption","ILOWHI"))
        self.attributes.append(EnumAttribute("integrateLogarithmicSingularitySeparately","sima/wamit/YesNoOption","ILOG"))
        self.attributes.append(Attribute("panelSize","number","",default=10.0))
        self.attributes.append(EnumAttribute("evaluateSourceStrength","sima/wamit/YesNoOption","ISOR"))
        self.attributes.append(EnumAttribute("calculationOfDiffractionPotential","sima/wamit/DiffractionPotentailOption","ISCATT"))
        self.attributes.append(BlueprintAttribute("fieldPoints","sima/sima/Point3","",True,Dimension("*")))
        self.attributes.append(Attribute("useInfiniteWaterDepth","boolean","HBOT",default=True))
        self.attributes.append(Attribute("maximumNumberOfIterations","integer","The maximum number of iterations when using an iterative solver",default=35))
        self.attributes.append(Attribute("maxNumOfIterationsAdaptiveIntegrationMomentum","integer","",default=8))
        self.attributes.append(Attribute("generateReport","boolean","",default=False))
        self.attributes.append(Attribute("briefOverviewOfTheory","boolean","",default=False))
        self.attributes.append(Attribute("taskDescription","boolean","",default=False))
        self.attributes.append(Attribute("wavePeriodsAndHeadings","boolean","",default=False))
        self.attributes.append(Attribute("calculationParameters","boolean","",default=False))
        self.attributes.append(Attribute("hydrostaticResults","boolean","",default=False))
        self.attributes.append(Attribute("structuralMass","boolean","",default=False))
        self.attributes.append(Attribute("externalStiffnessMatrix","boolean","",default=False))
        self.attributes.append(Attribute("linearDampingMatrix","boolean","",default=False))
        self.attributes.append(Attribute("firstOrderMotionTransferFunction","boolean","",default=False))
        self.attributes.append(Attribute("firstOrderWaveForceTransferFunctionDiffraction","boolean","",default=False))
        self.attributes.append(Attribute("firstOrderWaveForceTransferFunctionHaskind","boolean","",default=False))
        self.attributes.append(Attribute("addedMassZeroFrequency","boolean","",default=False))
        self.attributes.append(Attribute("addedMassInfiniteFrequency","boolean","",default=False))
        self.attributes.append(Attribute("frequencyDependentAddedMass","boolean","",default=False))
        self.attributes.append(Attribute("frequencyDependentDamping","boolean","",default=False))
        self.attributes.append(Attribute("diffractedWaveField","boolean","",default=False))
        self.attributes.append(Attribute("waveDriftForcePressure","boolean","",default=False))
        self.attributes.append(Attribute("waveDriftForceMomentum","boolean","",default=False))
        self.attributes.append(Attribute("waveDriftForceControlSurfaceIntegration","boolean","",default=False))
        self.attributes.append(Attribute("runPotenOnceInConditionSetsAndSpaces","boolean","This will make WAMIT run POTEN for one condition only, and copy that result and only run FORCE on the the rest of the conditions.",default=False))
        self.attributes.append(Attribute("ignoreExitCode","boolean","Ignore process exit code. Be careful to check the result when checked",default=False))