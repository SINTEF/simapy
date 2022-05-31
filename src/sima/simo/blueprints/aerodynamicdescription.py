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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("quadraticLongitudinalDrag","number","Quadratic longitudinal drag coefficient",default=0.0))
        self.attributes.append(Attribute("quadraticTransverseY","number","Quadratic transverse (Y) drag coefficient",default=0.0))
        self.attributes.append(Attribute("quadraticTransverseZ","number","Quadratic transverse (Z) drag coefficient",default=0.0))
        self.attributes.append(EnumAttribute("aerodynamicType","sima/simo/AerodynamicDescriptionType","Type of aerodynamic forces"))