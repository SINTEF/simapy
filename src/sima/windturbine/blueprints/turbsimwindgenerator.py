# 
# Generated with TurbSimWindGeneratorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class TurbSimWindGeneratorBlueprint(NamedObjectBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="TurbSimWindGenerator", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("randSeed1","integer","First random seed (-2147483648 to 2147483647)",default=0))
        self.add_attribute(EnumAttribute("seedGeneration","sima/windturbine/RandomSeedGeneration",""))
        self.add_attribute(Attribute("randSeed2","integer","Second random seed (-2147483648 to 2147483647) for intrinsic pRNG, or an alternative pRNG: 'RanLux' or 'RNSNLW'",default=0))
        self.add_attribute(Attribute("gridPointsZ","integer","Vertical grid-point matrix dimension",default=0))
        self.add_attribute(Attribute("gridPointsY","integer"," Horizontal grid-point matrix dimension",default=0))
        self.add_attribute(Attribute("timeStep","number","",default=0.0))
        self.add_attribute(Attribute("analysisTime","number","Length of analysis time series (program will add time if necessary: AnalysisTime = MAX(AnalysisTime, UsableTime+GridWidth/MeanHHWS) )",default=0.0))
        self.add_attribute(Attribute("usableTime","number","Usable length of output time series (program will add GridWidth/MeanHHWS seconds). Default value is analysis time for Turbsim v1, otherwise ALL",default=0.0))
        self.add_attribute(Attribute("hubHeight","number","Hub height (should be > 0.5*GridHeight)",default=0.0))
        self.add_attribute(Attribute("gridHeight","number","",default=0.0))
        self.add_attribute(Attribute("gridWidth","number","Grid width (should be >= 2*(RotorRadius+ShaftLength))",default=0.0))
        self.add_attribute(EnumAttribute("turbulenceModel","sima/windturbine/TurbulenceModel",""))
        self.add_attribute(EnumAttribute("iecStandard","sima/windturbine/IECStandard",""))
        self.add_attribute(EnumAttribute("turbulenceCharacteristics","sima/windturbine/IECTurbulenceCharacteristics",""))
        self.add_attribute(Attribute("turbulencePercentage","number","Turbulence intensity in percent",default=0.0))
        self.add_attribute(EnumAttribute("windType","sima/windturbine/IECWindType",""))
        self.add_attribute(Attribute("etmC","number"," IEC ETM 'c' parameter",default=0.0))
        self.add_attribute(EnumAttribute("windProfileType","sima/windturbine/IECWindProfileType",""))
        self.add_attribute(Attribute("referenceHeight","number","Height of the reference wind speed",default=0.0))
        self.add_attribute(Attribute("meanWindSpeed","number","Mean (total) wind speed at the reference height",default=0.0))
        self.add_attribute(Attribute("powerLawExponent","number","Power law exponent (or 'default')",default=0.0))
        self.add_attribute(Attribute("surfaceRoughnessLength","number","Surface roughness length (or 'default')",default=0.0))