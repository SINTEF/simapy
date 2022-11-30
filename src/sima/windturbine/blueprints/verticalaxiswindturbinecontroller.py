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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("sampleInterval","number","Controller sample interval",default=0.0))
        self.add_attribute(Attribute("startupLength","number","Length of time for using start-up control logic",default=0.0))
        self.add_attribute(Attribute("filterPeriodRotorSpeed","number","Filter period for 1st order LP filter for rotor speed",default=0.0))
        self.add_attribute(Attribute("filterPeriodWindSpeed","number","Filter period for 1st order LP filter for wind speed",default=0.0))
        self.add_attribute(Attribute("filterRadialFrequency","number","Radial frequency removed by notch filter. For value < 0 no notch filter will be applied",default=0.0))
        self.add_attribute(Attribute("notchFilterWidth","number","Width parameter in notch filter",default=0.0))
        self.add_attribute(Attribute("gearBoxRatio","number","Gear box ratio (N rotations of high speed shaft for one roation of the low speed shaft, i.e. generator versus rotor)",default=0.0))
        self.add_attribute(Attribute("maxTorque","number","Maximum torque",default=0.0))
        self.add_attribute(Attribute("maxTorqueRate","number","Maximum torque rate",default=0.0))
        self.add_attribute(Attribute("proportionalGain","number","Proportional gain K that will be used for zero blade pitch angle",default=0.0))
        self.add_attribute(Attribute("initialIntegratorGainRatio","number","Initial value of integrator gain",default=0.0))
        self.add_attribute(Attribute("finalIntegratorGainRatio","number","Final value of integrator gain",default=0.0))
        self.add_attribute(Attribute("integratorRelaxationTime","number","Time period for relaxing the integrator gain after the startup period",default=0.0))
        self.add_attribute(EnumAttribute("windRotorSpeed","sima/windturbine/TableFormat","Wind speed / rotor speed table"))
        self.add_attribute(EnumAttribute("gainScheduling","sima/windturbine/TableFormat",""))
        self.add_attribute(BlueprintAttribute("windRotorSpeedItems","sima/windturbine/WindRotorSpeedItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("gainSchedulingItems","sima/windturbine/GainSchedulingItem","",True,Dimension("*")))