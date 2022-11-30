# 
# Generated with HLATaskBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.task import TaskBlueprint

class HLATaskBlueprint(TaskBlueprint):
    """"""

    def __init__(self, name="HLATask", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.add_attribute(Attribute("runNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("model","sima/hla/HLAModel","",True))
        self.add_attribute(BlueprintAttribute("federates","sima/hla/HLAFederate","",True,Dimension("*")))
        self.add_attribute(Attribute("accelerationFactor","number","Acceleration factor. (1 means real time)",default=1.0))
        self.add_attribute(Attribute("restartAutomatically","boolean","If automatic restart is checked, the HLA federation will be restarted when it ends (even if it ends because of an error)",default=False))
        self.add_attribute(BlueprintAttribute("dataTables","sima/hla/HLADataTable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("plots","sima/hla/HLASignalPlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("controlPanels","sima/hla/ControlPanel","",True,Dimension("*")))