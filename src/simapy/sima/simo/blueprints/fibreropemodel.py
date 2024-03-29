# 
# Generated with FibreRopeModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.namedobject import NamedObjectBlueprint

class FibreRopeModelBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="FibreRopeModel", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("originalCurve","sima/simo/AxialStiffnessItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("originalWorkingCurve","sima/simo/AxialStiffnessItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("workingCurve","sima/simo/AxialStiffnessItem","",True,Dimension("*")))
        self.add_attribute(Attribute("dynamicStiffnessCoefficientA","number","",default=0.0))
        self.add_attribute(Attribute("dynamicStiffnessCoefficientB","number","",default=0.0))