# 
# Generated with CRSStiffnessDampingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CRSStiffnessDampingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CRSStiffnessDamping", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("axialFactor","number","Factor for stiffness proportional damping in axial dof",default=0.0))
        self.attributes.append(Attribute("torsionalFactor","number","Factor for stiffness proportional damping in torsional dof",default=0.0))
        self.attributes.append(Attribute("bendingFactor","number","Factor for stiffness proportional damping in bending dof",default=0.0))
        self.attributes.append(EnumAttribute("option","sima/riflex/RayleighDamping","Stiffness proportional damping options"))