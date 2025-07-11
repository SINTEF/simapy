# 
# Generated with AxisymmetricCrossSectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .crosssection import CrossSectionBlueprint
from .crsaxialfrictionmodel import CRSAxialFrictionModelBlueprint

class AxisymmetricCrossSectionBlueprint(CrossSectionBlueprint,CRSAxialFrictionModelBlueprint):
    """"""

    def __init__(self, name="AxisymmetricCrossSection", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("staticFriction","number","Static friction force corresponding to elongation",default=0.0))
        self.add_attribute(Attribute("staticElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("dynamicFriction","number","Dynamic friction force corresponding to elongation",default=0.0))
        self.add_attribute(Attribute("dynamicElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("axialFriction","boolean","Local axial friction model",default=False))
        self.add_attribute(Attribute("scfkSpecification","boolean","Scaling of Froude-Krylov term in Morison’s equation in normal direction",default=False))
        self.add_attribute(EnumAttribute("loadFormulation","sima/riflex/LoadFormulation",""))
        self.add_attribute(Attribute("hydrodynamicDiameter","number","Hydrodynamic diameter",default=0.0))
        self.add_attribute(EnumAttribute("hydrodynamicInputCode","sima/riflex/HydrodynamicInputCode","Hydrodynamic input code"))
        self.add_attribute(Attribute("addedMassTanDir","number","Added mass in tangential direction",default=0.0))
        self.add_attribute(Attribute("addedMassNormDir","number","Added mass in normal direction",default=0.0))
        self.add_attribute(Attribute("dampingNormDir","number","Damping coefficients in normal direction",default=0.0))
        self.add_attribute(Attribute("normalDirectionScaling","number","Scaling factor for Froude-Krylov term in Morison’s equation in normal direction",default=1.0))
        self.add_attribute(Attribute("tangentialDirectionScaling","number","Scale for Froude-Krylov term in Morison’s equation in tangential direction",default=1.0))
        self.add_attribute(Attribute("cdt","number","Quadratic drag coefficient in tangential direction.",default=0.0))
        self.add_attribute(Attribute("cdn","number","Quadratic drag coefficient in normal direction.",default=0.0))
        self.add_attribute(Attribute("cmt","number","Added mass per unit length in tangential direction.",default=0.0))
        self.add_attribute(Attribute("cmn","number","Added mass per unit length in normal direction.",default=0.0))
        self.add_attribute(Attribute("cdtl","number","Linear drag force coefficient in tangential direction.",default=0.0))
        self.add_attribute(Attribute("cdnl","number","Linear drag force coefficient in normal direction.",default=0.0))
        self.add_attribute(Attribute("cdx","number","Quadratic drag coefficient in tangential direction.",default=0.0))
        self.add_attribute(Attribute("cdy","number","Quadratic drag coefficient in normal direction.",default=0.0))
        self.add_attribute(Attribute("amx","number","Added mass per unit length in tangential direction.",default=0.0))
        self.add_attribute(Attribute("amy","number","Added mass per unit length in normal direction.",default=0.0))
        self.add_attribute(Attribute("cdlx","number","Linear drag force coefficient in tangential direction.",default=0.0))
        self.add_attribute(Attribute("cdly","number","Linear drag force coefficient in normal direction.",default=0.0))
        self.add_attribute(EnumAttribute("hydrodynamicRadiationInputCode","sima/riflex/HydrodynamicInputCode","Code for input of simplified radiation force coefficients"))
        self.add_attribute(Attribute("massDampingSpecification","boolean","Mass proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("stiffnessDampingSpecification","boolean","Stiffness proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("axialDampingSpecification","boolean","Local axial damping model",default=False))
        self.add_attribute(BlueprintAttribute("massDamping","sima/riflex/CRSMassDamping","",True))
        self.add_attribute(BlueprintAttribute("axialDamping","sima/riflex/CRSAxialDamping","",True))
        self.add_attribute(Attribute("temperature","number","Temperature at which the specification applies",default=0.0))
        self.add_attribute(Attribute("alpha","number","Thermal expansion coefficient",default=0.0))
        self.add_attribute(Attribute("beta","number","Pressure expansion coefficient",default=0.0))
        self.add_attribute(Attribute("defaultExpansion","boolean","Use default thermal and pressure expansion settings",default=True))
        self.add_attribute(Attribute("tensionCapacity","number","Tension capacity",default=0.0))
        self.add_attribute(Attribute("maxCurvature","number","Maximum curvature",default=0.0))
        self.add_attribute(Attribute("cdax","number","Quadratic aerodynamic drag force coefficient per unit length in tangential direction",default=0.0))
        self.add_attribute(Attribute("cday","number","Quadratic aerodynamic drag force coefficient per unit length in normal direction",default=0.0))
        self.add_attribute(Attribute("cdaz","number","Quadratic aerodynamic drag force coefficient per unit length in z direction",default=0.0))
        self.add_attribute(EnumAttribute("aerodynamicInputCode","sima/riflex/AerodynamicInputCode","Aerodynamic input code"))
        self.add_attribute(Attribute("aerodynamicDiameter","number","Aerodynamic diameter",default=0.0))
        self.add_attribute(Attribute("netWidthEnd1","number","Net width at segment end 1",default=0.0))
        self.add_attribute(Attribute("netWidthEnd2","number","Net width at segment end 2",default=0.0))
        self.add_attribute(Attribute("currentVelocityScaling","number","Ratio between reduced current speed and ambient current speed due to upstream net shadowing effects",default=1.0))
        self.add_attribute(Attribute("solidityRatio","number","Solidity ratio.",default=0.0))
        self.add_attribute(BlueprintAttribute("vivCoefficients","sima/riflex/TimeDomainVIVLoadCoefficients","",True))
        self.add_attribute(BlueprintAttribute("massVolume","sima/riflex/AxisymmetricCrossSectionMassVolume","",True))
        self.add_attribute(EnumAttribute("axialStiffnessInput","sima/riflex/AxialStiffness","Axial stiffness input specification"))
        self.add_attribute(EnumAttribute("bendingStiffnessInput","sima/riflex/BendingStiffness","Bending stiffness input specification"))
        self.add_attribute(EnumAttribute("torsionStiffnessInput","sima/riflex/TorsionStiffness","Torsion stiffness input specification"))
        self.add_attribute(Attribute("pressureDependency","integer","Pressure dependency parameter related to bending moment",default=0))
        self.add_attribute(EnumAttribute("hysteresisOption","sima/riflex/Hysteresis","Hysteresis option in bending moment / curvature relation"))
        self.add_attribute(Attribute("hardeningParameter","number","Hardening parameter",default=0.0))
        self.add_attribute(Attribute("axialStiffness","number","Axial stiffness",default=0.0))
        self.add_attribute(BlueprintAttribute("axialStiffnessCharacteristics","sima/riflex/AxialStiffnessItem","",True,Dimension("*")))
        self.add_attribute(Attribute("bendingStiffness","number","Bending stiffness around y-axis",default=0.0))
        self.add_attribute(Attribute("intFrictionMoment","number","Internal friction moment.",default=0.0))
        self.add_attribute(Attribute("shearStiffness","number","Shear stiffness",default=0.0))
        self.add_attribute(BlueprintAttribute("bendingStiffnessCharacteristics","sima/riflex/BendingStiffnessY_Item","",True,Dimension("*")))
        self.add_attribute(Attribute("negativeTorsionStiffness","number","Torsion stiffness for negative twist.",default=0.0))
        self.add_attribute(Attribute("positiveTorsionStiffness","number","Torsion stiffness for positive twist.",default=0.0))
        self.add_attribute(BlueprintAttribute("torsionStiffnessCharacteristics","sima/riflex/TorsionStiffnessItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("barBeam","sima/riflex/BarBeam","Cross section type"))
        self.add_attribute(Attribute("stiffnessFactor","number","Initial stiffness factor for internal friction moment",default=10.0))
        self.add_attribute(Attribute("coupledBendingTorsion","boolean","Geometric stiffness coupling between bending and torsion",default=False))
        self.add_attribute(BlueprintAttribute("stiffnessDamping","sima/riflex/CRSStiffnessDamping","",True))