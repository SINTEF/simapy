# 
# Generated with WamitBodyResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WamitBodyResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WamitBodyResult", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("firstOrderMotionTransferFunction","sima/hydro/FirstOrderMotionTransferFunction","",True))
        self.attributes.append(BlueprintAttribute("firstOrderWaveForceTransferFunctionDiffraction","sima/wamit/WamitFirstOrderWaveForceTransferFunction","",True))
        self.attributes.append(BlueprintAttribute("firstOrderWaveForceTransferFunctionHaskind","sima/wamit/WamitFirstOrderWaveForceTransferFunction","",True))
        self.attributes.append(Attribute("characteristicLength","number","Characteristic Length (ULEN)",default=0.0))
        self.attributes.append(Attribute("x","number","x position coordinate ",default=0.0))
        self.attributes.append(Attribute("y","number","y position coordinate ",default=0.0))
        self.attributes.append(Attribute("z","number","z position coordinate ",default=0.0))
        self.attributes.append(Attribute("rz","number","rotation about z-axis",default=0.0))
        self.attributes.append(Attribute("symmetryAboutX","boolean","",default=False))
        self.attributes.append(Attribute("symmetryAboutY","boolean","",default=False))
        self.attributes.append(Attribute("gravity","number","",default=0.0))
        self.attributes.append(Attribute("waterDensity","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("volumes","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("centreOfGravity","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("centreOfBuoyancy","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("radiationData","sima/hydro/RadiationDataGroup","",True))
        self.attributes.append(BlueprintAttribute("waveDriftForceMomentum","sima/wamit/WamitWaveDriftForce","",True))
        self.attributes.append(BlueprintAttribute("waveDriftForceControlSurface","sima/wamit/WamitWaveDriftForce","",True))
        self.attributes.append(BlueprintAttribute("waveDriftForcePressure","sima/wamit/WamitWaveDriftForce","",True))
        self.attributes.append(Attribute("waterDepth","number","Depth at global origin",default=0.0))
        self.attributes.append(BlueprintAttribute("externalStiffness","sima/hydro/ExternalStiffnessMatrix","",True))
        self.attributes.append(BlueprintAttribute("structuralMass","sima/hydro/StructuralMass","",True))
        self.attributes.append(BlueprintAttribute("linearDamping","sima/hydro/LinearDampingMatrix","",True))
        self.attributes.append(BlueprintAttribute("hydrostaticStiffness","sima/hydro/HydrostaticStiffnessData","",True))