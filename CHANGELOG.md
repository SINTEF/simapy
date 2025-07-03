# Changelog

All notable changes to this project will be documented in this file.

## [5.0.0]

- Updated data model to reflect SIMA 5.0.0
- Added default progress handler

Model changes per package:

### Package simo

Added:
 - Field SIMODynamicCalculationParameters.storeDifferenceFrequencyWaveForce
 - Field SIMOBody.differenceFrequencyQtf
 - Field SIMOBody.sumFrequencyQtf

Changed:
 - Field SIMOBody.qtf is split into two fields: differenceFrequencyQtf and sumFrequencyQtf

Removed:
 - Enum NonlinearBuoyancyCorrectionMethod
 - Class NonlinearBuoyancyCorrection
 - Field SIMOBody.nonlinearBuoyancyCorrection

### Package riflex

Added:
 - Class DNV_OS_E301CapacityCheck
 - Enum UtilizationCheck
 - Enum EndReference
 - Class WindVelocityRamping
 - Class TnFatigueAnalysisItem
 - Class TensionAndCurvatureCapacityCheck
 - Enum TypeOfUnit
 - Class MarineGrowthScaling
 - Field DynamicLoads.windVelocityRamping
 - Field RIFLEXModel.capacityChecks
 - Field EnvelopeCurveSpecification.storeDisplacement
 - Field EnvelopeCurveSpecification.storeCurvature
 - Field EnvelopeCurveSpecification.storeForce
 - Field ARLine.localElementAxes
 - Field ParameterVariation.deactivateCurrent
 - Field StaticLoadTypeItem.marineGrowthScalings
 - Field FatigueAnalysis.tnItems
 - Field RIFLEXStaticCalculationParameters.automaticLoading
 - Field HorizontalAxisController.pitchControl
 - Field HorizontalAxisController.accelerationFromDisplacement
 - Field UserdefinedElement.elementEnd
 - Option MatrixStorage.Automatic

Changed:
 - Field SlenderSystem.localElementAxes is moved to the referenced Line
 - Field EnvelopeCurveSpecification.compDisplacement is renamed to storeDisplacement
 - Field EnvelopeCurveSpecification.compForce is renamed to storeForce
 - Field EnvelopeCurveSpecification.compCurvature is renamed to storeCurvature

Removed:
 - Field EnvelopeCurveSpecification.printForce
 - Field EnvelopeCurveSpecification.printDisplacement
 - Field EnvelopeCurveSpecification.printCurvature

### Package environment

Added:
 - Class RegularCurrentFromFile
 - Field FluctuatingThreeComponent.reverseBox

Removed:
 - Wave.environment
 - Wind.environment
 - Current.environment

### Package hydro

Added:
 - Enum WamitQtfImportOption
 - Enum WamitWaveForceOption
 - Enum WamitWaveDriftForceOption
 - Class RetardationFunctionCalculationParameters
 - Class LinearHydrostatics
 - Class WamitImportConfiguration
 - Enum QtfInput
 - Class HydrostaticStiffnessMatrixData
 - Field DifferenceFrequencyQTF.bodyNumber
 - Field DifferenceFrequencyQTF.input
 - Field DifferenceFrequencyQTF.file
 - Field DifferenceFrequencyQTF.symmetry

Changed:
 - HydrostaticStiffnessData is renamed to HydrostaticStiffnessMatrixData

Removed:
 - Option DirectionSymmetry.X0_SYMMETRY

### Package windturbine

Added:
 - Enum PitchControl
 - Field HorizontalAxisWindTurbineController.pitchControl
 - Field HorizontalAxisWindTurbineController.accelerationFromDisplacement


### Package command

Added:
 - Field ImportCommand.configuration
 - Field ConditionRunCommand.destination
 - Field ConditionRunCommand.paths
 - Field ConditionRunCommand.copy


## [4.8.0]

- Updated data model to reflect SIMA 4.8.0

Model changes per package:

### Package riflex

Added:
 - Class BottomContactStorage
 - Enum ConstructionType
 - Class GeneralCrossSectionStiffnessDamping
 - Class ChainCrossSection
 - Class DoubleSymmetricStiffnessDamping
 - Class BottomContactForceStorage
 - Class TouchDownPointStorage
 - Enum SteelGrade
 - Field WindTurbine.skewedWake
 - Field WindTurbine.skewedWakeFactor
 - Field HorizontalAxisController.generatorEfficiency
 - Field RIFLEXDynamicCalculationParameters.bottomContactStorage

Changed:
 - Field DoubleSymmetricStiffnessDamping.bendingFactor renamed to bendingFactorY
 - Field GeneralCrossSectionStiffnessDamping.bendingFactor renamed to bendingFactorV
 - Field GeotechnicalSpring.strainVelocityExponent renamed to velocityExponent
 - Field ForceResponseStorage.storeBottomContactForces moved to BottomContactStorage

Removed:
 - Field GeneralCrossSectionStiffnessDamping.option
 - Field GeotechnicalSpring.relativeLength
 - Field VonMisesCombinedLoading.percentile
 - Field DNV_OS_F201CombinedLoading.percentile
 - Field ISO_13628_7CombinedLoading.percentile
 - Field RIFLEXTask.exportAsFMU


### Package simo

Added:
 - Class ExternalPythonForce
 - Class BallastTankPressureMeasurement
 - Class SIMOStaticResultStorageParameters
 - Field SIMOStaticCalculationParameters.storageParameters
 - Field StringDoubleItem.unit
 - Field BallastTank.pressureMeasurements
 - Field SIMOBody.externalPythonForces

Removed:
 - Class ExternalHLAForce
 - Field ExternalDLLForce.body
 - Field ExternalForceFromFile.body
 - Field CatenaryLine.xwinch 
 - Field SIMOTask.exportAsFMU
 - Field SIMOBody.externalHLAForces

### Package windturbine

Added:
 - Field HorizontalAxisWindTurbineController.generatorEfficiency

### Package environment

Added:
 - Field NumericalWave.file
 - Field NumericalWave.fromFile
 - Field ESDUWind.profileExponent


### Package sima

Added:
 - Class StringValue
 - Class IntValue
 - Class ValueRoot
 - Class SingleValue
 - Class NumberValue
 - Class CSVResult
 - Class Value
 - Class ValueContainer
 - Enum literal LengthUnit.MILLIMETER

Removed 
 - Class MOAOFolder
 - Field ScriptingPreference.showScripts

### Package command

Added:
 - Field ExportBlueprintCommand.delete

Removed:
 - Field ExportBlueprintCommand.versions


### Package workflow

Added:
 - Class PythonProgramNode
 - Field FileOutputNode.directModelExport

### Package post

Added:
 - Class SignalFilterSetup
 - Class OutputPlot
 - Enum Filtering
 - Field FileOutput.directModelExport


### Package report

Added:
 - Class SectionContent

Removed:

 - Class Formula
 - Class Linkable
 - Field Table.autoSplit
 - Field Plot.mergeSeries
 - Field Section.identifier
 - Field Appendix.identifier
 - Field Linkable.identifier


## [4.6.0]

### Added

- Updated data model to reflect SIMA 4.6.0
- New metocean package to enable creation of SIMA metocean data

### Changed

- Breaking changes:
    - sima root package is moved into simapy
    - marmo package is renamed and moved into simapy.sima.signals
    - sima module renamed to sre

### Fixed

- Fixed copy of cross references. Possibility to remove or keep (default) uncontained cross references when copying
