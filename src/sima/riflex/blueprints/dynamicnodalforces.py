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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("_type","sima/riflex/ForceSpecificationType","Type of force specification"))
        self.attributes.append(Attribute("fileName","string","File name for time series of force components\n\nNTDFO: : Number of time instants (given once) \nMDCOMP TIMDFO: Number of load components and \ntime instant for the given loads\nRLMAG:  Magnitude of load component (MDCOMP lines)\n\nThe block {MDCOMP TIMDFO RLMAG} must be given for \neach time instant. \n",default=""))
        self.attributes.append(BlueprintAttribute("items","sima/riflex/DynamicNodalForceItem","",True,Dimension("size","")))