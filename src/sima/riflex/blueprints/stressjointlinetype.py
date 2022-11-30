# 
# Generated with StressJointLineTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .arlinetype import ARLineTypeBlueprint

class StressJointLineTypeBlueprint(ARLineTypeBlueprint):
    """"""

    def __init__(self, name="StressJointLineType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("internalFluid","sima/riflex/InternalFluidType","Internal fluid component type.",False))
        self.add_attribute(Attribute("quadraticDrag","number","Quadratic drag coefficient in normal direction, non-dimensional.",default=0.0))
        self.add_attribute(Attribute("addedMass","number","Added mass pr. unit length coefficient in normal direction, non-dimensional.",default=0.0))
        self.add_attribute(Attribute("extDiameterEnd1","number","External diameter at 'first' end of first conical segment in stress joint.",default=0.0))
        self.add_attribute(Attribute("wallThicknessEnd1","number","Wall thickness at 'first' end of first conical segment in stress joint.",default=0.0))
        self.add_attribute(BlueprintAttribute("segments","sima/riflex/StressJointSegment","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("loadFormulation","sima/riflex/StressJointLoadFormulation",""))
        self.add_attribute(BlueprintAttribute("vivCoefficients","sima/riflex/TimeDomainVIVLoadCoefficients","",True))