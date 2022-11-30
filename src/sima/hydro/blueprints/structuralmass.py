# 
# Generated with StructuralMassBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StructuralMassBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StructuralMass", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("mass","number","Mass",default=0.0))
        self.add_attribute(Attribute("ixx","number","Mass moment of inertia about origin",default=0.0))
        self.add_attribute(Attribute("iyx","number","Mass moment of inertia about origin",default=0.0))
        self.add_attribute(Attribute("iyy","number","Mass moment of inertia about origin",default=0.0))
        self.add_attribute(Attribute("izx","number","Mass moment of inertia about origin",default=0.0))
        self.add_attribute(Attribute("izy","number","Mass moment of inertia about origin",default=0.0))
        self.add_attribute(Attribute("izz","number","Mass moment of inertia about origin",default=0.0))
        self.add_attribute(BlueprintAttribute("cog","sima/sima/Point3","Coordinates of centre of gravity, (L)",True))