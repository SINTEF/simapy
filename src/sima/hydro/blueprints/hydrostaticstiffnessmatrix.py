# 
# Generated with HydrostaticStiffnessMatrixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .matrix6 import Matrix6Blueprint

class HydrostaticStiffnessMatrixBlueprint(Matrix6Blueprint):
    """"""

    def __init__(self, name="HydrostaticStiffnessMatrix", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("values","number","",Dimension("*"),default=0.0))