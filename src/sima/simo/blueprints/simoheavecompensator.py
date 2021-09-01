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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("_type","sima/simo/CompensatorType",""))
        self.attributes.append(EnumAttribute("limitationMode","sima/simo/CompensatorLimitation","Limitation handling mode for the compensator"))
        self.attributes.append(Attribute("factor","number","Reduction factor for compensator action at high sea states",default=0.0))
        self.attributes.append(Attribute("clippingLevel","number","Clipping level for crane motion measurement",default=0.0))
        self.attributes.append(Attribute("numWiresCylinder","integer","Number of wire parts around compensator cylinder",default=2))
        self.attributes.append(Attribute("strokeLength","number","Maximum range of elongation (stroke length)",default=0.0))
        self.attributes.append(Attribute("cylinderArea","number","Cylinder cross section area",default=0.0))
        self.attributes.append(Attribute("feedbackGainFactor","number","Gain factor in feedback",default=0.0))
        self.attributes.append(Attribute("feedbackTimeDerivative","number","Time derivative in feedback",default=0.0))
        self.attributes.append(Attribute("feedforwardGainFactor","number","Gain factor in feedforward",default=0.0))
        self.attributes.append(Attribute("feedforwardTimeDerivative","number","Time derivative in feedforward",default=0.0))
        self.attributes.append(Attribute("valveCharacteristics","number","Characteristics of valve",default=0.0))
        self.attributes.append(Attribute("valveTimeConstant","number","Valve time constant",default=0.0))
        self.attributes.append(Attribute("lowPassTimeConstant","number","Time constant in low-pass filter",default=0.0))
        self.attributes.append(Attribute("numWiresTopHook","integer","Number of wire parts from crane top to hook",default=1))