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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("runWithPrevious","boolean","Run the load group together with the last",default=False))
        self.attributes.append(BlueprintAttribute("boundaryChangeGroup","sima/riflex/BoundaryChangeGroup","",True))
        self.attributes.append(EnumAttribute("loadType","sima/riflex/StaticLoadType","Load Type"))
        self.attributes.append(Attribute("nStep","integer","Number of load steps",default=10))
        self.attributes.append(Attribute("maxIterations","integer","Maximum number of iterations during application of load",default=10))
        self.attributes.append(Attribute("accuracy","number","Required accuracy measured by displacement norm",default=1e-05))
        self.attributes.append(EnumAttribute("convergenceNorm","sima/riflex/ConvergenceNorm",""))
        self.attributes.append(Attribute("energyAccuracy","number"," Required accuracy measured by energy norm. Value is not used if convergence norm is 'Displacement'.",default=1e-05))
        self.attributes.append(Attribute("entered","boolean","start condition for pipe-in-pipe contact",default=True))
        self.attributes.append(BlueprintAttribute("temperatureVariations","sima/riflex/TemperatureVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("pressureVariations","sima/riflex/PressureVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("winchVariations","sima/riflex/WinchVariationItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("growthFactor","number","Scaling factor for growth profile",default=1.0))
        self.attributes.append(Attribute("windOnTurbineBlades","boolean","Enables wind force on turbine blades",default=True))