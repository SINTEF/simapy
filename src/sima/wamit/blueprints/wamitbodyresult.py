# 
# Generated with WamitBodyResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class WamitBodyResultBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="WamitBodyResult", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("firstOrderMotionTransferFunction","sima/hydro/FirstOrderMotionTransferFunction","",True))
        self.add_attribute(BlueprintAttribute("firstOrderWaveForceTransferFunctionDiffraction","sima/wamit/WamitFirstOrderWaveForceTransferFunction","",True))
        self.add_attribute(BlueprintAttribute("firstOrderWaveForceTransferFunctionHaskind","sima/wamit/WamitFirstOrderWaveForceTransferFunction","",True))
        self.add_attribute(Attribute("characteristicLength","number","Characteristic Length (ULEN)",default=0.0))
        self.add_attribute(Attribute("x","number","x position coordinate ",default=0.0))
        self.add_attribute(Attribute("y","number","y position coordinate ",default=0.0))
        self.add_attribute(Attribute("z","number","z position coordinate ",default=0.0))
        self.add_attribute(Attribute("rz","number","rotation about z-axis",default=0.0))
        self.add_attribute(Attribute("symmetryAboutX","boolean","",default=False))
        self.add_attribute(Attribute("symmetryAboutY","boolean","",default=False))
        self.add_attribute(Attribute("gravity","number","",default=0.0))
        self.add_attribute(Attribute("waterDensity","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("volumes","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("centreOfGravity","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("centreOfBuoyancy","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("radiationData","sima/hydro/RadiationDataGroup","",True))
        self.add_attribute(BlueprintAttribute("waveDriftForceMomentum","sima/wamit/WamitWaveDriftForce","",True))
        self.add_attribute(BlueprintAttribute("waveDriftForceControlSurface","sima/wamit/WamitWaveDriftForce","",True))
        self.add_attribute(BlueprintAttribute("waveDriftForcePressure","sima/wamit/WamitWaveDriftForce","",True))
        self.add_attribute(Attribute("waterDepth","number","Depth at global origin",default=0.0))
        self.add_attribute(BlueprintAttribute("externalStiffness","sima/hydro/ExternalStiffnessMatrix","",True))
        self.add_attribute(BlueprintAttribute("structuralMass","sima/hydro/StructuralMass","",True))
        self.add_attribute(BlueprintAttribute("linearDamping","sima/hydro/LinearDampingMatrix","",True))
        self.add_attribute(BlueprintAttribute("hydrostaticStiffness","sima/hydro/HydrostaticStiffnessData","",True))