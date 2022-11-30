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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("runStaticAutomatically","boolean","Run Static calculation automatically each time the model changes",default=False))
        self.add_attribute(Attribute("calculateEquilibrium","boolean","Perform equlibrium calculation",default=True))
        self.add_attribute(Attribute("maxPeriod","number","Maximum natural period",default=10.0))
        self.add_attribute(Attribute("posTol","number","Position tolerance",default=0.1))
        self.add_attribute(Attribute("dirTol","number","Direction tolerance",default=0.1))
        self.add_attribute(Attribute("timeStep","number","Equilibrium time step",default=0.01))
        self.add_attribute(Attribute("maxStep","integer","Maximum number of time steps",default=10000))
        self.add_attribute(Attribute("criticalDamping","boolean","Add critical damping?",default=True))
        self.add_attribute(Attribute("writeVisFile","boolean","write visualization file?",default=True))
        self.add_attribute(Attribute("calculateEigenvalues","boolean","Perform eigenvalue calculation",default=False))
        self.add_attribute(BlueprintAttribute("eliminations","sima/simo/DOFElimination","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("eigenvalueItems","sima/simo/BodyEigenvalueItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("equilibriumCalculationMethod","sima/simo/EquilibriumCalculationOption",""))
        self.add_attribute(Attribute("forceTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=100.0))
        self.add_attribute(Attribute("momentTolerance","number","An equilibrium will be accepted if all the force components are lower than the force tolerance, and all the moment components are lower than the moment tolerance.",default=1000.0))
        self.add_attribute(BlueprintAttribute("staticEquilibriumBody","sima/simo/StaticEquilibriumBody","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("restrainFromGlobalDOFBodies","sima/simo/DOFElimination","",True,Dimension("*")))
        self.add_attribute(Attribute("multipleEquilibriumCalculations","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("equilibriumGridDefinition","sima/simo/EquilibriumGridDefinition","",True))
        self.add_attribute(Attribute("requireSuccessfulCalculation","boolean","When checked, static calculation will fail if no equilibrium position is found",default=True))