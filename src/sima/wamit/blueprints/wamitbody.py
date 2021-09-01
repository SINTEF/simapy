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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("length","number","Length",default=10.0))
        self.attributes.append(Attribute("width","number","Width",default=5.0))
        self.attributes.append(Attribute("height","number","Height",default=5.0))
        self.attributes.append(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
        self.attributes.append(BlueprintAttribute("initialPosition","sima/sima/Position","",True))
        self.attributes.append(BlueprintAttribute("viewpoints","sima/sima/BodyViewpoint","",True,Dimension("size","")))
        self.attributes.append(Attribute("geometryFilename","string","GDF Geometry",default=""))
        self.attributes.append(EnumAttribute("surfacesToIncludeFromMs2File","sima/wamit/SurfacesToIncludeFromMs2FileOption",""))
        self.attributes.append(Attribute("symmetryAboutX","boolean","",default=False))
        self.attributes.append(Attribute("symmetryAboutY","boolean","",default=False))
        self.attributes.append(Attribute("entitySelectionList","string","",default=""))
        self.attributes.append(EnumAttribute("evaluationMode","sima/wamit/EvaluationModeOption",""))
        self.attributes.append(Attribute("divisionsMultiplier","integer","",default=0))
        self.attributes.append(EnumAttribute("directionOfNormals","sima/wamit/DirectionsOfNormalsOption",""))
        self.attributes.append(BlueprintAttribute("parameterLines","sima/wamit/ParameterLines","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("cog","sima/sima/Point3","Coordinates of centre of gravity, (L)",True))
        self.attributes.append(BlueprintAttribute("massData","sima/hydro/MassMatrix","",True))
        self.attributes.append(BlueprintAttribute("externalStiffness","sima/hydro/HydrostaticStiffnessMatrix","",True))
        self.attributes.append(BlueprintAttribute("linearDamping","sima/hydro/LinearDampingMatrix","",True))
        self.attributes.append(Attribute("includeExternalDampingMatrix","boolean","Use external damping",default=False))
        self.attributes.append(Attribute("includeExternalStiffnessMatrix","boolean","Use external stiffness",default=False))
        self.attributes.append(Attribute("includeExternalMassMatrix","boolean","Use external mass matrix",default=False))
        self.attributes.append(BlueprintAttribute("modes","sima/wamit/ModesOfMotion","",True))
        self.attributes.append(Attribute("characteristicLength","number","Characteristic Length (ULEN)",default=1.0))
        self.attributes.append(BlueprintAttribute("controlSurface","sima/wamit/WamitControlSurface","",True))
        self.attributes.append(EnumAttribute("removeIrregularFrequencies","sima/wamit/RemoveIrregularFrequenciesOption",""))
        self.attributes.append(Attribute("trimWaterline","boolean","The static orientation of the body is shifted relative to the horizontal plane of the free surface, first by a prescribed vertical elevation, then by a pitch angle (often referred to as the trim angle), and then by a roll angle (heel).",default=False))
        self.attributes.append(Attribute("draftChange","number","",default=0.0))
        self.attributes.append(Attribute("heelChange","number","",default=0.0))
        self.attributes.append(Attribute("trimChange","number","",default=0.0))