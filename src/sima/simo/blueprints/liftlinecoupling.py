# 
# Generated with LiftLineCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simplecoupling import SimpleCouplingBlueprint

class LiftLineCouplingBlueprint(SimpleCouplingBlueprint):
    """"""

    def __init__(self, name="LiftLineCoupling", package_path="sima/simo", description=""):
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
        self.attributes.append(Attribute("numElements","integer","Number of elements",default=0))
        self.attributes.append(Attribute("accIncluded","boolean","Flag for including acceleration of the line",default=True))
        self.attributes.append(Attribute("diameter","number","Segment diameter",default=0.0))
        self.attributes.append(Attribute("eMod","number","Modulus of elasticity",default=0.0))
        self.attributes.append(Attribute("emFac","integer","Factor of elasticity - 2 for chains - 1 for other segment types",default=1))
        self.attributes.append(Attribute("length","number","Initial, unstretched wire length",default=0.0))
        self.attributes.append(Attribute("flexibility","number","Connection flexibility",default=0.0))
        self.attributes.append(Attribute("damping","number","Material damping",default=0.0))
        self.attributes.append(Attribute("uwia","number","Unit weight in air",default=0.0))
        self.attributes.append(Attribute("watfac","number","The ratio of weight in water to weight in air",default=0.0))
        self.attributes.append(Attribute("transverseDrag","number","Transverse drag coefficient",default=0.0))
        self.attributes.append(Attribute("longitudinalDrag","number","Longitudinal drag coefficient",default=0.0))