# This an autogenerated file
# 
# Generated with DoubleSymmetricCrossSection
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.doublesymmetriccrosssection import DoubleSymmetricCrossSectionBlueprint
from sima.riflex.aerodynamicforcetype import AerodynamicForceType
from sima.riflex.aerodynamicinputcode import AerodynamicInputCode
from sima.riflex.axialstiffness import AxialStiffness
from sima.riflex.axialstiffnessitem import AxialStiffnessItem
from sima.riflex.barbeam import BarBeam
from sima.riflex.bendingstiffness import BendingStiffness
from sima.riflex.bendingstiffnessyz_item import BendingStiffnessYZ_Item
from sima.riflex.crosssection import CrossSection
from sima.riflex.crsaxialdamping import CRSAxialDamping
from sima.riflex.crsaxialfrictionmodel import CRSAxialFrictionModel
from sima.riflex.crsmassdamping import CRSMassDamping
from sima.riflex.crsstiffnessdamping import CRSStiffnessDamping
from sima.riflex.doublesymmetriccrosssectionmassvolume import DoubleSymmetricCrossSectionMassVolume
from sima.riflex.hydrodynamicinputcode import HydrodynamicInputCode
from sima.riflex.hydrodynamicradiationinputcode import HydrodynamicRadiationInputCode
from sima.riflex.loadformulation import LoadFormulation
from sima.riflex.tangentialfroudekrylovscaling import TangentialFroudeKrylovScaling
from sima.riflex.torsionstiffness import TorsionStiffness
from sima.riflex.torsionstiffnessitem import TorsionStiffnessItem
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.windturbine.airfoil import Airfoil

