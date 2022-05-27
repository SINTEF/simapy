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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("method","sima/riflex/MethodIndicator","Method indicator"))
        self.attributes.append(EnumAttribute("procedure","sima/riflex/ProcedureIndicator","Procedure indicator"))
        self.attributes.append(Attribute("displacementStorage","boolean","Displacement storage indicator",default=False))
        self.attributes.append(Attribute("forceResultStorage","boolean","Force response storage indicator",default=False))
        self.attributes.append(Attribute("sumForceResponseStorage","boolean","Sum force response storage indicator",default=False))
        self.attributes.append(Attribute("curvatureResponseStorage","boolean","Curvature response storage indicator",default=False))
        self.attributes.append(Attribute("envelopeCurveSpecification","boolean","Envelope curve specification indicator",default=False))
        self.attributes.append(Attribute("inverseBeta","number","Inverse value of the beta-parameter.",default=4.0))
        self.attributes.append(Attribute("gamma","number","Value of the parameter gamma of the Newmark operators (usually equal to 0.5)",default=0.5))
        self.attributes.append(Attribute("theta","number","Value of the parameter theta in Wilson`s integration method",default=1.0))
        self.attributes.append(EnumAttribute("dampingOption","sima/riflex/RayleighDamping","Stiffness proportional damping options"))
        self.attributes.append(Attribute("globalMassDampingFactor","number","Global mass proportional damping factor",default=0.0))
        self.attributes.append(Attribute("globalStiffnessDampingFactor","number","Global stiffness proportional damping factor",default=0.0))
        self.attributes.append(Attribute("localMassTensionDamping","number","Local mass proportional damping factor for tension",default=0.0))
        self.attributes.append(Attribute("localMassTorsionDamping","number","Local mass proportional damping factor for torsion",default=0.0))
        self.attributes.append(Attribute("localMassBendingDamping","number","Local mass proportional damping factor for bending",default=0.0))
        self.attributes.append(Attribute("localStiffnessTensionDamping","number","Local stiffness proportional damping factor for tension",default=0.0))
        self.attributes.append(Attribute("localStiffnessTorsionDamping","number","Local stiffness proportional damping factor for torsion",default=0.0))
        self.attributes.append(Attribute("localStiffnessBendingDamping","number","Local stiffness proportional damping factor for bending",default=0.0))
        self.attributes.append(BlueprintAttribute("nonLinearForceModel","sima/riflex/NonLinearForceModel","",True))
        self.attributes.append(BlueprintAttribute("nonLinearIntegrationProcedure","sima/riflex/NonLinearIntegrationProcedure","",True))