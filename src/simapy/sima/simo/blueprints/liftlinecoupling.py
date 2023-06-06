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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.add_attribute(Attribute("numElements","integer","Number of elements",default=0))
        self.add_attribute(Attribute("accIncluded","boolean","Flag for including acceleration of the line",default=False))
        self.add_attribute(Attribute("diameter","number","Segment diameter",default=0.0))
        self.add_attribute(Attribute("eMod","number","Modulus of elasticity",default=0.0))
        self.add_attribute(Attribute("emFac","integer","Factor of elasticity - 2 for chains - 1 for other segment types",default=1))
        self.add_attribute(Attribute("length","number","Initial, unstretched wire length",default=0.0))
        self.add_attribute(Attribute("flexibility","number","Connection flexibility",default=0.0))
        self.add_attribute(Attribute("damping","number","Material damping",default=0.0))
        self.add_attribute(Attribute("uwia","number","Unit weight in air",default=0.0))
        self.add_attribute(Attribute("watfac","number","The ratio of weight in water to weight in air",default=0.0))
        self.add_attribute(Attribute("transverseDrag","number","Transverse drag coefficient",default=0.0))
        self.add_attribute(Attribute("longitudinalDrag","number","Longitudinal drag coefficient",default=0.0))