# 
# Generated with DynamicNodalForcesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynamicNodalForcesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynamicNodalForces", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/riflex/ForceSpecificationType","Type of force specification"))
        self.add_attribute(Attribute("fileName","string","File name for time series of force components\n\nNTDFO: : Number of time instants (given once) \nMDCOMP TIMDFO: Number of load components and \ntime instant for the given loads\nRLMAG:  Magnitude of load component (MDCOMP lines)\n\nThe block {MDCOMP TIMDFO RLMAG} must be given for \neach time instant. \n"))
        self.add_attribute(BlueprintAttribute("items","sima/riflex/DynamicNodalForceItem","",True,Dimension("*")))