# This an autogenerated file
# 
# Generated with ThinWalledPipe
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thinwalledpipe import ThinWalledPipeBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .aerodynamicinputcode import AerodynamicInputCode
from .crosssection import CrossSection
from .crsaxialdamping import CRSAxialDamping
from .crsaxialfrictionmodel import CRSAxialFrictionModel
from .crsmassdamping import CRSMassDamping
from .crsstiffnessdamping import CRSStiffnessDamping
from .hydrodynamicinputcode import HydrodynamicInputCode
from .innerouter import InnerOuter
from .loadformulation import LoadFormulation
from .thinwalledpipematerial import ThinWalledPipeMaterial
from .timedomainvivloadcoefficients import TimeDomainVIVLoadCoefficients

class ThinWalledPipe(CrossSection,CRSAxialFrictionModel):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    staticFriction : float
         Static friction force corresponding to elongation(default 0.0)
    staticElongation : float
         Relative elongation(default 0.0)
    dynamicFriction : float
         Dynamic friction force corresponding to elongation(default 0.0)
    dynamicElongation : float
         Relative elongation(default 0.0)
    axialFriction : bool
         Local axial friction model(default False)
    scfkSpecification : bool
         Scaling of Froude-Krylov term in Morison’s equation in normal direction(default False)
    loadFormulation : LoadFormulation
    hydrodynamicDiameter : float
         Hydrodynamic diameter(default 0.0)
    hydrodynamicInputCode : HydrodynamicInputCode
         Hydrodynamic input code
    addedMassTanDir : float
         Added mass in tangential direction(default 0.0)
    addedMassNormDir : float
         Added mass in normal direction(default 0.0)
    dampingNormDir : float
         Damping coefficients in normal direction(default 0.0)
    normalDirectionScaling : float
         Scaling factor for Froude-Krylov term in Morison’s equation in normal direction(default 1.0)
    tangentialDirectionScaling : float
         Scale for Froude-Krylov term in Morison’s equation in tangential direction(default 1.0)
    cdt : float
         Quadratic drag coefficient in tangential direction.(default 0.0)
    cdn : float
         Quadratic drag coefficient in normal direction.(default 0.0)
    cmt : float
         Added mass per unit length in tangential direction.(default 0.0)
    cmn : float
         Added mass per unit length in normal direction.(default 0.0)
    cdtl : float
         Linear drag force coefficient in tangential direction.(default 0.0)
    cdnl : float
         Linear drag force coefficient in normal direction.(default 0.0)
    cdx : float
         Quadratic drag coefficient in tangential direction.(default 0.0)
    cdy : float
         Quadratic drag coefficient in normal direction.(default 0.0)
    amx : float
         Added mass per unit length in tangential direction.(default 0.0)
    amy : float
         Added mass per unit length in normal direction.(default 0.0)
    cdlx : float
         Linear drag force coefficient in tangential direction.(default 0.0)
    cdly : float
         Linear drag force coefficient in normal direction.(default 0.0)
    hydrodynamicRadiationInputCode : HydrodynamicInputCode
         Code for input of simplified radiation force coefficients
    massDampingSpecification : bool
         Mass proportional Rayleigh damping(default False)
    stiffnessDampingSpecification : bool
         Stiffness proportional Rayleigh damping(default False)
    axialDampingSpecification : bool
         Local axial damping model(default False)
    massDamping : CRSMassDamping
    axialDamping : CRSAxialDamping
    temperature : float
         Temperature at which the specification applies(default 0.0)
    alpha : float
         Thermal expansion coefficient(default 0.0)
    beta : float
         Pressure expansion coefficient(default 0.0)
    defaultExpansion : bool
         Use default thermal and pressure expansion settings(default True)
    tensionCapacity : float
         Tension capacity(default 0.0)
    maxCurvature : float
         Maximum curvature(default 0.0)
    cdax : float
         Quadratic aerodynamic drag force coefficient per unit length in tangential direction(default 0.0)
    cday : float
         Quadratic aerodynamic drag force coefficient per unit length in normal direction(default 0.0)
    cdaz : float
         Quadratic aerodynamic drag force coefficient per unit length in z direction(default 0.0)
    aerodynamicInputCode : AerodynamicInputCode
         Aerodynamic input code
    aerodynamicDiameter : float
         Aerodynamic diameter(default 0.0)
    vivCoefficients : TimeDomainVIVLoadCoefficients
    pipeDiameter : float
         Diameter of pipe.(default 0.0)
    pipeThickness : float
         Thickness of pipe(default 0.0)
    materialDensity : float
         Density of pipe material(default 0.0)
    extCoatingThickness : float
         Thickness of external coating(default 0.0)
    extCoatingDensity : float
         Density of external coating(default 0.0)
    extContactRadius : float
         External contact radius(default 0.0)
    intContactRadius : float
         Inner contact radius(default 0.0)
    materialProperties : ThinWalledPipeMaterial
    calculateBeta : bool
         Let RIFLEX calculate beta(default False)
    diameterType : InnerOuter
         Inner or outer diameter
    coupledBendingTorsion : bool
         Geometric stiffness coupling between bending and torsion(default False)
    stiffnessDamping : CRSStiffnessDamping
    """

    def __init__(self , description="", staticFriction=0.0, staticElongation=0.0, dynamicFriction=0.0, dynamicElongation=0.0, axialFriction=False, scfkSpecification=False, loadFormulation=LoadFormulation.MORISON, hydrodynamicDiameter=0.0, hydrodynamicInputCode=HydrodynamicInputCode.DIMENSIONAL, addedMassTanDir=0.0, addedMassNormDir=0.0, dampingNormDir=0.0, normalDirectionScaling=1.0, tangentialDirectionScaling=1.0, cdt=0.0, cdn=0.0, cmt=0.0, cmn=0.0, cdtl=0.0, cdnl=0.0, cdx=0.0, cdy=0.0, amx=0.0, amy=0.0, cdlx=0.0, cdly=0.0, hydrodynamicRadiationInputCode=HydrodynamicInputCode.DIMENSIONAL, massDampingSpecification=False, stiffnessDampingSpecification=False, axialDampingSpecification=False, temperature=0.0, alpha=0.0, beta=0.0, defaultExpansion=True, tensionCapacity=0.0, maxCurvature=0.0, cdax=0.0, cday=0.0, cdaz=0.0, aerodynamicInputCode=AerodynamicInputCode.NONE, aerodynamicDiameter=0.0, pipeDiameter=0.0, pipeThickness=0.0, materialDensity=0.0, extCoatingThickness=0.0, extCoatingDensity=0.0, extContactRadius=0.0, intContactRadius=0.0, calculateBeta=False, diameterType=InnerOuter.OUTER, coupledBendingTorsion=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.staticFriction = staticFriction
        self.staticElongation = staticElongation
        self.dynamicFriction = dynamicFriction
        self.dynamicElongation = dynamicElongation
        self.axialFriction = axialFriction
        self.scfkSpecification = scfkSpecification
        self.loadFormulation = loadFormulation
        self.hydrodynamicDiameter = hydrodynamicDiameter
        self.hydrodynamicInputCode = hydrodynamicInputCode
        self.addedMassTanDir = addedMassTanDir
        self.addedMassNormDir = addedMassNormDir
        self.dampingNormDir = dampingNormDir
        self.normalDirectionScaling = normalDirectionScaling
        self.tangentialDirectionScaling = tangentialDirectionScaling
        self.cdt = cdt
        self.cdn = cdn
        self.cmt = cmt
        self.cmn = cmn
        self.cdtl = cdtl
        self.cdnl = cdnl
        self.cdx = cdx
        self.cdy = cdy
        self.amx = amx
        self.amy = amy
        self.cdlx = cdlx
        self.cdly = cdly
        self.hydrodynamicRadiationInputCode = hydrodynamicRadiationInputCode
        self.massDampingSpecification = massDampingSpecification
        self.stiffnessDampingSpecification = stiffnessDampingSpecification
        self.axialDampingSpecification = axialDampingSpecification
        self.massDamping = None
        self.axialDamping = None
        self.temperature = temperature
        self.alpha = alpha
        self.beta = beta
        self.defaultExpansion = defaultExpansion
        self.tensionCapacity = tensionCapacity
        self.maxCurvature = maxCurvature
        self.cdax = cdax
        self.cday = cday
        self.cdaz = cdaz
        self.aerodynamicInputCode = aerodynamicInputCode
        self.aerodynamicDiameter = aerodynamicDiameter
        self.vivCoefficients = None
        self.pipeDiameter = pipeDiameter
        self.pipeThickness = pipeThickness
        self.materialDensity = materialDensity
        self.extCoatingThickness = extCoatingThickness
        self.extCoatingDensity = extCoatingDensity
        self.extContactRadius = extContactRadius
        self.intContactRadius = intContactRadius
        self.materialProperties = None
        self.calculateBeta = calculateBeta
        self.diameterType = diameterType
        self.coupledBendingTorsion = coupledBendingTorsion
        self.stiffnessDamping = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThinWalledPipeBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def staticFriction(self) -> float:
        """Static friction force corresponding to elongation"""
        return self.__staticFriction

    @staticFriction.setter
    def staticFriction(self, value: float):
        """Set staticFriction"""
        self.__staticFriction = float(value)

    @property
    def staticElongation(self) -> float:
        """Relative elongation"""
        return self.__staticElongation

    @staticElongation.setter
    def staticElongation(self, value: float):
        """Set staticElongation"""
        self.__staticElongation = float(value)

    @property
    def dynamicFriction(self) -> float:
        """Dynamic friction force corresponding to elongation"""
        return self.__dynamicFriction

    @dynamicFriction.setter
    def dynamicFriction(self, value: float):
        """Set dynamicFriction"""
        self.__dynamicFriction = float(value)

    @property
    def dynamicElongation(self) -> float:
        """Relative elongation"""
        return self.__dynamicElongation

    @dynamicElongation.setter
    def dynamicElongation(self, value: float):
        """Set dynamicElongation"""
        self.__dynamicElongation = float(value)

    @property
    def axialFriction(self) -> bool:
        """Local axial friction model"""
        return self.__axialFriction

    @axialFriction.setter
    def axialFriction(self, value: bool):
        """Set axialFriction"""
        self.__axialFriction = bool(value)

    @property
    def scfkSpecification(self) -> bool:
        """Scaling of Froude-Krylov term in Morison’s equation in normal direction"""
        return self.__scfkSpecification

    @scfkSpecification.setter
    def scfkSpecification(self, value: bool):
        """Set scfkSpecification"""
        self.__scfkSpecification = bool(value)

    @property
    def loadFormulation(self) -> LoadFormulation:
        """"""
        return self.__loadFormulation

    @loadFormulation.setter
    def loadFormulation(self, value: LoadFormulation):
        """Set loadFormulation"""
        self.__loadFormulation = value

    @property
    def hydrodynamicDiameter(self) -> float:
        """Hydrodynamic diameter"""
        return self.__hydrodynamicDiameter

    @hydrodynamicDiameter.setter
    def hydrodynamicDiameter(self, value: float):
        """Set hydrodynamicDiameter"""
        self.__hydrodynamicDiameter = float(value)

    @property
    def hydrodynamicInputCode(self) -> HydrodynamicInputCode:
        """Hydrodynamic input code"""
        return self.__hydrodynamicInputCode

    @hydrodynamicInputCode.setter
    def hydrodynamicInputCode(self, value: HydrodynamicInputCode):
        """Set hydrodynamicInputCode"""
        self.__hydrodynamicInputCode = value

    @property
    def addedMassTanDir(self) -> float:
        """Added mass in tangential direction"""
        return self.__addedMassTanDir

    @addedMassTanDir.setter
    def addedMassTanDir(self, value: float):
        """Set addedMassTanDir"""
        self.__addedMassTanDir = float(value)

    @property
    def addedMassNormDir(self) -> float:
        """Added mass in normal direction"""
        return self.__addedMassNormDir

    @addedMassNormDir.setter
    def addedMassNormDir(self, value: float):
        """Set addedMassNormDir"""
        self.__addedMassNormDir = float(value)

    @property
    def dampingNormDir(self) -> float:
        """Damping coefficients in normal direction"""
        return self.__dampingNormDir

    @dampingNormDir.setter
    def dampingNormDir(self, value: float):
        """Set dampingNormDir"""
        self.__dampingNormDir = float(value)

    @property
    def normalDirectionScaling(self) -> float:
        """Scaling factor for Froude-Krylov term in Morison’s equation in normal direction"""
        return self.__normalDirectionScaling

    @normalDirectionScaling.setter
    def normalDirectionScaling(self, value: float):
        """Set normalDirectionScaling"""
        self.__normalDirectionScaling = float(value)

    @property
    def tangentialDirectionScaling(self) -> float:
        """Scale for Froude-Krylov term in Morison’s equation in tangential direction"""
        return self.__tangentialDirectionScaling

    @tangentialDirectionScaling.setter
    def tangentialDirectionScaling(self, value: float):
        """Set tangentialDirectionScaling"""
        self.__tangentialDirectionScaling = float(value)

    @property
    def cdt(self) -> float:
        """Quadratic drag coefficient in tangential direction."""
        return self.__cdt

    @cdt.setter
    def cdt(self, value: float):
        """Set cdt"""
        self.__cdt = float(value)

    @property
    def cdn(self) -> float:
        """Quadratic drag coefficient in normal direction."""
        return self.__cdn

    @cdn.setter
    def cdn(self, value: float):
        """Set cdn"""
        self.__cdn = float(value)

    @property
    def cmt(self) -> float:
        """Added mass per unit length in tangential direction."""
        return self.__cmt

    @cmt.setter
    def cmt(self, value: float):
        """Set cmt"""
        self.__cmt = float(value)

    @property
    def cmn(self) -> float:
        """Added mass per unit length in normal direction."""
        return self.__cmn

    @cmn.setter
    def cmn(self, value: float):
        """Set cmn"""
        self.__cmn = float(value)

    @property
    def cdtl(self) -> float:
        """Linear drag force coefficient in tangential direction."""
        return self.__cdtl

    @cdtl.setter
    def cdtl(self, value: float):
        """Set cdtl"""
        self.__cdtl = float(value)

    @property
    def cdnl(self) -> float:
        """Linear drag force coefficient in normal direction."""
        return self.__cdnl

    @cdnl.setter
    def cdnl(self, value: float):
        """Set cdnl"""
        self.__cdnl = float(value)

    @property
    def cdx(self) -> float:
        """Quadratic drag coefficient in tangential direction."""
        return self.__cdx

    @cdx.setter
    def cdx(self, value: float):
        """Set cdx"""
        self.__cdx = float(value)

    @property
    def cdy(self) -> float:
        """Quadratic drag coefficient in normal direction."""
        return self.__cdy

    @cdy.setter
    def cdy(self, value: float):
        """Set cdy"""
        self.__cdy = float(value)

    @property
    def amx(self) -> float:
        """Added mass per unit length in tangential direction."""
        return self.__amx

    @amx.setter
    def amx(self, value: float):
        """Set amx"""
        self.__amx = float(value)

    @property
    def amy(self) -> float:
        """Added mass per unit length in normal direction."""
        return self.__amy

    @amy.setter
    def amy(self, value: float):
        """Set amy"""
        self.__amy = float(value)

    @property
    def cdlx(self) -> float:
        """Linear drag force coefficient in tangential direction."""
        return self.__cdlx

    @cdlx.setter
    def cdlx(self, value: float):
        """Set cdlx"""
        self.__cdlx = float(value)

    @property
    def cdly(self) -> float:
        """Linear drag force coefficient in normal direction."""
        return self.__cdly

    @cdly.setter
    def cdly(self, value: float):
        """Set cdly"""
        self.__cdly = float(value)

    @property
    def hydrodynamicRadiationInputCode(self) -> HydrodynamicInputCode:
        """Code for input of simplified radiation force coefficients"""
        return self.__hydrodynamicRadiationInputCode

    @hydrodynamicRadiationInputCode.setter
    def hydrodynamicRadiationInputCode(self, value: HydrodynamicInputCode):
        """Set hydrodynamicRadiationInputCode"""
        self.__hydrodynamicRadiationInputCode = value

    @property
    def massDampingSpecification(self) -> bool:
        """Mass proportional Rayleigh damping"""
        return self.__massDampingSpecification

    @massDampingSpecification.setter
    def massDampingSpecification(self, value: bool):
        """Set massDampingSpecification"""
        self.__massDampingSpecification = bool(value)

    @property
    def stiffnessDampingSpecification(self) -> bool:
        """Stiffness proportional Rayleigh damping"""
        return self.__stiffnessDampingSpecification

    @stiffnessDampingSpecification.setter
    def stiffnessDampingSpecification(self, value: bool):
        """Set stiffnessDampingSpecification"""
        self.__stiffnessDampingSpecification = bool(value)

    @property
    def axialDampingSpecification(self) -> bool:
        """Local axial damping model"""
        return self.__axialDampingSpecification

    @axialDampingSpecification.setter
    def axialDampingSpecification(self, value: bool):
        """Set axialDampingSpecification"""
        self.__axialDampingSpecification = bool(value)

    @property
    def massDamping(self) -> CRSMassDamping:
        """"""
        return self.__massDamping

    @massDamping.setter
    def massDamping(self, value: CRSMassDamping):
        """Set massDamping"""
        self.__massDamping = value

    @property
    def axialDamping(self) -> CRSAxialDamping:
        """"""
        return self.__axialDamping

    @axialDamping.setter
    def axialDamping(self, value: CRSAxialDamping):
        """Set axialDamping"""
        self.__axialDamping = value

    @property
    def temperature(self) -> float:
        """Temperature at which the specification applies"""
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        """Set temperature"""
        self.__temperature = float(value)

    @property
    def alpha(self) -> float:
        """Thermal expansion coefficient"""
        return self.__alpha

    @alpha.setter
    def alpha(self, value: float):
        """Set alpha"""
        self.__alpha = float(value)

    @property
    def beta(self) -> float:
        """Pressure expansion coefficient"""
        return self.__beta

    @beta.setter
    def beta(self, value: float):
        """Set beta"""
        self.__beta = float(value)

    @property
    def defaultExpansion(self) -> bool:
        """Use default thermal and pressure expansion settings"""
        return self.__defaultExpansion

    @defaultExpansion.setter
    def defaultExpansion(self, value: bool):
        """Set defaultExpansion"""
        self.__defaultExpansion = bool(value)

    @property
    def tensionCapacity(self) -> float:
        """Tension capacity"""
        return self.__tensionCapacity

    @tensionCapacity.setter
    def tensionCapacity(self, value: float):
        """Set tensionCapacity"""
        self.__tensionCapacity = float(value)

    @property
    def maxCurvature(self) -> float:
        """Maximum curvature"""
        return self.__maxCurvature

    @maxCurvature.setter
    def maxCurvature(self, value: float):
        """Set maxCurvature"""
        self.__maxCurvature = float(value)

    @property
    def cdax(self) -> float:
        """Quadratic aerodynamic drag force coefficient per unit length in tangential direction"""
        return self.__cdax

    @cdax.setter
    def cdax(self, value: float):
        """Set cdax"""
        self.__cdax = float(value)

    @property
    def cday(self) -> float:
        """Quadratic aerodynamic drag force coefficient per unit length in normal direction"""
        return self.__cday

    @cday.setter
    def cday(self, value: float):
        """Set cday"""
        self.__cday = float(value)

    @property
    def cdaz(self) -> float:
        """Quadratic aerodynamic drag force coefficient per unit length in z direction"""
        return self.__cdaz

    @cdaz.setter
    def cdaz(self, value: float):
        """Set cdaz"""
        self.__cdaz = float(value)

    @property
    def aerodynamicInputCode(self) -> AerodynamicInputCode:
        """Aerodynamic input code"""
        return self.__aerodynamicInputCode

    @aerodynamicInputCode.setter
    def aerodynamicInputCode(self, value: AerodynamicInputCode):
        """Set aerodynamicInputCode"""
        self.__aerodynamicInputCode = value

    @property
    def aerodynamicDiameter(self) -> float:
        """Aerodynamic diameter"""
        return self.__aerodynamicDiameter

    @aerodynamicDiameter.setter
    def aerodynamicDiameter(self, value: float):
        """Set aerodynamicDiameter"""
        self.__aerodynamicDiameter = float(value)

    @property
    def vivCoefficients(self) -> TimeDomainVIVLoadCoefficients:
        """"""
        return self.__vivCoefficients

    @vivCoefficients.setter
    def vivCoefficients(self, value: TimeDomainVIVLoadCoefficients):
        """Set vivCoefficients"""
        self.__vivCoefficients = value

    @property
    def pipeDiameter(self) -> float:
        """Diameter of pipe."""
        return self.__pipeDiameter

    @pipeDiameter.setter
    def pipeDiameter(self, value: float):
        """Set pipeDiameter"""
        self.__pipeDiameter = float(value)

    @property
    def pipeThickness(self) -> float:
        """Thickness of pipe"""
        return self.__pipeThickness

    @pipeThickness.setter
    def pipeThickness(self, value: float):
        """Set pipeThickness"""
        self.__pipeThickness = float(value)

    @property
    def materialDensity(self) -> float:
        """Density of pipe material"""
        return self.__materialDensity

    @materialDensity.setter
    def materialDensity(self, value: float):
        """Set materialDensity"""
        self.__materialDensity = float(value)

    @property
    def extCoatingThickness(self) -> float:
        """Thickness of external coating"""
        return self.__extCoatingThickness

    @extCoatingThickness.setter
    def extCoatingThickness(self, value: float):
        """Set extCoatingThickness"""
        self.__extCoatingThickness = float(value)

    @property
    def extCoatingDensity(self) -> float:
        """Density of external coating"""
        return self.__extCoatingDensity

    @extCoatingDensity.setter
    def extCoatingDensity(self, value: float):
        """Set extCoatingDensity"""
        self.__extCoatingDensity = float(value)

    @property
    def extContactRadius(self) -> float:
        """External contact radius"""
        return self.__extContactRadius

    @extContactRadius.setter
    def extContactRadius(self, value: float):
        """Set extContactRadius"""
        self.__extContactRadius = float(value)

    @property
    def intContactRadius(self) -> float:
        """Inner contact radius"""
        return self.__intContactRadius

    @intContactRadius.setter
    def intContactRadius(self, value: float):
        """Set intContactRadius"""
        self.__intContactRadius = float(value)

    @property
    def materialProperties(self) -> ThinWalledPipeMaterial:
        """"""
        return self.__materialProperties

    @materialProperties.setter
    def materialProperties(self, value: ThinWalledPipeMaterial):
        """Set materialProperties"""
        self.__materialProperties = value

    @property
    def calculateBeta(self) -> bool:
        """Let RIFLEX calculate beta"""
        return self.__calculateBeta

    @calculateBeta.setter
    def calculateBeta(self, value: bool):
        """Set calculateBeta"""
        self.__calculateBeta = bool(value)

    @property
    def diameterType(self) -> InnerOuter:
        """Inner or outer diameter"""
        return self.__diameterType

    @diameterType.setter
    def diameterType(self, value: InnerOuter):
        """Set diameterType"""
        self.__diameterType = value

    @property
    def coupledBendingTorsion(self) -> bool:
        """Geometric stiffness coupling between bending and torsion"""
        return self.__coupledBendingTorsion

    @coupledBendingTorsion.setter
    def coupledBendingTorsion(self, value: bool):
        """Set coupledBendingTorsion"""
        self.__coupledBendingTorsion = bool(value)

    @property
    def stiffnessDamping(self) -> CRSStiffnessDamping:
        """"""
        return self.__stiffnessDamping

    @stiffnessDamping.setter
    def stiffnessDamping(self, value: CRSStiffnessDamping):
        """Set stiffnessDamping"""
        self.__stiffnessDamping = value
