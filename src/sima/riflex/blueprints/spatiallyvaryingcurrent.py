# 
# Generated with SpatiallyVaryingCurrentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.environment.blueprints.current import CurrentBlueprint

class SpatiallyVaryingCurrentBlueprint(CurrentBlueprint):
    """"""

    def __init__(self, name="SpatiallyVaryingCurrent", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("profiles","sima/riflex/CurrentProfile","",True,Dimension("*")))