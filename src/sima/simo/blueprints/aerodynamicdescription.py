# 
# Generated with AerodynamicDescriptionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AerodynamicDescriptionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AerodynamicDescription", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("quadraticLongitudinalDrag","number","Quadratic longitudinal drag coefficient",default=0.0))
        self.add_attribute(Attribute("quadraticTransverseY","number","Quadratic transverse (Y) drag coefficient",default=0.0))
        self.add_attribute(Attribute("quadraticTransverseZ","number","Quadratic transverse (Z) drag coefficient",default=0.0))
        self.add_attribute(EnumAttribute("aerodynamicType","sima/simo/AerodynamicDescriptionType","Type of aerodynamic forces"))