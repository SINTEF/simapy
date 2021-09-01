# 
# Generated with RIFLEXStaticCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RIFLEXStaticCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RIFLEXStaticCalculationParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("loadTypeItems","sima/riflex/StaticLoadTypeItem","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("matrixStorage","sima/riflex/MatrixStorage",""))
        self.attributes.append(Attribute("currentProfileScaling","number","Scaling factor to amplify or reduce the referred current profile",default=1.0))
        self.attributes.append(BlueprintAttribute("staticLoadComponents","sima/riflex/StaticLoadComponent","",True,Dimension("size","")))
        self.attributes.append(Attribute("stressFreeConfiguration","boolean","Whether a stress free configuration has been defined for the Slender system.",default=False))
        self.attributes.append(Attribute("stressfreeFile","string","",default=""))
        self.attributes.append(EnumAttribute("loadAndMassFormulation","sima/riflex/LoadAndMassFormulation",""))
        self.attributes.append(BlueprintAttribute("parameterVariation","sima/riflex/ParameterVariation","",True))
        self.attributes.append(Attribute("storeVisualisationResponses","boolean","Store visualisation responses indicator",default=True))
        self.attributes.append(EnumAttribute("matrixPlotStorage","sima/riflex/MatrixPlotStorage","Storage option for Matrix Plot"))
        self.attributes.append(Attribute("startAtZero","boolean","Start arc length at zero for each line",default=True))