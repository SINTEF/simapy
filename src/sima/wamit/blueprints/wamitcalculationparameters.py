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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("solveRadiationProblem","sima/wamit/YesNoOption","IRAD"))
        self.add_attribute(EnumAttribute("solveDiffractionProblem","sima/wamit/PotenProblemOption","IDIFF"))
        self.add_attribute(EnumAttribute("calculateAddedMassAndDampingCoefficients","sima/wamit/YesNoOption","Corresponds to IOPTN(1)"))
        self.add_attribute(EnumAttribute("calculateExcitingForcesFromHaskindRelations","sima/wamit/CalculateExcitingForcesOption","Corresponds to IOPTN(2)"))
        self.add_attribute(EnumAttribute("calculateExcitingForcesFromDiffractionPotential","sima/wamit/CalculateExcitingForcesOption","Corresponds to IOPTN(3)"))
        self.add_attribute(EnumAttribute("calculateResponseAmplitudeOperator","sima/wamit/CalculateResponseAmplitudeOperatorOption","Corresponds to IOPTN(4)"))
        self.add_attribute(EnumAttribute("useMomentumIntegration","sima/wamit/CalculateMeanForceAndMomentIntegrationOption","Corresponds to IOPTN(8)"))
        self.add_attribute(EnumAttribute("usePressureIntegration","sima/wamit/CalculateMeanForceAndMomentIntegrationOption","Corresponds to IOPTN(9)"))
        self.add_attribute(BlueprintAttribute("pointField","sima/wamit/PointField","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("useControlSurfaceIntegration","sima/wamit/CalculateMeanForceAndMomentIntegrationOption","Corresponds to IOPTN(7)"))
        self.add_attribute(EnumAttribute("methodForSolvingLinearSystems","sima/wamit/LinearSystemSolvingMethod","ISOLVE"))
        self.add_attribute(Attribute("numberOfBlocksInBlockIterativeSolver","integer","",default=2))
        self.add_attribute(EnumAttribute("geometryMethod","sima/wamit/GeometryOrderOption","ILOWHI"))
        self.add_attribute(EnumAttribute("integrateLogarithmicSingularitySeparately","sima/wamit/YesNoOption","ILOG"))
        self.add_attribute(Attribute("panelSize","number","",default=10.0))
        self.add_attribute(EnumAttribute("evaluateSourceStrength","sima/wamit/YesNoOption","ISOR"))
        self.add_attribute(EnumAttribute("calculationOfDiffractionPotential","sima/wamit/DiffractionPotentailOption","ISCATT"))
        self.add_attribute(BlueprintAttribute("fieldPoints","sima/sima/Point3","",True,Dimension("*")))
        self.add_attribute(Attribute("useInfiniteWaterDepth","boolean","HBOT",default=True))
        self.add_attribute(Attribute("maximumNumberOfIterations","integer","The maximum number of iterations when using an iterative solver",default=35))
        self.add_attribute(Attribute("maxNumOfIterationsAdaptiveIntegrationMomentum","integer","",default=8))
        self.add_attribute(Attribute("generateReport","boolean","",default=False))
        self.add_attribute(Attribute("briefOverviewOfTheory","boolean","",default=False))
        self.add_attribute(Attribute("taskDescription","boolean","",default=False))
        self.add_attribute(Attribute("wavePeriodsAndHeadings","boolean","",default=False))
        self.add_attribute(Attribute("calculationParameters","boolean","",default=False))
        self.add_attribute(Attribute("hydrostaticResults","boolean","",default=False))
        self.add_attribute(Attribute("structuralMass","boolean","",default=False))
        self.add_attribute(Attribute("externalStiffnessMatrix","boolean","",default=False))
        self.add_attribute(Attribute("linearDampingMatrix","boolean","",default=False))
        self.add_attribute(Attribute("firstOrderMotionTransferFunction","boolean","",default=False))
        self.add_attribute(Attribute("firstOrderWaveForceTransferFunctionDiffraction","boolean","",default=False))
        self.add_attribute(Attribute("firstOrderWaveForceTransferFunctionHaskind","boolean","",default=False))
        self.add_attribute(Attribute("addedMassZeroFrequency","boolean","",default=False))
        self.add_attribute(Attribute("addedMassInfiniteFrequency","boolean","",default=False))
        self.add_attribute(Attribute("frequencyDependentAddedMass","boolean","",default=False))
        self.add_attribute(Attribute("frequencyDependentDamping","boolean","",default=False))
        self.add_attribute(Attribute("diffractedWaveField","boolean","",default=False))
        self.add_attribute(Attribute("waveDriftForcePressure","boolean","",default=False))
        self.add_attribute(Attribute("waveDriftForceMomentum","boolean","",default=False))
        self.add_attribute(Attribute("waveDriftForceControlSurfaceIntegration","boolean","",default=False))
        self.add_attribute(Attribute("runPotenOnceInConditionSetsAndSpaces","boolean","This will make WAMIT run POTEN for one condition only, and copy that result and only run FORCE on the the rest of the conditions.",default=False))
        self.add_attribute(Attribute("ignoreExitCode","boolean","Ignore process exit code. Be careful to check the result when checked",default=False))