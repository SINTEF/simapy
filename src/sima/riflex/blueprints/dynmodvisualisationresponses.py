# 
# Generated with DynmodVisualisationResponsesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynmodVisualisationResponsesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynmodVisualisationResponses", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("startTime","number","Start time for export",default=0.0))
        self.attributes.append(Attribute("endTime","number","End time for export",default=512.0))
        self.attributes.append(Attribute("timeIncrement","number","Time increment for export",default=0.5))
        self.attributes.append(Attribute("storeVisualisationResponses","boolean","Visualisation responses indicator",default=False))
        self.attributes.append(Attribute("storeVTF","boolean","Visualisation responses indicator",default=False))