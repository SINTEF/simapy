# This an autogenerated file
# 
# Generated with DoubleSymmetricCrossSection
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.doublesymmetriccrosssection import DoubleSymmetricCrossSectionBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .aerodynamicforcetype import AerodynamicForceType
from .aerodynamicinputcode import AerodynamicInputCode
from .axialstiffness import AxialStiffness
from .axialstiffnessitem import AxialStiffnessItem
from .barbeam import BarBeam
from .bendingstiffness import BendingStiffness
from .bendingstiffnessyz_item import BendingStiffnessYZ_Item
from .crosssection import CrossSection
from .crsaxialdamping import CRSAxialDamping
from .crsaxialfrictionmodel import CRSAxialFrictionModel
from .crsmassdamping import CRSMassDamping
from .doublesymmetriccrosssectionmassvolume import DoubleSymmetricCrossSectionMassVolume
from .doublesymmetricstiffnessdamping import DoubleSymmetricStiffnessDamping
from .hydrodynamicinputcode import HydrodynamicInputCode
from .loadformulation import LoadFormulation
from .torsionstiffness import TorsionStiffness
from .torsionstiffnessitem import TorsionStiffnessItem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..windturbine import Airfoil

class DoubleSymmetricCrossSection(CrossSection,CRSAxialFrictionModel):
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
    cdx : float
         Quadratic drag force coefficient per unit length in tangential direction(default 0.0)
    cdy : float
         Quadratic drag force coefficient per unit length in local y-direction(default 0.0)
    cdz : float
         Quadratic drag force coefficient per unit length local z-direction(default 0.0)
    amx : float
         Added mass per unit length in tangential direction(default 0.0)
    amy : float
         Added mass per unit length in local y-direction(default 0.0)
    amz : float
         Added mass per unit length in local z-direction(default 0.0)
    addedMass : float
         Added mass per unit length for torsional rotation(default 0.0)
    cdlx : float
         Linear drag force coefficient per unit length in tangential direction(default 0.0)
    cdly : float
         Linear drag force coefficient per unit length in local y-direction(default 0.0)
    cdlz : float
         Linear drag force coefficient per unit length in local z-direction(default 0.0)
    cdt : float
         Quadratic drag coefficient in tangential direction.(default 0.0)
    cdn : float
         Quadratic drag coefficient in normal direction.(default 0.0)
    cdnz : float
         Quadratic drag coefficient in normal direction.(default 0.0)
    massDampingSpecification : bool
         Mass proportional Rayleigh damping(default False)
    stiffnessDampingSpecification : bool
         Stiffness proportional Rayleigh damping(default False)
    axialDampingSpecification : bool
         Local axial damping model(default False)
    massDamping : CRSMassDamping
    axialDamping : CRSAxialDamping
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
    temperature : float
         Temperature at which the specification applies(default 0.0)
    pressureDependency : int
         Pressure dependency parameter related to bending moment(default 0)
    axialStiffness : float
         Axial stiffness(default 0.0)
    tensionCapacity : float
         Tension capacity(default 0.0)
    maxCurvatureY : float
         Maximum curvature around local y-axis(default 0.0)
    maxCurvatureZ : float
         Maximum curvature around local z-axis(default 0.0)
    airfoil : Airfoil
    chordLength : float
         (default 0.0)
    foilOriginY : float
         Y-coordinate of foil origin(default 0.0)
    foilOriginZ : float
         Z-coordinate of foil origin(default 0.0)
    foilInclination : float
         Inclination of foil system in the local cross section (strength) system.(default 0.0)
    aerodynamicForceType : AerodynamicForceType
    coupledBendingTorsion : bool
         Geometric stiffness coupling between bending and torsion(default False)
    barBeam : BarBeam
         Cross section type
    massVolume : DoubleSymmetricCrossSectionMassVolume
    axialStiffnessInput : AxialStiffness
         Axial stiffness input specification
    bendingStiffnessInput : BendingStiffness
         Bending stiffness input specification
    torsionStiffnessInput : TorsionStiffness
         Torsion stiffness input specification
    axialStiffnessCharacteristics : List[AxialStiffnessItem]
    bendingStiffnessCharacteristics : List[BendingStiffnessYZ_Item]
    torsionStiffnessCharacteristics : List[TorsionStiffnessItem]
    negativeTorsionStiffness : float
         Torsion stiffness for negative twist.(default 0.0)
    positiveTorsionStiffness : float
         Torsion stiffness for positive twist.(default 0.0)
    bendingStiffnessY : float
         Bending stiffness around y-axis(default 0.0)
    bendingStiffnessZ : float
         Bending stiffness around z-axis(default 0.0)
    shearStiffnessZ : float
         Shear stiffness in Z-direction(default 0.0)
    shearStiffnessY : float
         Shear stiffness in Y-direction(default 0.0)
    hydrodynamicRadiationInputCode : HydrodynamicInputCode
         Code for input of simplified radiation force coefficients
    stiffnessDamping : DoubleSymmetricStiffnessDamping
    """

    def __init__(self , description="", staticFriction=0.0, staticElongation=0.0, dynamicFriction=0.0, dynamicElongation=0.0, axialFriction=False, scfkSpecification=False, loadFormulation=LoadFormulation.MORISON, hydrodynamicDiameter=0.0, hydrodynamicInputCode=HydrodynamicInputCode.DIMENSIONAL, addedMassTanDir=0.0, addedMassNormDir=0.0, dampingNormDir=0.0, normalDirectionScaling=1.0, tangentialDirectionScaling=1.0, cdx=0.0, cdy=0.0, cdz=0.0, amx=0.0, amy=0.0, amz=0.0, addedMass=0.0, cdlx=0.0, cdly=0.0, cdlz=0.0, cdt=0.0, cdn=0.0, cdnz=0.0, massDampingSpecification=False, stiffnessDampingSpecification=False, axialDampingSpecification=False, cdax=0.0, cday=0.0, cdaz=0.0, aerodynamicInputCode=AerodynamicInputCode.NONE, aerodynamicDiameter=0.0, temperature=0.0, pressureDependency=0, axialStiffness=0.0, tensionCapacity=0.0, maxCurvatureY=0.0, maxCurvatureZ=0.0, chordLength=0.0, foilOriginY=0.0, foilOriginZ=0.0, foilInclination=0.0, aerodynamicForceType=AerodynamicForceType.NONE, coupledBendingTorsion=False, barBeam=BarBeam.BAR, axialStiffnessInput=AxialStiffness.CONSTANT, bendingStiffnessInput=BendingStiffness.CONSTANT, torsionStiffnessInput=TorsionStiffness.CONSTANT, negativeTorsionStiffness=0.0, positiveTorsionStiffness=0.0, bendingStiffnessY=0.0, bendingStiffnessZ=0.0, shearStiffnessZ=0.0, shearStiffnessY=0.0, hydrodynamicRadiationInputCode=HydrodynamicInputCode.DIMENSIONAL, **kwargs):
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
        self.cdx = cdx
        self.cdy = cdy
        self.cdz = cdz
        self.amx = amx
        self.amy = amy
        self.amz = amz
        self.addedMass = addedMass
        self.cdlx = cdlx
        self.cdly = cdly
        self.cdlz = cdlz
        self.cdt = cdt
        self.cdn = cdn
        self.cdnz = cdnz
        self.massDampingSpecification = massDampingSpecification
        self.stiffnessDampingSpecification = stiffnessDampingSpecification
        self.axialDampingSpecification = axialDampingSpecification
        self.massDamping = None
        self.axialDamping = None
        self.cdax = cdax
        self.cday = cday
        self.cdaz = cdaz
        self.aerodynamicInputCode = aerodynamicInputCode
        self.aerodynamicDiameter = aerodynamicDiameter
        self.temperature = temperature
        self.pressureDependency = pressureDependency
        self.axialStiffness = axialStiffness
        self.tensionCapacity = tensionCapacity
        self.maxCurvatureY = maxCurvatureY
        self.maxCurvatureZ = maxCurvatureZ
        self.airfoil = None
        self.chordLength = chordLength
        self.foilOriginY = foilOriginY
        self.foilOriginZ = foilOriginZ
        self.foilInclination = foilInclination
        self.aerodynamicForceType = aerodynamicForceType
        self.coupledBendingTorsion = coupledBendingTorsion
        self.barBeam = barBeam
        self.massVolume = None
        self.axialStiffnessInput = axialStiffnessInput
        self.bendingStiffnessInput = bendingStiffnessInput
        self.torsionStiffnessInput = torsionStiffnessInput
        self.axialStiffnessCharacteristics = list()
        self.bendingStiffnessCharacteristics = list()
        self.torsionStiffnessCharacteristics = list()
        self.negativeTorsionStiffness = negativeTorsionStiffness
        self.positiveTorsionStiffness = positiveTorsionStiffness
        self.bendingStiffnessY = bendingStiffnessY
        self.bendingStiffnessZ = bendingStiffnessZ
        self.shearStiffnessZ = shearStiffnessZ
        self.shearStiffnessY = shearStiffnessY
        self.hydrodynamicRadiationInputCode = hydrodynamicRadiationInputCode
        self.stiffnessDamping = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DoubleSymmetricCrossSectionBlueprint()


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
    def cdx(self) -> float:
        """Quadratic drag force coefficient per unit length in tangential direction"""
        return self.__cdx

    @cdx.setter
    def cdx(self, value: float):
        """Set cdx"""
        self.__cdx = float(value)

    @property
    def cdy(self) -> float:
        """Quadratic drag force coefficient per unit length in local y-direction"""
        return self.__cdy

    @cdy.setter
    def cdy(self, value: float):
        """Set cdy"""
        self.__cdy = float(value)

    @property
    def cdz(self) -> float:
        """Quadratic drag force coefficient per unit length local z-direction"""
        return self.__cdz

    @cdz.setter
    def cdz(self, value: float):
        """Set cdz"""
        self.__cdz = float(value)

    @property
    def amx(self) -> float:
        """Added mass per unit length in tangential direction"""
        return self.__amx

    @amx.setter
    def amx(self, value: float):
        """Set amx"""
        self.__amx = float(value)

    @property
    def amy(self) -> float:
        """Added mass per unit length in local y-direction"""
        return self.__amy

    @amy.setter
    def amy(self, value: float):
        """Set amy"""
        self.__amy = float(value)

    @property
    def amz(self) -> float:
        """Added mass per unit length in local z-direction"""
        return self.__amz

    @amz.setter
    def amz(self, value: float):
        """Set amz"""
        self.__amz = float(value)

    @property
    def addedMass(self) -> float:
        """Added mass per unit length for torsional rotation"""
        return self.__addedMass

    @addedMass.setter
    def addedMass(self, value: float):
        """Set addedMass"""
        self.__addedMass = float(value)

    @property
    def cdlx(self) -> float:
        """Linear drag force coefficient per unit length in tangential direction"""
        return self.__cdlx

    @cdlx.setter
    def cdlx(self, value: float):
        """Set cdlx"""
        self.__cdlx = float(value)

    @property
    def cdly(self) -> float:
        """Linear drag force coefficient per unit length in local y-direction"""
        return self.__cdly

    @cdly.setter
    def cdly(self, value: float):
        """Set cdly"""
        self.__cdly = float(value)

    @property
    def cdlz(self) -> float:
        """Linear drag force coefficient per unit length in local z-direction"""
        return self.__cdlz

    @cdlz.setter
    def cdlz(self, value: float):
        """Set cdlz"""
        self.__cdlz = float(value)

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
    def cdnz(self) -> float:
        """Quadratic drag coefficient in normal direction."""
        return self.__cdnz

    @cdnz.setter
    def cdnz(self, value: float):
        """Set cdnz"""
        self.__cdnz = float(value)

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
    def temperature(self) -> float:
        """Temperature at which the specification applies"""
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        """Set temperature"""
        self.__temperature = float(value)

    @property
    def pressureDependency(self) -> int:
        """Pressure dependency parameter related to bending moment"""
        return self.__pressureDependency

    @pressureDependency.setter
    def pressureDependency(self, value: int):
        """Set pressureDependency"""
        self.__pressureDependency = int(value)

    @property
    def axialStiffness(self) -> float:
        """Axial stiffness"""
        return self.__axialStiffness

    @axialStiffness.setter
    def axialStiffness(self, value: float):
        """Set axialStiffness"""
        self.__axialStiffness = float(value)

    @property
    def tensionCapacity(self) -> float:
        """Tension capacity"""
        return self.__tensionCapacity

    @tensionCapacity.setter
    def tensionCapacity(self, value: float):
        """Set tensionCapacity"""
        self.__tensionCapacity = float(value)

    @property
    def maxCurvatureY(self) -> float:
        """Maximum curvature around local y-axis"""
        return self.__maxCurvatureY

    @maxCurvatureY.setter
    def maxCurvatureY(self, value: float):
        """Set maxCurvatureY"""
        self.__maxCurvatureY = float(value)

    @property
    def maxCurvatureZ(self) -> float:
        """Maximum curvature around local z-axis"""
        return self.__maxCurvatureZ

    @maxCurvatureZ.setter
    def maxCurvatureZ(self, value: float):
        """Set maxCurvatureZ"""
        self.__maxCurvatureZ = float(value)

    @property
    def airfoil(self) -> Airfoil:
        """"""
        return self.__airfoil

    @airfoil.setter
    def airfoil(self, value: Airfoil):
        """Set airfoil"""
        self.__airfoil = value

    @property
    def chordLength(self) -> float:
        """"""
        return self.__chordLength

    @chordLength.setter
    def chordLength(self, value: float):
        """Set chordLength"""
        self.__chordLength = float(value)

    @property
    def foilOriginY(self) -> float:
        """Y-coordinate of foil origin"""
        return self.__foilOriginY

    @foilOriginY.setter
    def foilOriginY(self, value: float):
        """Set foilOriginY"""
        self.__foilOriginY = float(value)

    @property
    def foilOriginZ(self) -> float:
        """Z-coordinate of foil origin"""
        return self.__foilOriginZ

    @foilOriginZ.setter
    def foilOriginZ(self, value: float):
        """Set foilOriginZ"""
        self.__foilOriginZ = float(value)

    @property
    def foilInclination(self) -> float:
        """Inclination of foil system in the local cross section (strength) system."""
        return self.__foilInclination

    @foilInclination.setter
    def foilInclination(self, value: float):
        """Set foilInclination"""
        self.__foilInclination = float(value)

    @property
    def aerodynamicForceType(self) -> AerodynamicForceType:
        """"""
        return self.__aerodynamicForceType

    @aerodynamicForceType.setter
    def aerodynamicForceType(self, value: AerodynamicForceType):
        """Set aerodynamicForceType"""
        self.__aerodynamicForceType = value

    @property
    def coupledBendingTorsion(self) -> bool:
        """Geometric stiffness coupling between bending and torsion"""
        return self.__coupledBendingTorsion

    @coupledBendingTorsion.setter
    def coupledBendingTorsion(self, value: bool):
        """Set coupledBendingTorsion"""
        self.__coupledBendingTorsion = bool(value)

    @property
    def barBeam(self) -> BarBeam:
        """Cross section type"""
        return self.__barBeam

    @barBeam.setter
    def barBeam(self, value: BarBeam):
        """Set barBeam"""
        self.__barBeam = value

    @property
    def massVolume(self) -> DoubleSymmetricCrossSectionMassVolume:
        """"""
        return self.__massVolume

    @massVolume.setter
    def massVolume(self, value: DoubleSymmetricCrossSectionMassVolume):
        """Set massVolume"""
        self.__massVolume = value

    @property
    def axialStiffnessInput(self) -> AxialStiffness:
        """Axial stiffness input specification"""
        return self.__axialStiffnessInput

    @axialStiffnessInput.setter
    def axialStiffnessInput(self, value: AxialStiffness):
        """Set axialStiffnessInput"""
        self.__axialStiffnessInput = value

    @property
    def bendingStiffnessInput(self) -> BendingStiffness:
        """Bending stiffness input specification"""
        return self.__bendingStiffnessInput

    @bendingStiffnessInput.setter
    def bendingStiffnessInput(self, value: BendingStiffness):
        """Set bendingStiffnessInput"""
        self.__bendingStiffnessInput = value

    @property
    def torsionStiffnessInput(self) -> TorsionStiffness:
        """Torsion stiffness input specification"""
        return self.__torsionStiffnessInput

    @torsionStiffnessInput.setter
    def torsionStiffnessInput(self, value: TorsionStiffness):
        """Set torsionStiffnessInput"""
        self.__torsionStiffnessInput = value

    @property
    def axialStiffnessCharacteristics(self) -> List[AxialStiffnessItem]:
        """"""
        return self.__axialStiffnessCharacteristics

    @axialStiffnessCharacteristics.setter
    def axialStiffnessCharacteristics(self, value: List[AxialStiffnessItem]):
        """Set axialStiffnessCharacteristics"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__axialStiffnessCharacteristics = value

    @property
    def bendingStiffnessCharacteristics(self) -> List[BendingStiffnessYZ_Item]:
        """"""
        return self.__bendingStiffnessCharacteristics

    @bendingStiffnessCharacteristics.setter
    def bendingStiffnessCharacteristics(self, value: List[BendingStiffnessYZ_Item]):
        """Set bendingStiffnessCharacteristics"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__bendingStiffnessCharacteristics = value

    @property
    def torsionStiffnessCharacteristics(self) -> List[TorsionStiffnessItem]:
        """"""
        return self.__torsionStiffnessCharacteristics

    @torsionStiffnessCharacteristics.setter
    def torsionStiffnessCharacteristics(self, value: List[TorsionStiffnessItem]):
        """Set torsionStiffnessCharacteristics"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__torsionStiffnessCharacteristics = value

    @property
    def negativeTorsionStiffness(self) -> float:
        """Torsion stiffness for negative twist."""
        return self.__negativeTorsionStiffness

    @negativeTorsionStiffness.setter
    def negativeTorsionStiffness(self, value: float):
        """Set negativeTorsionStiffness"""
        self.__negativeTorsionStiffness = float(value)

    @property
    def positiveTorsionStiffness(self) -> float:
        """Torsion stiffness for positive twist."""
        return self.__positiveTorsionStiffness

    @positiveTorsionStiffness.setter
    def positiveTorsionStiffness(self, value: float):
        """Set positiveTorsionStiffness"""
        self.__positiveTorsionStiffness = float(value)

    @property
    def bendingStiffnessY(self) -> float:
        """Bending stiffness around y-axis"""
        return self.__bendingStiffnessY

    @bendingStiffnessY.setter
    def bendingStiffnessY(self, value: float):
        """Set bendingStiffnessY"""
        self.__bendingStiffnessY = float(value)

    @property
    def bendingStiffnessZ(self) -> float:
        """Bending stiffness around z-axis"""
        return self.__bendingStiffnessZ

    @bendingStiffnessZ.setter
    def bendingStiffnessZ(self, value: float):
        """Set bendingStiffnessZ"""
        self.__bendingStiffnessZ = float(value)

    @property
    def shearStiffnessZ(self) -> float:
        """Shear stiffness in Z-direction"""
        return self.__shearStiffnessZ

    @shearStiffnessZ.setter
    def shearStiffnessZ(self, value: float):
        """Set shearStiffnessZ"""
        self.__shearStiffnessZ = float(value)

    @property
    def shearStiffnessY(self) -> float:
        """Shear stiffness in Y-direction"""
        return self.__shearStiffnessY

    @shearStiffnessY.setter
    def shearStiffnessY(self, value: float):
        """Set shearStiffnessY"""
        self.__shearStiffnessY = float(value)

    @property
    def hydrodynamicRadiationInputCode(self) -> HydrodynamicInputCode:
        """Code for input of simplified radiation force coefficients"""
        return self.__hydrodynamicRadiationInputCode

    @hydrodynamicRadiationInputCode.setter
    def hydrodynamicRadiationInputCode(self, value: HydrodynamicInputCode):
        """Set hydrodynamicRadiationInputCode"""
        self.__hydrodynamicRadiationInputCode = value

    @property
    def stiffnessDamping(self) -> DoubleSymmetricStiffnessDamping:
        """"""
        return self.__stiffnessDamping

    @stiffnessDamping.setter
    def stiffnessDamping(self, value: DoubleSymmetricStiffnessDamping):
        """Set stiffnessDamping"""
        self.__stiffnessDamping = value
