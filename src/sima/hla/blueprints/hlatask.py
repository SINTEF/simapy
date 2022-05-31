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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.attributes.append(Attribute("runNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("model","sima/hla/HLAModel","",True))
        self.attributes.append(BlueprintAttribute("federates","sima/hla/HLAFederate","",True,Dimension("*")))
        self.attributes.append(Attribute("accelerationFactor","number","Acceleration factor. (1 means real time)",default=1.0))
        self.attributes.append(Attribute("restartAutomatically","boolean","If automatic restart is checked, the HLA federation will be restarted when it ends (even if it ends because of an error)",default=True))
        self.attributes.append(BlueprintAttribute("dataTables","sima/hla/HLADataTable","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("plots","sima/hla/HLASignalPlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("controlPanels","sima/hla/ControlPanel","",True,Dimension("*")))