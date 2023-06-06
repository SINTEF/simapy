# 
# Generated with ControllerFederateBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlafederate import HLAFederateBlueprint

class ControllerFederateBlueprint(HLAFederateBlueprint):
    """"""

    def __init__(self, name="ControllerFederate", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("timeStep","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("allHLAControlConfigurations","sima/hla/HLAControlConfiguration","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("winchGroups","sima/hla/HLAWinchGroup","",True,Dimension("*")))