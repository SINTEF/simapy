# 
# Generated with TimeDomainProcedureBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TimeDomainProcedureBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TimeDomainProcedure", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("method","sima/riflex/MethodIndicator","Method indicator"))
        self.add_attribute(EnumAttribute("procedure","sima/riflex/ProcedureIndicator","Procedure indicator"))
        self.add_attribute(Attribute("displacementStorage","boolean","Displacement storage indicator",default=False))
        self.add_attribute(Attribute("forceResultStorage","boolean","Force response storage indicator",default=False))
        self.add_attribute(Attribute("sumForceResponseStorage","boolean","Sum force response storage indicator",default=False))
        self.add_attribute(Attribute("curvatureResponseStorage","boolean","Curvature response storage indicator",default=False))
        self.add_attribute(Attribute("envelopeCurveSpecification","boolean","Envelope curve specification indicator",default=False))
        self.add_attribute(Attribute("inverseBeta","number","Inverse value of the beta-parameter.",default=4.0))
        self.add_attribute(Attribute("gamma","number","Value of the parameter gamma of the Newmark operators (usually equal to 0.5)",default=0.5))
        self.add_attribute(Attribute("theta","number","Value of the parameter theta in Wilson`s integration method",default=1.0))
        self.add_attribute(EnumAttribute("dampingOption","sima/riflex/RayleighDamping","Stiffness proportional damping options"))
        self.add_attribute(Attribute("globalMassDampingFactor","number","Global mass proportional damping factor",default=0.0))
        self.add_attribute(Attribute("globalStiffnessDampingFactor","number","Global stiffness proportional damping factor",default=0.0))
        self.add_attribute(Attribute("localMassTensionDamping","number","Local mass proportional damping factor for tension",default=0.0))
        self.add_attribute(Attribute("localMassTorsionDamping","number","Local mass proportional damping factor for torsion",default=0.0))
        self.add_attribute(Attribute("localMassBendingDamping","number","Local mass proportional damping factor for bending",default=0.0))
        self.add_attribute(Attribute("localStiffnessTensionDamping","number","Local stiffness proportional damping factor for tension",default=0.0))
        self.add_attribute(Attribute("localStiffnessTorsionDamping","number","Local stiffness proportional damping factor for torsion",default=0.0))
        self.add_attribute(Attribute("localStiffnessBendingDamping","number","Local stiffness proportional damping factor for bending",default=0.0))
        self.add_attribute(BlueprintAttribute("nonLinearForceModel","sima/riflex/NonLinearForceModel","",True))
        self.add_attribute(BlueprintAttribute("nonLinearIntegrationProcedure","sima/riflex/NonLinearIntegrationProcedure","",True))