# 
# Generated with SIMOStaticCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SIMOStaticCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIMOStaticCalculationParameters", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("runStaticAutomatically","boolean","Run Static calculation automatically each time the model changes",default=False))
        self.attributes.append(Attribute("calculateEquilibrium","boolean","Perform equlibrium calculation",default=True))
        self.attributes.append(Attribute("maxPeriod","number","Maximum natural period",default=10.0))
        self.attributes.append(Attribute("posTol","number","Position tolerance",default=0.1))
        self.attributes.append(Attribute("dirTol","number","Direction tolerance",default=0.1))
        self.attributes.append(Attribute("timeStep","number","Equilibrium time step",default=0.01))
        self.attributes.append(Attribute("maxStep","integer","Maximum number of time steps",default=10000))
        self.attributes.append(Attribute("criticalDamping","boolean","Add critical damping?",default=True))
        self.attributes.append(Attribute("writeVisFile","boolean","write visualization file?",default=True))
        self.attributes.append(Attribute("calculateEigenvalues","boolean","Perform eigenvalue calculation",default=False))
        self.attributes.append(BlueprintAttribute("eliminations","sima/simo/DOFElimination","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("eigenvalueItems","sima/simo/BodyEigenvalueItem","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("equilibriumCalculationMethod","sima/simo/EquilibriumCalculationOption",""))
        self.attributes.append(Attribute("forceTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=100.0))
        self.attributes.append(Attribute("momentTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=1000.0))
        self.attributes.append(BlueprintAttribute("staticEquilibriumBody","sima/simo/StaticEquilibriumBody","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("restrainFromGlobalDOFBodies","sima/simo/DOFElimination","",True,Dimension("*")))
        self.attributes.append(Attribute("multipleEquilibriumCalculations","boolean","",default=False))
        self.attributes.append(BlueprintAttribute("equilibriumGridDefinition","sima/simo/EquilibriumGridDefinition","",True))
        self.attributes.append(Attribute("requireSuccessfulCalculation","boolean","When checked, static calculation will fail if no equilibrium position is found",default=True))