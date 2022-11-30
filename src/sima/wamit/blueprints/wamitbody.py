# 
# Generated with WamitBodyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.body import BodyBlueprint

class WamitBodyBlueprint(BodyBlueprint):
    """"""

    def __init__(self, name="WamitBody", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("length","number","Length",default=10.0))
        self.add_attribute(Attribute("width","number","Width",default=5.0))
        self.add_attribute(Attribute("height","number","Height",default=5.0))
        self.add_attribute(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
        self.add_attribute(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.add_attribute(BlueprintAttribute("viewpoints","sima/sima/BodyViewpoint","",True,Dimension("*")))
        self.add_attribute(Attribute("geometryFilename","string","GDF Geometry"))
        self.add_attribute(EnumAttribute("surfacesToIncludeFromMs2File","sima/wamit/SurfacesToIncludeFromMs2FileOption",""))
        self.add_attribute(Attribute("symmetryAboutX","boolean","",default=False))
        self.add_attribute(Attribute("symmetryAboutY","boolean","",default=False))
        self.add_attribute(Attribute("entitySelectionList","string",""))
        self.add_attribute(EnumAttribute("evaluationMode","sima/wamit/EvaluationModeOption",""))
        self.add_attribute(Attribute("divisionsMultiplier","integer","",default=0))
        self.add_attribute(EnumAttribute("directionOfNormals","sima/wamit/DirectionsOfNormalsOption",""))
        self.add_attribute(BlueprintAttribute("parameterLines","sima/wamit/ParameterLines","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("cog","sima/sima/Point3","Coordinates of centre of gravity, (L)",True))
        self.add_attribute(BlueprintAttribute("massData","sima/hydro/MassMatrix","",True))
        self.add_attribute(BlueprintAttribute("externalStiffness","sima/hydro/HydrostaticStiffnessMatrix","",True))
        self.add_attribute(BlueprintAttribute("linearDamping","sima/hydro/LinearDampingMatrix","",True))
        self.add_attribute(Attribute("includeExternalDampingMatrix","boolean","Use external damping",default=False))
        self.add_attribute(Attribute("includeExternalStiffnessMatrix","boolean","Use external stiffness",default=False))
        self.add_attribute(Attribute("includeExternalMassMatrix","boolean","Use external mass matrix",default=False))
        self.add_attribute(BlueprintAttribute("modes","sima/wamit/ModesOfMotion","",True))
        self.add_attribute(Attribute("characteristicLength","number","Characteristic Length (ULEN)",default=1.0))
        self.add_attribute(BlueprintAttribute("controlSurface","sima/wamit/WamitControlSurface","",True))
        self.add_attribute(EnumAttribute("removeIrregularFrequencies","sima/wamit/RemoveIrregularFrequenciesOption",""))
        self.add_attribute(Attribute("trimWaterline","boolean","The static orientation of the body is shifted relative to the horizontal plane of the free surface, first by a prescribed vertical elevation, then by a pitch angle (often referred to as the trim angle), and then by a roll angle (heel).",default=False))
        self.add_attribute(Attribute("draftChange","number","",default=0.0))
        self.add_attribute(Attribute("heelChange","number","",default=0.0))
        self.add_attribute(Attribute("trimChange","number","",default=0.0))