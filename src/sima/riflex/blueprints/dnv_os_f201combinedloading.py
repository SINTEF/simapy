# 
# Generated with DNV_OS_F201CombinedLoadingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .combinedloading import CombinedLoadingBlueprint

class DNV_OS_F201CombinedLoadingBlueprint(CombinedLoadingBlueprint):
    """"""

    def __init__(self, name="DNV_OS_F201CombinedLoading", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("refPointPressure","number","Internal design pressure at vertical reference position",default=0.0))
        self.add_attribute(Attribute("referencePoint","number","Vertical reference position for internal pressure. \nGiven as the Z coordinate in global coordinate system.",default=0.0))
        self.add_attribute(Attribute("limitTimeInterval","boolean","Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time",default=False))
        self.add_attribute(Attribute("startTime","number","",default=0.0))
        self.add_attribute(Attribute("endTime","number","",default=0.0))
        self.add_attribute(Attribute("addIntermediateResults","boolean","Add intermediate element results to the output",default=False))
        self.add_attribute(BlueprintAttribute("properties","sima/riflex/CombinedLoadingProperties","Specification of nodes for displacement storage",True,Dimension("*")))
        self.add_attribute(Attribute("useDistributionFitting","boolean","Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting",default=False))
        self.add_attribute(Attribute("seastateReturnPeriod","number","Return period used for estimating the characteristic extreme value",default=3.0))
        self.add_attribute(Attribute("percentile","number","Specify percentile in extreme value distribution. \nThe value 0.57038 corresponds to the expected extreme, and 0.9 corresponds to 90% estimate of the extreme response",default=0.57038))
        self.add_attribute(EnumAttribute("approach","sima/riflex/CombinedLoadingApproach",""))
        self.add_attribute(Attribute("customSafetyClassResistanceFactor","number","Safety class resistance factor (ɣ SC)",default=0.0))
        self.add_attribute(Attribute("customLoadEffectFactorForEnvironmentalLoads","number","Load effect factor for environmental loads (ɣ E)",default=0.0))
        self.add_attribute(Attribute("customLoadEffectFactorForFunctionalLoads","number","Load effect factor for functional loads (ɣ F)",default=0.0))
        self.add_attribute(Attribute("customLoadFactorForAccidentalLoads","number","Load factor for accidental loads (ɣ A)",default=0.0))
        self.add_attribute(Attribute("customMaterialResistanceFactor","number","Material resistance factor (ɣ m)",default=0.0))
        self.add_attribute(Attribute("fabricationFactor","number","Fabrication factor (α fab)",default=0.85))
        self.add_attribute(EnumAttribute("safetyClass","sima/post/SafetyClass",""))
        self.add_attribute(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.add_attribute(Attribute("lastFunctionalLoadGroup","integer","Number of the last load group in static calculation parameter that is part of the functional load",default=0))