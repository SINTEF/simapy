# 
# Generated with StaticLoadTypeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StaticLoadTypeItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StaticLoadTypeItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("runWithPrevious","boolean","Run the load group together with the last",default=False))
        self.add_attribute(BlueprintAttribute("boundaryChangeGroup","sima/riflex/BoundaryChangeGroup","",True))
        self.add_attribute(EnumAttribute("loadType","sima/riflex/StaticLoadType","Load Type"))
        self.add_attribute(Attribute("nStep","integer","Number of load steps",default=10))
        self.add_attribute(Attribute("maxIterations","integer","Maximum number of iterations during application of load",default=10))
        self.add_attribute(Attribute("accuracy","number","Required accuracy measured by displacement norm",default=1e-05))
        self.add_attribute(EnumAttribute("convergenceNorm","sima/riflex/ConvergenceNorm",""))
        self.add_attribute(Attribute("energyAccuracy","number"," Required accuracy measured by energy norm. Value is not used if convergence norm is 'Displacement'.",default=1e-05))
        self.add_attribute(Attribute("entered","boolean","start condition for pipe-in-pipe contact",default=True))
        self.add_attribute(BlueprintAttribute("temperatureVariations","sima/riflex/TemperatureVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("pressureVariations","sima/riflex/PressureVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("winchVariations","sima/riflex/WinchVariationItem","",True,Dimension("*")))
        self.add_attribute(Attribute("growthFactor","number","Scaling factor for growth profile",default=1.0))
        self.add_attribute(Attribute("windOnTurbineBlades","boolean","Enables wind force on turbine blades",default=False))