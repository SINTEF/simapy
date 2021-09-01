# 
# Generated with FibreRopeModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class FibreRopeModelBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="FibreRopeModel", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("originalCurve","sima/simo/AxialStiffnessItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("originalWorkingCurve","sima/simo/AxialStiffnessItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("workingCurve","sima/simo/AxialStiffnessItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("dynamicStiffnessCoefficientA","number","",default=0.0))
        self.attributes.append(Attribute("dynamicStiffnessCoefficientB","number","",default=0.0))