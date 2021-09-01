# 
# Generated with SimpleWireCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simplecoupling import SimpleCouplingBlueprint

class SimpleWireCouplingBlueprint(SimpleCouplingBlueprint):
    """"""

    def __init__(self, name="SimpleWireCoupling", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.attributes.append(Attribute("ea","number","Wire cross section stiffness",default=0.0))
        self.attributes.append(Attribute("length","number","Initial, unstretched wire length",default=0.0))
        self.attributes.append(Attribute("damping","number","Material damping",default=0.0))
        self.attributes.append(Attribute("flexibility","number","Connection flexibility",default=0.0))
        self.attributes.append(BlueprintAttribute("guidePointSpecifications","sima/simo/GuidePointSpecification","",True,Dimension("size","")))
        self.attributes.append(Attribute("constantTensionControl","boolean","Enable constant tension control for this wire",default=True))
        self.attributes.append(Attribute("tensionLevel","number","Desired tension level",default=0.0))
        self.attributes.append(Attribute("tensionDeadband","number","Tension level deadband",default=0.0))
        self.attributes.append(Attribute("maxSpeed","number","Max wire length rate of change",default=0.0))
        self.attributes.append(Attribute("activationTime","number","Activation time for constant tension control",default=0.0))
        self.attributes.append(Attribute("deactivationTime","number","Deactivation time for constant tension control. If value is less then or equal to activation time, controller will remain active throughout simulation",default=0.0))