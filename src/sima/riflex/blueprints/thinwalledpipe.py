# 
# Generated with ThinWalledPipeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .crosssection import CrossSectionBlueprint

class ThinWalledPipeBlueprint(CrossSectionBlueprint):
    """"""

    def __init__(self, name="ThinWalledPipe", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("scfkSpecification","boolean","Scaling of Froude-Krylov term in Morison’s equation in normal direction",default=False))
        self.add_attribute(EnumAttribute("loadFormulation","sima/riflex/LoadFormulation",""))
        self.add_attribute(Attribute("hydrodynamicDiameter","number","Hydrodynamic diameter",default=0.0))
        self.add_attribute(Attribute("addedMassTanDir","number","Added mass in tangential direction",default=0.0))
        self.add_attribute(Attribute("addedMassNormDir","number","Added mass in normal direction",default=0.0))
        self.add_attribute(Attribute("dampingNormDir","number","Damping coefficients in normal direction",default=0.0))
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
        self.add_attribute(EnumAttribute("hydrodynamicInputCode","sima/riflex/HydrodynamicInputCode","Hydrodynamic input code"))
        self.add_attribute(Attribute("scfk","number","Scaling factor for Froude-Krylov term in Morison’s equation in normal direction",default=1.0))
        self.add_attribute(EnumAttribute("scfkt","sima/riflex/TangentialFroudeKrylovScaling","Scale for Froude-Krylov term in Morison’s equation in tangential direction"))
        self.add_attribute(Attribute("massDampingSpecification","boolean","Mass proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("stiffnessDampingSpecification","boolean","Stiffness proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("axialDampingSpecification","boolean","Local axial damping model",default=False))
        self.add_attribute(Attribute("temperature","number","Temperature at which the specification applies",default=0.0))
        self.add_attribute(Attribute("alpha","number","Thermal expansion coefficient",default=0.0))
        self.add_attribute(Attribute("beta","number","Pressure expansion coefficient",default=0.0))
        self.add_attribute(BlueprintAttribute("massDamping","sima/riflex/CRSMassDamping","",True))
        self.add_attribute(BlueprintAttribute("stiffnessDamping","sima/riflex/CRSStiffnessDamping","",True))
        self.add_attribute(BlueprintAttribute("axialDamping","sima/riflex/CRSAxialDamping","",True))
        self.add_attribute(Attribute("defaultExpansion","boolean","Use default thermal and pressure expansion settings",default=True))
        self.add_attribute(Attribute("cdax","number","Quadratic aerodynamic drag force coefficient per unit length in tangential direction",default=0.0))
        self.add_attribute(Attribute("cday","number","Quadratic aerodynamic drag force coefficient per unit length in normal direction",default=0.0))
        self.add_attribute(Attribute("cdaz","number","Quadratic aerodynamic drag force coefficient per unit length in z direction",default=0.0))
        self.add_attribute(EnumAttribute("aerodynamicInputCode","sima/riflex/AerodynamicInputCode","Aerodynamic input code"))
        self.add_attribute(Attribute("aerodynamicDiameter","number","Aerodynamic diameter",default=0.0))
        self.add_attribute(Attribute("pipeDiameter","number","Diameter of pipe.",default=0.0))
        self.add_attribute(Attribute("pipeThickness","number","Thickness of pipe",default=0.0))
        self.add_attribute(Attribute("materialDensity","number","Density of pipe material",default=0.0))
        self.add_attribute(Attribute("extCoatingThickness","number","Thickness of external coating",default=0.0))
        self.add_attribute(Attribute("extCoatingDensity","number","Density of external coating",default=0.0))
        self.add_attribute(Attribute("extContactRadius","number","External contact radius",default=0.0))
        self.add_attribute(Attribute("intContactRadius","number","Inner contact radius",default=0.0))
        self.add_attribute(BlueprintAttribute("materialProperties","sima/riflex/ThinWalledPipeMaterial","",True))
        self.add_attribute(Attribute("tensionCapacity","number","Tension capacity",default=0.0))
        self.add_attribute(Attribute("maxCurvature","number","Maximum curvature",default=0.0))
        self.add_attribute(Attribute("calculateBeta","boolean","Let RIFLEX calculate beta",default=False))
        self.add_attribute(EnumAttribute("diameterType","sima/riflex/InnerOuter","Inner or outer diameter"))
        self.add_attribute(Attribute("coupledBendingTorsion","boolean","Geometric stiffness coupling between bending and torsion",default=False))
        self.add_attribute(EnumAttribute("hydrodynamicRadiationInputCode","sima/riflex/HydrodynamicInputCode","Code for input of simplified radiation force coefficients"))
        self.add_attribute(BlueprintAttribute("vivCoefficients","sima/riflex/TimeDomainVIVLoadCoefficients","",True))