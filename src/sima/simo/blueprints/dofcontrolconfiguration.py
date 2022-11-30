# 
# Generated with DOFControlConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DOFControlConfigurationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DOFControlConfiguration", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("dof","sima/simo/ControlDOF","Degree Of Freedom"))
        self.add_attribute(Attribute("mass","number","Total Mass",default=0.0))
        self.add_attribute(Attribute("drag","number","drag coefficient",default=0.0))
        self.add_attribute(Attribute("stiffness","number","Linear stiffness in global direction (not from DP system)",default=0.0))
        self.add_attribute(Attribute("naturalPeriod","number","Wanted natural period",default=100.0))
        self.add_attribute(Attribute("dampingFactor","number","Damping factors rel. to critical damping",default=0.7))
        self.add_attribute(Attribute("integrationTime","number","Integration time, small time means heavy use of integral effect \n(Discontinuity in 0, 0 means no integral effect)",default=0.0))
        self.add_attribute(Attribute("cutOffPeriod","number","Cut-off period for LP-filtering",default=0.0))
        self.add_attribute(Attribute("filterDampingFactor","number","Damping factors rel. to critical damping",default=0.0))
        self.add_attribute(Attribute("integralLF","number","Integral LF estimation gain:\n\n* LF_surge_integralgain=0.00001*mass_surge 	[N/m] (where the mass is in [kg])\n* LF_sway_integralgain=0.00001*mass_sway [N/m] (where the mass is in [kg])\n* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (where the mass is in [kg.m^2])\n* For Current bias estimation (see point 11), the default values are:\n* LF_surge_integralgain=0.0025 [1/s] \n* LF_sway_integralgain=0.0025 [1/s]\n* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (as for the force estimation)",default=0.0))
        self.add_attribute(Attribute("proportionalHF","number","Proportional HF estimation gain",default=0.1))
        self.add_attribute(Attribute("dampingOnly","boolean","Turn off proportional control and use damping only",default=False))