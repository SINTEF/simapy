# 
# Generated with FibreRopeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .crosssection import CrossSectionBlueprint
from .crsaxialfrictionmodel import CRSAxialFrictionModelBlueprint

class FibreRopeBlueprint(CrossSectionBlueprint,CRSAxialFrictionModelBlueprint):
    """"""

    def __init__(self, name="FibreRope", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("staticFriction","number","Static friction force corresponding to elongation",default=0.0))
        self.attributes.append(Attribute("staticElongation","number","Relative elongation",default=0.0))
        self.attributes.append(Attribute("dynamicFriction","number","Dynamic friction force corresponding to elongation",default=0.0))
        self.attributes.append(Attribute("dynamicElongation","number","Relative elongation",default=0.0))
        self.attributes.append(Attribute("axialFriction","boolean","Local axial friction model",default=False))
        self.attributes.append(Attribute("scfkSpecification","boolean","Scaling of Froude-Krylov term in Morison’s equation in normal direction",default=True))
        self.attributes.append(EnumAttribute("loadFormulation","sima/riflex/LoadFormulation",""))
        self.attributes.append(Attribute("hydrodynamicDiameter","number","Hydrodynamic diameter",default=0.0))
        self.attributes.append(Attribute("addedMassTanDir","number","Added mass in tangential direction",default=0.0))
        self.attributes.append(Attribute("addedMassNormDir","number","Added mass in normal direction",default=0.0))
        self.attributes.append(Attribute("dampingNormDir","number","Damping coefficients in normal direction",default=0.0))
        self.attributes.append(Attribute("cdt","number","Quadratic drag coefficient in tangential direction.",default=0.0))
        self.attributes.append(Attribute("cdn","number","Quadratic drag coefficient in normal direction.",default=0.0))
        self.attributes.append(Attribute("cmt","number","Added mass per unit length in tangential direction.",default=0.0))
        self.attributes.append(Attribute("cmn","number","Added mass per unit length in normal direction.",default=0.0))
        self.attributes.append(Attribute("cdtl","number","Linear drag force coefficient in tangential direction.",default=0.0))
        self.attributes.append(Attribute("cdnl","number","Linear drag force coefficient in normal direction.",default=0.0))
        self.attributes.append(Attribute("cdx","number","Quadratic drag coefficient in tangential direction.",default=0.0))
        self.attributes.append(Attribute("cdy","number","Quadratic drag coefficient in normal direction.",default=0.0))
        self.attributes.append(Attribute("amx","number","Added mass per unit length in tangential direction.",default=0.0))
        self.attributes.append(Attribute("amy","number","Added mass per unit length in normal direction.",default=0.0))
        self.attributes.append(Attribute("cdlx","number","Linear drag force coefficient in tangential direction.",default=0.0))
        self.attributes.append(Attribute("cdly","number","Linear drag force coefficient in normal direction.",default=0.0))
        self.attributes.append(EnumAttribute("hydrodynamicInputCode","sima/riflex/HydrodynamicInputCode","Hydrodynamic input code"))
        self.attributes.append(Attribute("scfk","number","Scaling factor for Froude-Krylov term in Morison’s equation in normal direction",default=1.0))
        self.attributes.append(EnumAttribute("scfkt","sima/riflex/TangentialFroudeKrylovScaling","Scale for Froude-Krylov term in Morison’s equation in tangential direction"))
        self.attributes.append(Attribute("massDampingSpecification","boolean","Mass proportional Rayleigh damping",default=False))
        self.attributes.append(Attribute("stiffnessDampingSpecification","boolean","Stiffness proportional Rayleigh damping",default=False))
        self.attributes.append(Attribute("axialDampingSpecification","boolean","Local axial damping model",default=False))
        self.attributes.append(Attribute("temperature","number","Temperature at which the specification applies",default=0.0))
        self.attributes.append(Attribute("alpha","number","Thermal expansion coefficient",default=0.0))
        self.attributes.append(Attribute("beta","number","Pressure expansion coefficient",default=0.0))
        self.attributes.append(BlueprintAttribute("massDamping","sima/riflex/CRSMassDamping","",True))
        self.attributes.append(BlueprintAttribute("stiffnessDamping","sima/riflex/CRSStiffnessDamping","",True))
        self.attributes.append(BlueprintAttribute("axialDamping","sima/riflex/CRSAxialDamping","",True))
        self.attributes.append(Attribute("defaultExpansion","boolean","Use default thermal and pressure expansion settings",default=True))
        self.attributes.append(Attribute("cdax","number","Quadratic aerodynamic drag force coefficient per unit length in tangential direction",default=0.0))
        self.attributes.append(Attribute("cday","number","Quadratic aerodynamic drag force coefficient per unit length in normal direction",default=0.0))
        self.attributes.append(Attribute("cdaz","number","Quadratic aerodynamic drag force coefficient per unit length in z direction",default=0.0))
        self.attributes.append(EnumAttribute("aerodynamicInputCode","sima/riflex/AerodynamicInputCode","Aerodynamic input code"))
        self.attributes.append(Attribute("aerodynamicDiameter","number","Aerodynamic diameter",default=0.0))
        self.attributes.append(BlueprintAttribute("massVolume","sima/riflex/FibreRopeMassVolume","",True))
        self.attributes.append(Attribute("tensionCapacity","number","Tension capacity",default=0.0))
        self.attributes.append(Attribute("maxCurvature","number","Maximum curvature",default=0.0))
        self.attributes.append(Attribute("submerged","boolean","Use formulation for partly submerged cross-section",default=False))
        self.attributes.append(Attribute("tmax","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("fibreRopeModel","sima/simo/FibreRopeModel","",False))