# 
# Generated with GeneralCrossSectionStiffnessDampingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class GeneralCrossSectionStiffnessDampingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GeneralCrossSectionStiffnessDamping", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("axialFactor","number","Factor for stiffness proportional damping in axial dof",default=0.0))
        self.add_attribute(Attribute("torsionalFactor","number","Factor for stiffness proportional damping in torsional dof",default=0.0))
        self.add_attribute(Attribute("bendingFactorV","number","Factor for stiffness proportional damping for bending around principal V-axis and shear in principal W-axis",default=0.0))
        self.add_attribute(Attribute("bendingFactorW","number","Factor for stiffness proportional damping for bending around principal W-axis and shear in principal V-axis",default=0.0))