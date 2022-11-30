# 
# Generated with MultipleWireCouplingPartBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class MultipleWireCouplingPartBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="MultipleWireCouplingPart", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("endPoint","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(Attribute("ea","number","Wire cross section stiffness",default=0.0))
        self.add_attribute(Attribute("length","number","Initial, unstretched wire length",default=0.0))
        self.add_attribute(Attribute("damping","number","Material damping",default=0.0))
        self.add_attribute(Attribute("flexibility","number","Connection flexibility",default=0.0))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/FailureMode","Failure mode of coupling element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))