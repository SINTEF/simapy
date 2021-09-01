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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("mass","number","Mass",default=0.0))
        self.attributes.append(Attribute("ixx","number","Mass moment of inertia about origin",default=0.0))
        self.attributes.append(Attribute("iyx","number","Mass moment of inertia about origin",default=0.0))
        self.attributes.append(Attribute("iyy","number","Mass moment of inertia about origin",default=0.0))
        self.attributes.append(Attribute("izx","number","Mass moment of inertia about origin",default=0.0))
        self.attributes.append(Attribute("izy","number","Mass moment of inertia about origin",default=0.0))
        self.attributes.append(Attribute("izz","number","Mass moment of inertia about origin",default=0.0))
        self.attributes.append(BlueprintAttribute("cog","sima/sima/Point3","Coordinates of centre of gravity, (L)",True))