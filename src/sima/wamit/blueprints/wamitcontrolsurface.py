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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("geometryFilename","string","GDF Geometry",default=""))
        self.attributes.append(EnumAttribute("surfacesToIncludeFromMs2File","sima/wamit/SurfacesToIncludeFromMs2FileOption",""))
        self.attributes.append(Attribute("symmetryAboutX","boolean","",default=False))
        self.attributes.append(Attribute("symmetryAboutY","boolean","",default=False))
        self.attributes.append(Attribute("entitySelectionList","string","",default=""))
        self.attributes.append(EnumAttribute("evaluationMode","sima/wamit/EvaluationModeOption",""))
        self.attributes.append(Attribute("divisionsMultiplier","integer","",default=0))
        self.attributes.append(EnumAttribute("directionOfNormals","sima/wamit/DirectionsOfNormalsOption",""))
        self.attributes.append(BlueprintAttribute("parameterLines","sima/wamit/ParameterLines","",True,Dimension("*")))
        self.attributes.append(Attribute("panelSize","number","",default=10.0))