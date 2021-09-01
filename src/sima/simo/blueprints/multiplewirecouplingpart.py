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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("endPoint","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(Attribute("ea","number","Wire cross section stiffness",default=0.0))
        self.attributes.append(Attribute("length","number","Initial, unstretched wire length",default=0.0))
        self.attributes.append(Attribute("damping","number","Material damping",default=0.0))
        self.attributes.append(Attribute("flexibility","number","Connection flexibility",default=0.0))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/FailureMode","Failure mode of coupling element"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))