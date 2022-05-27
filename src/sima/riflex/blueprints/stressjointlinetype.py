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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("internalFluid","sima/riflex/InternalFluidType","Internal fluid component type.",False))
        self.attributes.append(Attribute("quadraticDrag","number","Quadratic drag coefficient in normal direction, non-dimensional.",default=0.0))
        self.attributes.append(Attribute("addedMass","number","Added mass pr. unit length coefficient in normal direction, non-dimensional.",default=0.0))
        self.attributes.append(Attribute("extDiameterEnd1","number","External diameter at 'first' end of first conical segment in stress joint.",default=0.0))
        self.attributes.append(Attribute("wallThicknessEnd1","number","Wall thickness at 'first' end of first conical segment in stress joint.",default=0.0))
        self.attributes.append(BlueprintAttribute("segments","sima/riflex/StressJointSegment","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("loadFormulation","sima/riflex/StressJointLoadFormulation",""))
        self.attributes.append(BlueprintAttribute("vivCoefficients","sima/riflex/TimeDomainVIVLoadCoefficients","",True))