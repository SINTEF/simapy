# 
# Generated with CoupledAxialTorsionStrainItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .axialstiffnessitem import AxialStiffnessItemBlueprint
from .torsionstiffnessitem import TorsionStiffnessItemBlueprint

class CoupledAxialTorsionStrainItemBlueprint(AxialStiffnessItemBlueprint,TorsionStiffnessItemBlueprint):
    """"""

    def __init__(self, name="CoupledAxialTorsionStrainItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("axialForce","number","Axial force corresponding to relative elongation.",default=0.0))
        self.add_attribute(Attribute("relativeElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("torsionMoment","number","Torsion moment",default=0.0))
        self.add_attribute(Attribute("torsionAngle","number","Torsion angle/length",default=0.0))
        self.add_attribute(Attribute("tensionTorsionCoupling","number"," Tension/torsion coupling parameter",default=0.0))