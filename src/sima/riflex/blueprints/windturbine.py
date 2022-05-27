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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("shaftLine","sima/riflex/ARLine","Reference to the line that is used for shaft modelling",False))
        self.attributes.append(BlueprintAttribute("blades","sima/riflex/BladeItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("controller","sima/windturbine/HorizontalAxisWindTurbineController","",True))
        self.attributes.append(BlueprintAttribute("body","sima/sima/Body","Reference to SIMO body with wind",False))
        self.attributes.append(BlueprintAttribute("towerLine","sima/riflex/ARLine","Reference to the line that is used for tower modelling.\nIf specified the incoming wind acting on the blades will be modified due to the presence of the tower.",False))
        self.attributes.append(EnumAttribute("windLoadOption","sima/riflex/WindTurbineLoadOption","If the aerodynamic moment is removed, Cm is treated as zero and the distance between aerodynamic and structural axes is ignored."))
        self.attributes.append(EnumAttribute("turbineOrientation","sima/riflex/TurbineOrientation","Turbine orientation"))
        self.attributes.append(Attribute("bakFactor","number","Bak correction in tower shadow",default=0.1))
        self.attributes.append(Attribute("dragEffect","boolean","Drag correction in tower shadow",default=True))
        self.attributes.append(Attribute("advancedOptions","boolean","Use advanced aerodynamic options",default=True))
        self.attributes.append(Attribute("inductionCalculation","boolean","It is recommended to turn off the induction calculation for a parked or idling wind turbine.",default=True))
        self.attributes.append(Attribute("prandtlTip","boolean","The correction for tip loss due to the finite number of blades may be applied or removed.",default=True))
        self.attributes.append(Attribute("prandtlRoot","boolean","The correction for hub loss due to the finite number of blades may be applied or removed.",default=True))
        self.attributes.append(Attribute("prandtlYaw","boolean","If yaw correction is selected, the Prandtl factor is modified based on the angle between the incoming wind and the rotor plane.",default=True))
        self.attributes.append(BlueprintAttribute("measurementNodes","sima/riflex/MeasurementNode","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("measurementElements","sima/riflex/MeasurementElement","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("yawController","sima/riflex/HorizontalAxisYawController","",True))