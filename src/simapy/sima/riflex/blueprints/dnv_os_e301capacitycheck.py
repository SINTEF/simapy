# 
# Generated with DNV_OS_E301CapacityCheckBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .capacitycheck import CapacityCheckBlueprint

class DNV_OS_E301CapacityCheckBlueprint(CapacityCheckBlueprint):
    """"""

    def __init__(self, name="DNV_OS_E301CapacityCheck", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("limitTimeInterval","boolean","Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time",default=False))
        self.add_attribute(Attribute("startTime","number","",default=0.0))
        self.add_attribute(Attribute("endTime","number","",default=0.0))
        self.add_attribute(Attribute("addIntermediateResults","boolean","Add intermediate element results to the output",default=False))
        self.add_attribute(BlueprintAttribute("sections","sima/riflex/ElementReference","Specification of nodes for displacement storage",True,Dimension("*")))
        self.add_attribute(Attribute("useDistributionFitting","boolean","Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting",default=False))
        self.add_attribute(Attribute("seastateReturnPeriod","number","Return period used for estimating the characteristic extreme value",default=3.0))
        self.add_attribute(EnumAttribute("typeOfUnit","sima/riflex/TypeOfUnit",""))
        self.add_attribute(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.add_attribute(Attribute("safetyFactorOnPretension","number","",default=0.0))
        self.add_attribute(Attribute("safetyFactorOnEnvironmentTension","number","",default=0.0))
        self.add_attribute(Attribute("lastFunctionalLoadGroup","integer","Number of the last load group in static calculation parameter that is part of the functional load",default=0))