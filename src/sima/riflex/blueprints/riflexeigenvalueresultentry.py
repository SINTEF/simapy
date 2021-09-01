# 
# Generated with RIFLEXEigenvalueResultEntryBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.resultentry import ResultEntryBlueprint

class RIFLEXEigenvalueResultEntryBlueprint(ResultEntryBlueprint):
    """"""

    def __init__(self, name="RIFLEXEigenvalueResultEntry", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("size","")))
        self.attributes.append(Attribute("resource","string","",default=""))
        self.attributes.append(Attribute("relative","boolean","",default=False))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("results","sima/sima/Result","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("entries","sima/sima/ResultEntry","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("riflexLDAT","sima/sima/Result","",True))
        self.attributes.append(BlueprintAttribute("mpfResult","sima/riflex/MatrixPlotResult","",True))
        self.attributes.append(BlueprintAttribute("resFile","sima/riflex/ResFile","",True))