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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.add_attribute(Attribute("ea","number","Wire cross section stiffness",default=0.0))
        self.add_attribute(Attribute("length","number","Initial, unstretched wire length",default=0.0))
        self.add_attribute(Attribute("damping","number","Material damping",default=0.0))
        self.add_attribute(Attribute("flexibility","number","Connection flexibility",default=0.0))
        self.add_attribute(BlueprintAttribute("guidePointSpecifications","sima/simo/GuidePointSpecification","",True,Dimension("*")))
        self.add_attribute(Attribute("constantTensionControl","boolean","Enable constant tension control for this wire",default=False))
        self.add_attribute(Attribute("tensionLevel","number","Desired tension level",default=0.0))
        self.add_attribute(Attribute("tensionDeadband","number","Tension level deadband",default=0.0))
        self.add_attribute(Attribute("maxSpeed","number","Max wire length rate of change",default=0.0))
        self.add_attribute(Attribute("activationTime","number","Activation time for constant tension control",default=0.0))
        self.add_attribute(Attribute("deactivationTime","number","Deactivation time for constant tension control. If value is less then or equal to activation time, controller will remain active throughout simulation",default=0.0))