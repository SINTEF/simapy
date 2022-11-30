# 
# Generated with SIMOHeaveCompensatorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class SIMOHeaveCompensatorBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="SIMOHeaveCompensator", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("_type","sima/simo/CompensatorType",""))
        self.add_attribute(EnumAttribute("limitationMode","sima/simo/CompensatorLimitation","Limitation handling mode for the compensator"))
        self.add_attribute(Attribute("factor","number","Reduction factor for compensator action at high sea states",default=0.0))
        self.add_attribute(Attribute("clippingLevel","number","Clipping level for crane motion measurement",default=0.0))
        self.add_attribute(Attribute("numWiresCylinder","integer","Number of wire parts around compensator cylinder",default=2))
        self.add_attribute(Attribute("strokeLength","number","Maximum range of elongation (stroke length)",default=0.0))
        self.add_attribute(Attribute("cylinderArea","number","Cylinder cross section area",default=0.0))
        self.add_attribute(Attribute("feedbackGainFactor","number","Gain factor in feedback",default=0.0))
        self.add_attribute(Attribute("feedbackTimeDerivative","number","Time derivative in feedback",default=0.0))
        self.add_attribute(Attribute("feedforwardGainFactor","number","Gain factor in feedforward",default=0.0))
        self.add_attribute(Attribute("feedforwardTimeDerivative","number","Time derivative in feedforward",default=0.0))
        self.add_attribute(Attribute("valveCharacteristics","number","Characteristics of valve",default=0.0))
        self.add_attribute(Attribute("valveTimeConstant","number","Valve time constant",default=0.0))
        self.add_attribute(Attribute("lowPassTimeConstant","number","Time constant in low-pass filter",default=0.0))
        self.add_attribute(Attribute("numWiresTopHook","integer","Number of wire parts from crane top to hook",default=1))