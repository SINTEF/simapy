# 
# Generated with WindTurbineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class WindTurbineBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="WindTurbine", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("shaftLine","sima/riflex/ARLine","Reference to the line that is used for shaft modelling",False))
        self.add_attribute(BlueprintAttribute("blades","sima/riflex/BladeItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("controller","sima/riflex/HorizontalAxisController","",True))
        self.add_attribute(BlueprintAttribute("body","sima/sima/Body","Reference to SIMO body with wind",False))
        self.add_attribute(BlueprintAttribute("towerLine","sima/riflex/ARLine","Reference to the line that is used for tower modelling.\nIf specified the incoming wind acting on the blades will be modified due to the presence of the tower.",False))
        self.add_attribute(EnumAttribute("windLoadOption","sima/riflex/WindTurbineLoadOption","If the aerodynamic moment is removed, Cm is treated as zero and the distance between aerodynamic and structural axes is ignored."))
        self.add_attribute(EnumAttribute("turbineOrientation","sima/riflex/TurbineOrientation","Turbine orientation"))
        self.add_attribute(Attribute("bakFactor","number","Bak correction in tower shadow",default=0.1))
        self.add_attribute(Attribute("dragEffect","boolean","Drag correction in tower shadow",default=False))
        self.add_attribute(Attribute("advancedOptions","boolean","Use advanced aerodynamic options",default=False))
        self.add_attribute(Attribute("inductionCalculation","boolean","It is recommended to turn off the induction calculation for a parked or idling wind turbine.",default=True))
        self.add_attribute(Attribute("prandtlTip","boolean","The correction for tip loss due to the finite number of blades may be applied or removed.",default=True))
        self.add_attribute(Attribute("prandtlRoot","boolean","The correction for hub loss due to the finite number of blades may be applied or removed.",default=False))
        self.add_attribute(Attribute("prandtlYaw","boolean","If yaw correction is selected, the Prandtl factor is modified based on the angle between the incoming wind and the rotor plane.",default=True))
        self.add_attribute(BlueprintAttribute("measurementNodes","sima/riflex/MeasurementNode","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("measurementElements","sima/riflex/MeasurementElement","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("yawController","sima/riflex/HorizontalAxisYawController","",True))