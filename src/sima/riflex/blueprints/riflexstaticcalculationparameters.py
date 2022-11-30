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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("loadTypeItems","sima/riflex/StaticLoadTypeItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("matrixStorage","sima/riflex/MatrixStorage",""))
        self.add_attribute(Attribute("currentProfileScaling","number","Scaling factor to amplify or reduce the referred current profile",default=1.0))
        self.add_attribute(BlueprintAttribute("staticLoadComponents","sima/riflex/StaticLoadComponent","",True,Dimension("*")))
        self.add_attribute(Attribute("stressFreeConfiguration","boolean","Whether a stress free configuration has been defined for the Slender system.",default=False))
        self.add_attribute(Attribute("stressfreeFile","string",""))
        self.add_attribute(EnumAttribute("loadAndMassFormulation","sima/riflex/LoadAndMassFormulation",""))
        self.add_attribute(BlueprintAttribute("parameterVariation","sima/riflex/ParameterVariation","",True))
        self.add_attribute(Attribute("storeVisualisationResponses","boolean","Store visualisation responses indicator",default=True))
        self.add_attribute(EnumAttribute("matrixPlotStorage","sima/riflex/MatrixPlotStorage","Storage option for Matrix Plot"))
        self.add_attribute(Attribute("startAtZero","boolean","Start arc length at zero for each line",default=True))