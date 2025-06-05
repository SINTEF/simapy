# 
# Generated with TensionAndCurvatureCapacityCheckBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .capacitycheck import CapacityCheckBlueprint

class TensionAndCurvatureCapacityCheckBlueprint(CapacityCheckBlueprint):
    """"""

    def __init__(self, name="TensionAndCurvatureCapacityCheck", package_path="sima/riflex", description=""):
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
        self.add_attribute(EnumAttribute("check","sima/riflex/UtilizationCheck",""))
        self.add_attribute(Attribute("tensionMaterialFactor","number","",default=1.0))
        self.add_attribute(Attribute("tensionLoadFactor","number","",default=1.0))
        self.add_attribute(Attribute("curvatureMaterialFactor","number","",default=1.0))
        self.add_attribute(Attribute("curvatureLoadFactor","number","",default=1.0))