# 
# Generated with HorizontalAxisWindTurbineControllerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class HorizontalAxisWindTurbineControllerBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="HorizontalAxisWindTurbineController", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("kp","number","Proportionnal gain K that will be used for zero blade pitch angle",default=0.0))
        self.attributes.append(Attribute("ki","number","Integral gain",default=0.0))
        self.attributes.append(Attribute("filterPeriod","number","Filter period for 1st order LP filter",default=0.0))
        self.attributes.append(Attribute("ratedOmega","number","Rated electrical omega",default=0.0))
        self.attributes.append(Attribute("ratedTorque","number","Rated electrical torque",default=0.0))
        self.attributes.append(Attribute("gearBoxRatio","number","Gear box ratio",default=0.0))
        self.attributes.append(Attribute("maxPitchRate","number","Maximum pitch rate",default=0.0))
        self.attributes.append(Attribute("maxPitch","number","Maximum pitch",default=0.0))
        self.attributes.append(Attribute("maxTorqueRate","number","Maximum torque rate",default=0.0))
        self.attributes.append(Attribute("maxTorque","number","Maximum torque",default=0.0))
        self.attributes.append(EnumAttribute("gainScheduling","sima/windturbine/TableFormat",""))
        self.attributes.append(BlueprintAttribute("gainItems","sima/windturbine/GainItem","",True,Dimension("*")))
        self.attributes.append(Attribute("external","boolean","Use external controller",default=False))
        self.attributes.append(Attribute("controllerFile","string","Path to controller file",default=""))
        self.attributes.append(Attribute("className","string","Class name of controller",default=""))
        self.attributes.append(Attribute("configuration","string","Configuration filename",default=""))
        self.attributes.append(BlueprintAttribute("libraryPaths","sima/sima/LibraryPaths","",True))
        self.attributes.append(Attribute("reg3MinPitch","number","Minimum pitch angle for which electrical torque versus generator speed will stay in region 3",default=0.0))
        self.attributes.append(Attribute("transitionalSpeed15","number","Transitional generator speed between region 1 and 1.5",default=0.0))
        self.attributes.append(Attribute("transitionalSpeed20","number","Transitional generator speed between region 1.5 and 2",default=0.0))
        self.attributes.append(Attribute("transitionalSpeed25","number","Transitional generator speed between region 2 and 2.5",default=0.0))
        self.attributes.append(Attribute("transitionalSpeed30","number","Transitional generator speed between region 2.5 and 3",default=0.0))
        self.attributes.append(Attribute("reg2Torque","number","Generator torque constant in region 2",default=0.0))
        self.attributes.append(EnumAttribute("powerExtraction","sima/windturbine/PowerExtraction",""))
        self.attributes.append(Attribute("minPitch","number","Minimum pitch setting in pitch controller",default=0.0))
        self.attributes.append(Attribute("sampleInterval","number","Controller sample interval",default=0.0))
        self.attributes.append(EnumAttribute("controllerType","sima/windturbine/ControllerType",""))