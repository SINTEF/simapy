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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("refPointPressure","number","Internal design pressure at vertical reference position",default=0.0))
        self.attributes.append(Attribute("referencePoint","number","Vertical reference position for internal pressure. \nGiven as the Z coordinate in global coordinate system.",default=0.0))
        self.attributes.append(Attribute("limitTimeInterval","boolean","Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time",default=False))
        self.attributes.append(Attribute("startTime","number","",default=0.0))
        self.attributes.append(Attribute("endTime","number","",default=0.0))
        self.attributes.append(Attribute("addIntermediateResults","boolean","Add intermediate element results to the output",default=False))
        self.attributes.append(BlueprintAttribute("properties","sima/riflex/CombinedLoadingProperties","Specification of nodes for displacement storage",True,Dimension("*")))
        self.attributes.append(Attribute("useDistributionFitting","boolean","Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting",default=False))
        self.attributes.append(Attribute("seastateReturnPeriod","number","Return period used for estimating the characteristic extreme value",default=3.0))
        self.attributes.append(Attribute("percentile","number","Specify percentile in extreme value distribution. \nThe value 0.57038 corresponds to the expected extreme, and 0.9 corresponds to 90% estimate of the extreme response",default=0.57038))
        self.attributes.append(EnumAttribute("approach","sima/riflex/CombinedLoadingApproach",""))
        self.attributes.append(Attribute("customSafetyClassResistanceFactor","number","Safety class resistance factor (ɣ SC)",default=0.0))
        self.attributes.append(Attribute("customLoadEffectFactorForEnvironmentalLoads","number","Load effect factor for environmental loads (ɣ E)",default=0.0))
        self.attributes.append(Attribute("customLoadEffectFactorForFunctionalLoads","number","Load effect factor for functional loads (ɣ F)",default=0.0))
        self.attributes.append(Attribute("customLoadFactorForAccidentalLoads","number","Load factor for accidental loads (ɣ A)",default=0.0))
        self.attributes.append(Attribute("customMaterialResistanceFactor","number","Material resistance factor (ɣ m)",default=0.0))
        self.attributes.append(Attribute("fabricationFactor","number","Fabrication factor (α fab)",default=0.85))
        self.attributes.append(EnumAttribute("safetyClass","sima/post/SafetyClass",""))
        self.attributes.append(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.attributes.append(Attribute("lastFunctionalLoadGroup","integer","Number of the last load group in static calculation parameter that is part of the functional load",default=0))