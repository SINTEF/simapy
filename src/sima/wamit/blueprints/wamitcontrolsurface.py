# 
# Generated with WamitControlSurfaceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WamitControlSurfaceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WamitControlSurface", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("geometryFilename","string","GDF Geometry"))
        self.add_attribute(EnumAttribute("surfacesToIncludeFromMs2File","sima/wamit/SurfacesToIncludeFromMs2FileOption",""))
        self.add_attribute(Attribute("symmetryAboutX","boolean","",default=False))
        self.add_attribute(Attribute("symmetryAboutY","boolean","",default=False))
        self.add_attribute(Attribute("entitySelectionList","string",""))
        self.add_attribute(EnumAttribute("evaluationMode","sima/wamit/EvaluationModeOption",""))
        self.add_attribute(Attribute("divisionsMultiplier","integer","",default=0))
        self.add_attribute(EnumAttribute("directionOfNormals","sima/wamit/DirectionsOfNormalsOption",""))
        self.add_attribute(BlueprintAttribute("parameterLines","sima/wamit/ParameterLines","",True,Dimension("*")))
        self.add_attribute(Attribute("panelSize","number","",default=10.0))