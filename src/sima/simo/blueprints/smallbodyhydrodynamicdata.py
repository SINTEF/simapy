# 
# Generated with SmallBodyHydrodynamicDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SmallBodyHydrodynamicDataBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SmallBodyHydrodynamicData", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("svol","number","Fully submerged volume",default=0.0))
        self.attributes.append(Attribute("am1","number","Added mass in 1. degree of freedom, fully submerged",default=0.0))
        self.attributes.append(Attribute("am2","number","Added mass in 2. degree of freedom, fully submerged",default=0.0))
        self.attributes.append(Attribute("am3","number","Added mass in 3. degree of freedom, fully submerged",default=0.0))
        self.attributes.append(Attribute("c11","number","Linear drag coefficient in 1. degree of freedom, \nfully submerged",default=0.0))
        self.attributes.append(Attribute("c12","number","Linear drag coefficient in 2. degree of freedom, \nfully submerged",default=0.0))
        self.attributes.append(Attribute("c13","number","Linear drag coefficient in 3. degree of freedom, \nfully submerged",default=0.0))
        self.attributes.append(Attribute("c21","number","Quadratic drag coefficient in 1. degree of freedom,\nfully submerged",default=0.0))
        self.attributes.append(Attribute("c22","number","Quadratic drag coefficient in 2. degree of freedom,\nfully submerged",default=0.0))
        self.attributes.append(Attribute("c23","number","Quadratic drag coefficient in 3. degree of freedom,fully submerged",default=0.0))
        self.attributes.append(Attribute("zcoef","number","Vertical position used as reference for depth dependency",default=0.0))
        self.attributes.append(EnumAttribute("depthDependency","sima/simo/DepthDependency","Reference for depth dependency"))
        self.attributes.append(BlueprintAttribute("depthDependentHydrodynamicCoefficients","sima/simo/DepthDependenthydrodynamicCoefficient","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("soilPenetration","sima/simo/SoilPenetration","",True))
        self.attributes.append(BlueprintAttribute("diffractedWave","sima/hydro/DiffractedWave","",False))