class DoubleSymmetricCrossSection(CrossSection,CRSAxialFrictionModel):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
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
         Scaling of Froude-Krylov term in Morison’s equation in normal direction(default True)
    loadFormulation : LoadFormulation
    hydrodynamicDiameter : float
         Hydrodynamic diameter(default 0.0)
    addedMassTanDir : float
         Added mass in tangential direction(default 0.0)
    addedMassNormDir : float
         Added mass in normal direction(default 0.0)
    dampingNormDir : float
         Damping coefficients in normal direction(default 0.0)
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
    scfk : float
         Scaling factor for Froude-Krylov term in Morison’s equation in normal direction(default 1.0)
    scfkt : TangentialFroudeKrylovScaling
         Scale for Froude-Krylov term in Morison’s equation in tangential direction
    hydrodynamicInputCode : HydrodynamicInputCode
         Hydrodynamic input code
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
    massDamping : CRSMassDamping
    stiffnessDamping : CRSStiffnessDamping
    axialDamping : CRSAxialDamping
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
    submerged : bool
         Use formulation for partly submerged cross-section(default False)
    bendingStiffnessY : float
         Bending stiffness around y-axis(default 0.0)
    bendingStiffnessZ : float
         Bending stiffness around z-axis(default 0.0)
    shearStiffnessZ : float
         Shear stiffness in Z-direction(default 0.0)
    shearStiffnessY : float
         Shear stiffness in Y-direction(default 0.0)
    hydrodynamicRadiationInputCode : HydrodynamicRadiationInputCode
         Code for input of simplified radiation force coefficients
    """

    def __init__(self , name:str="", description:str="", _id:str="", staticFriction:float=0.0, staticElongation:float=0.0, dynamicFriction:float=0.0, dynamicElongation:float=0.0, axialFriction:bool=False, scfkSpecification:bool=True, loadFormulation:LoadFormulation=LoadFormulation.MORISON, hydrodynamicDiameter:float=0.0, addedMassTanDir:float=0.0, addedMassNormDir:float=0.0, dampingNormDir:float=0.0, cdx:float=0.0, cdy:float=0.0, cdz:float=0.0, amx:float=0.0, amy:float=0.0, amz:float=0.0, addedMass:float=0.0, cdlx:float=0.0, cdly:float=0.0, cdlz:float=0.0, scfk:float=1.0, scfkt:TangentialFroudeKrylovScaling=TangentialFroudeKrylovScaling.ON, hydrodynamicInputCode:HydrodynamicInputCode=HydrodynamicInputCode.DIMENSIONAL, cdt:float=0.0, cdn:float=0.0, cdnz:float=0.0, massDampingSpecification:bool=False, stiffnessDampingSpecification:bool=False, axialDampingSpecification:bool=False, cdax:float=0.0, cday:float=0.0, cdaz:float=0.0, aerodynamicInputCode:AerodynamicInputCode=AerodynamicInputCode.NONE, aerodynamicDiameter:float=0.0, temperature:float=0.0, pressureDependency:int=0, axialStiffness:float=0.0, tensionCapacity:float=0.0, maxCurvatureY:float=0.0, maxCurvatureZ:float=0.0, chordLength:float=0.0, foilOriginY:float=0.0, foilOriginZ:float=0.0, foilInclination:float=0.0, aerodynamicForceType:AerodynamicForceType=AerodynamicForceType.NONE, coupledBendingTorsion:bool=False, barBeam:BarBeam=BarBeam.BAR, axialStiffnessInput:AxialStiffness=AxialStiffness.CONSTANT, bendingStiffnessInput:BendingStiffness=BendingStiffness.CONSTANT, torsionStiffnessInput:TorsionStiffness=TorsionStiffness.CONSTANT, negativeTorsionStiffness:float=0.0, positiveTorsionStiffness:float=0.0, submerged:bool=False, bendingStiffnessY:float=0.0, bendingStiffnessZ:float=0.0, shearStiffnessZ:float=0.0, shearStiffnessY:float=0.0, hydrodynamicRadiationInputCode:HydrodynamicRadiationInputCode=HydrodynamicRadiationInputCode.DIMENSIONAL, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__staticFriction = staticFriction
        self.__staticElongation = staticElongation
        self.__dynamicFriction = dynamicFriction
        self.__dynamicElongation = dynamicElongation
        self.__axialFriction = axialFriction
        self.__scfkSpecification = scfkSpecification
        self.__loadFormulation = loadFormulation
        self.__hydrodynamicDiameter = hydrodynamicDiameter
        self.__addedMassTanDir = addedMassTanDir
        self.__addedMassNormDir = addedMassNormDir
        self.__dampingNormDir = dampingNormDir
        self.__cdx = cdx
        self.__cdy = cdy
        self.__cdz = cdz
        self.__amx = amx
        self.__amy = amy
        self.__amz = amz
        self.__addedMass = addedMass
        self.__cdlx = cdlx
        self.__cdly = cdly
        self.__cdlz = cdlz
        self.__scfk = scfk
        self.__scfkt = scfkt
        self.__hydrodynamicInputCode = hydrodynamicInputCode
        self.__cdt = cdt
        self.__cdn = cdn
        self.__cdnz = cdnz
        self.__massDampingSpecification = massDampingSpecification
        self.__stiffnessDampingSpecification = stiffnessDampingSpecification
        self.__axialDampingSpecification = axialDampingSpecification
        self.__cdax = cdax
        self.__cday = cday
        self.__cdaz = cdaz
        self.__aerodynamicInputCode = aerodynamicInputCode
        self.__aerodynamicDiameter = aerodynamicDiameter
        self.__temperature = temperature
        self.__pressureDependency = pressureDependency
        self.__axialStiffness = axialStiffness
        self.__tensionCapacity = tensionCapacity
        self.__maxCurvatureY = maxCurvatureY
        self.__maxCurvatureZ = maxCurvatureZ
        self.__massDamping = CRSMassDamping()
        self.__stiffnessDamping = CRSStiffnessDamping()
        self.__axialDamping = CRSAxialDamping()
        self.__airfoil = None
        self.__chordLength = chordLength
        self.__foilOriginY = foilOriginY
        self.__foilOriginZ = foilOriginZ
        self.__foilInclination = foilInclination
        self.__aerodynamicForceType = aerodynamicForceType
        self.__coupledBendingTorsion = coupledBendingTorsion
        self.__barBeam = barBeam
        self.__massVolume = DoubleSymmetricCrossSectionMassVolume()
        self.__axialStiffnessInput = axialStiffnessInput
        self.__bendingStiffnessInput = bendingStiffnessInput
        self.__torsionStiffnessInput = torsionStiffnessInput
        self.__axialStiffnessCharacteristics = list()
        self.__bendingStiffnessCharacteristics = list()
        self.__torsionStiffnessCharacteristics = list()
        self.__negativeTorsionStiffness = negativeTorsionStiffness
        self.__positiveTorsionStiffness = positiveTorsionStiffness
        self.__submerged = submerged
        self.__bendingStiffnessY = bendingStiffnessY
        self.__bendingStiffnessZ = bendingStiffnessZ
        self.__shearStiffnessZ = shearStiffnessZ
        self.__shearStiffnessY = shearStiffnessY
        self.__hydrodynamicRadiationInputCode = hydrodynamicRadiationInputCode
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DoubleSymmetricCrossSectionBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

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
    def scfk(self) -> float:
        """Scaling factor for Froude-Krylov term in Morison’s equation in normal direction"""
        return self.__scfk

    @scfk.setter
    def scfk(self, value: float):
        """Set scfk"""
        self.__scfk = float(value)

    @property
    def scfkt(self) -> TangentialFroudeKrylovScaling:
        """Scale for Froude-Krylov term in Morison’s equation in tangential direction"""
        return self.__scfkt

    @scfkt.setter
    def scfkt(self, value: TangentialFroudeKrylovScaling):
        """Set scfkt"""
        self.__scfkt = value

    @property
    def hydrodynamicInputCode(self) -> HydrodynamicInputCode:
        """Hydrodynamic input code"""
        return self.__hydrodynamicInputCode

    @hydrodynamicInputCode.setter
    def hydrodynamicInputCode(self, value: HydrodynamicInputCode):
        """Set hydrodynamicInputCode"""
        self.__hydrodynamicInputCode = value

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
    def massDamping(self) -> CRSMassDamping:
        """"""
        return self.__massDamping

    @massDamping.setter
    def massDamping(self, value: CRSMassDamping):
        """Set massDamping"""
        self.__massDamping = value

    @property
    def stiffnessDamping(self) -> CRSStiffnessDamping:
        """"""
        return self.__stiffnessDamping

    @stiffnessDamping.setter
    def stiffnessDamping(self, value: CRSStiffnessDamping):
        """Set stiffnessDamping"""
        self.__stiffnessDamping = value

    @property
    def axialDamping(self) -> CRSAxialDamping:
        """"""
        return self.__axialDamping

    @axialDamping.setter
    def axialDamping(self, value: CRSAxialDamping):
        """Set axialDamping"""
        self.__axialDamping = value

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
            raise Exception("Expected sequense, but was " , type(value))
        self.__axialStiffnessCharacteristics = value

    @property
    def bendingStiffnessCharacteristics(self) -> List[BendingStiffnessYZ_Item]:
        """"""
        return self.__bendingStiffnessCharacteristics

    @bendingStiffnessCharacteristics.setter
    def bendingStiffnessCharacteristics(self, value: List[BendingStiffnessYZ_Item]):
        """Set bendingStiffnessCharacteristics"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__bendingStiffnessCharacteristics = value

    @property
    def torsionStiffnessCharacteristics(self) -> List[TorsionStiffnessItem]:
        """"""
        return self.__torsionStiffnessCharacteristics

    @torsionStiffnessCharacteristics.setter
    def torsionStiffnessCharacteristics(self, value: List[TorsionStiffnessItem]):
        """Set torsionStiffnessCharacteristics"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
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
    def submerged(self) -> bool:
        """Use formulation for partly submerged cross-section"""
        return self.__submerged

    @submerged.setter
    def submerged(self, value: bool):
        """Set submerged"""
        self.__submerged = bool(value)

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
    def hydrodynamicRadiationInputCode(self) -> HydrodynamicRadiationInputCode:
        """Code for input of simplified radiation force coefficients"""
        return self.__hydrodynamicRadiationInputCode

    @hydrodynamicRadiationInputCode.setter
    def hydrodynamicRadiationInputCode(self, value: HydrodynamicRadiationInputCode):
        """Set hydrodynamicRadiationInputCode"""
        self.__hydrodynamicRadiationInputCode = value
