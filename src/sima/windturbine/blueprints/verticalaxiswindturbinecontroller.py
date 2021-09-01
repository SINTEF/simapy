# 
# Generated with VerticalAxisWindTurbineControllerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class VerticalAxisWindTurbineControllerBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="VerticalAxisWindTurbineController", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("sampleInterval","number","Controller sample interval",default=0.0))
        self.attributes.append(Attribute("startupLength","number","Length of time for using start-up control logic",default=0.0))
        self.attributes.append(Attribute("filterPeriodRotorSpeed","number","Filter period for 1st order LP filter for rotor speed",default=0.0))
        self.attributes.append(Attribute("filterPeriodWindSpeed","number","Filter period for 1st order LP filter for wind speed",default=0.0))
        self.attributes.append(Attribute("filterRadialFrequency","number","Radial frequency removed by notch filter. For value < 0 no notch filter will be applied",default=0.0))
        self.attributes.append(Attribute("notchFilterWidth","number","Width parameter in notch filter",default=0.0))
        self.attributes.append(Attribute("gearBoxRatio","number","Gear box ratio (N rotations of high speed shaft for one roation of the low speed shaft, i.e. generator versus rotor)",default=0.0))
        self.attributes.append(Attribute("maxTorque","number","Maximum torque",default=0.0))
        self.attributes.append(Attribute("maxTorqueRate","number","Maximum torque rate",default=0.0))
        self.attributes.append(Attribute("proportionalGain","number","Proportional gain K that will be used for zero blade pitch angle",default=0.0))
        self.attributes.append(Attribute("initialIntegratorGainRatio","number","Initial value of integrator gain",default=0.0))
        self.attributes.append(Attribute("finalIntegratorGainRatio","number","Final value of integrator gain",default=0.0))
        self.attributes.append(Attribute("integratorRelaxationTime","number","Time period for relaxing the integrator gain after the startup period",default=0.0))
        self.attributes.append(EnumAttribute("windRotorSpeed","sima/windturbine/TableFormat","Wind speed / rotor speed table"))
        self.attributes.append(EnumAttribute("gainScheduling","sima/windturbine/TableFormat",""))
        self.attributes.append(BlueprintAttribute("windRotorSpeedItems","sima/windturbine/WindRotorSpeedItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("gainSchedulingItems","sima/windturbine/GainSchedulingItem","",True,Dimension("size","")))