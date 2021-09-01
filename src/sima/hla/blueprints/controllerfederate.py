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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("timeStep","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("allHLAControlConfigurations","sima/hla/HLAControlConfiguration","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("winchGroups","sima/hla/HLAWinchGroup","",True,Dimension("size","")))