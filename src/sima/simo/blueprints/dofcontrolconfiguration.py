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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("dof","sima/simo/ControlDOF","Degree Of Freedom"))
        self.attributes.append(Attribute("mass","number","Total Mass",default=0.0))
        self.attributes.append(Attribute("drag","number","drag coefficient",default=0.0))
        self.attributes.append(Attribute("stiffness","number","Linear stiffness in global direction (not from DP system)",default=0.0))
        self.attributes.append(Attribute("naturalPeriod","number","Wanted natural period",default=100.0))
        self.attributes.append(Attribute("dampingFactor","number","Damping factors rel. to critical damping",default=0.7))
        self.attributes.append(Attribute("integrationTime","number","Integration time, small time means heavy use of integral effect \n(Discontinuity in 0, 0 means no integral effect)",default=0.0))
        self.attributes.append(Attribute("cutOffPeriod","number","Cut-off period for LP-filtering",default=0.0))
        self.attributes.append(Attribute("filterDampingFactor","number","Damping factors rel. to critical damping",default=0.0))
        self.attributes.append(Attribute("integralLF","number","Integral LF estimation gain:\n\n* LF_surge_integralgain=0.00001*mass_surge 	[N/m] (where the mass is in [kg])\n* LF_sway_integralgain=0.00001*mass_sway [N/m] (where the mass is in [kg])\n* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (where the mass is in [kg.m^2])\n* For Current bias estimation (see point 11), the default values are:\n* LF_surge_integralgain=0.0025 [1/s] \n* LF_sway_integralgain=0.0025 [1/s]\n* LF_yaw_integralgain=0.00005*mass_yaw [N.m.s] (as for the force estimation)",default=0.0))
        self.attributes.append(Attribute("proportionalHF","number","Proportional HF estimation gain",default=0.1))
        self.attributes.append(Attribute("dampingOnly","boolean","Turn off proportional control and use damping only",default=False))