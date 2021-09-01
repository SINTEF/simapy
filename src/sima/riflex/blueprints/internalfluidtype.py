# 
# Generated with InternalFluidTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class InternalFluidTypeBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="InternalFluidType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("density","number","Density",default=0.0))
        self.attributes.append(Attribute("volumeVelocity","number","Volume velocity",default=0.0))
        self.attributes.append(Attribute("inletPressure","number","Pressure at fluid inlet end",default=0.0))
        self.attributes.append(Attribute("pressureDrop","number","Pressure drop",default=0.0))
        self.attributes.append(EnumAttribute("flowInlet","sima/riflex/End","Flow direction code."))