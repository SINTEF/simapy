# 
# Generated with RegularLineTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .arlinetype import ARLineTypeBlueprint

class RegularLineTypeBlueprint(ARLineTypeBlueprint):
    """"""

    def __init__(self, name="RegularLineType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("internalFluid","sima/riflex/InternalFluidType","Internal fluid component type.",False))
        self.attributes.append(BlueprintAttribute("endComponent","sima/riflex/NodalComponentType","Nodal component type number for attached body or connector at end 2 of rthe last segment.",False))
        self.attributes.append(BlueprintAttribute("segments","sima/riflex/RegularSegment","",True,Dimension("size","")))