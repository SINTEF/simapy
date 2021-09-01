# This an autogenerated file
# 
# Generated with GeneralCrossSection
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.generalcrosssection import GeneralCrossSectionBlueprint
from sima.riflex.aerodynamicforcetype import AerodynamicForceType
from sima.riflex.aerodynamicinputcode import AerodynamicInputCode
from sima.riflex.crosssection import CrossSection
from sima.riflex.crsaxialdamping import CRSAxialDamping
from sima.riflex.crsaxialfrictionmodel import CRSAxialFrictionModel
from sima.riflex.crsmassdamping import CRSMassDamping
from sima.riflex.crsstiffnessdamping import CRSStiffnessDamping
from sima.riflex.hydrodynamicinputcode import HydrodynamicInputCode
from sima.riflex.loadformulation import LoadFormulation
from sima.riflex.tangentialfroudekrylovscaling import TangentialFroudeKrylovScaling
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.windturbine.airfoil import Airfoil

class GeneralCrossSection(CrossSection,CRSAxialFrictionModel):
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
    alpha : float
         Thermal expansion coefficient(default 0.0)
    massCenterY : float
         Mass center Y-coordinate in beam element system(default 0.0)
    massCenterZ : float
         Mass center Z-coordinate in beam element system(default 0.0)
    buoyancyCenterY : float
         Buoyancy center Y-coordinate in beam element system(default 0.0)
    buoyancyCenterZ : float
         Buoyancy center Z-coordinate in beam element system(default 0.0)
    areaCenterY : float
         Area center Y-coordinate in beam element system(default 0.0)
    areaCenterZ : float
         Area center Z-coordinate in beam element system(default 0.0)
    principalAxesOrientation : float
         Orientation (theta) of principal axes V and W(default 0.0)
    shearCenterY : float
         Shear center Y-coordinate in beam element system(default 0.0)
    shearCenterZ : float
         Shear center Z-coordinate in beam element system(default 0.0)
    massCoefficient : float
         Mass / unit length(default 0.0)
    extCrossSectionalArea : float
         External cross-sectional area(default 0.0)
    intCrossSectionalArea : float
         Internal cross-sectional area(default 0.0)
    gyrationRadius : float
         Radius of gyration about local x-axis(default 0.0)
    torsionStiffness : float
         Torsion stiffness(default 0.0)
    bendingStiffnessV : float
         Bending stiffness around principal V-axis(default 0.0)
    bendingStiffnessW : float
         Bending stiffness around principal W-axis(default 0.0)
    shearStiffnessW : float
         Shear stiffness in principal W-direction. Infinite shear stiffness if equal to zero(default 0.0)
    shearStiffnessV : float
         Shear stiffness in principal V-direction. Infinite shear stiffness if equal to zero(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", staticFriction:float=0.0, staticElongation:float=0.0, dynamicFriction:float=0.0, dynamicElongation:float=0.0, axialFriction:bool=False, scfkSpecification:bool=True, loadFormulation:LoadFormulation=LoadFormulation.MORISON, hydrodynamicDiameter:float=0.0, addedMassTanDir:float=0.0, addedMassNormDir:float=0.0, dampingNormDir:float=0.0, cdx:float=0.0, cdy:float=0.0, cdz:float=0.0, amx:float=0.0, amy:float=0.0, amz:float=0.0, addedMass:float=0.0, cdlx:float=0.0, cdly:float=0.0, cdlz:float=0.0, scfk:float=1.0, scfkt:TangentialFroudeKrylovScaling=TangentialFroudeKrylovScaling.ON, hydrodynamicInputCode:HydrodynamicInputCode=HydrodynamicInputCode.DIMENSIONAL, cdt:float=0.0, cdn:float=0.0, cdnz:float=0.0, massDampingSpecification:bool=False, stiffnessDampingSpecification:bool=False, axialDampingSpecification:bool=False, cdax:float=0.0, cday:float=0.0, cdaz:float=0.0, aerodynamicInputCode:AerodynamicInputCode=AerodynamicInputCode.NONE, aerodynamicDiameter:float=0.0, temperature:float=0.0, pressureDependency:int=0, axialStiffness:float=0.0, tensionCapacity:float=0.0, maxCurvatureY:float=0.0, maxCurvatureZ:float=0.0, chordLength:float=0.0, foilOriginY:float=0.0, foilOriginZ:float=0.0, foilInclination:float=0.0, aerodynamicForceType:AerodynamicForceType=AerodynamicForceType.NONE, coupledBendingTorsion:bool=False, alpha:float=0.0, massCenterY:float=0.0, massCenterZ:float=0.0, buoyancyCenterY:float=0.0, buoyancyCenterZ:float=0.0, areaCenterY:float=0.0, areaCenterZ:float=0.0, principalAxesOrientation:float=0.0, shearCenterY:float=0.0, shearCenterZ:float=0.0, massCoefficient:float=0.0, extCrossSectionalArea:float=0.0, intCrossSectionalArea:float=0.0, gyrationRadius:float=0.0, torsionStiffness:float=0.0, bendingStiffnessV:float=0.0, bendingStiffnessW:float=0.0, shearStiffnessW:float=0.0, shearStiffnessV:float=0.0, **kwargs):
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
        self.__alpha = alpha
        self.__massCenterY = massCenterY
        self.__massCenterZ = massCenterZ
        self.__buoyancyCenterY = buoyancyCenterY
        self.__buoyancyCenterZ = buoyancyCenterZ
        self.__areaCenterY = areaCenterY
        self.__areaCenterZ = areaCenterZ
        self.__principalAxesOrientation = principalAxesOrientation
        self.__shearCenterY = shearCenterY
        self.__shearCenterZ = shearCenterZ
        self.__massCoefficient = massCoefficient
        self.__extCrossSectionalArea = extCrossSectionalArea
        self.__intCrossSectionalArea = intCrossSectionalArea
        self.__gyrationRadius = gyrationRadius
        self.__torsionStiffness = torsionStiffness
        self.__bendingStiffnessV = bendingStiffnessV
        self.__bendingStiffnessW = bendingStiffnessW
        self.__shearStiffnessW = shearStiffnessW
        self.__shearStiffnessV = shearStiffnessV
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeneralCrossSectionBlueprint()


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
    def alpha(self) -> float:
        """Thermal expansion coefficient"""
        return self.__alpha

    @alpha.setter
    def alpha(self, value: float):
        """Set alpha"""
        self.__alpha = float(value)

    @property
    def massCenterY(self) -> float:
        """Mass center Y-coordinate in beam element system"""
        return self.__massCenterY

    @massCenterY.setter
    def massCenterY(self, value: float):
        """Set massCenterY"""
        self.__massCenterY = float(value)

    @property
    def massCenterZ(self) -> float:
        """Mass center Z-coordinate in beam element system"""
        return self.__massCenterZ

    @massCenterZ.setter
    def massCenterZ(self, value: float):
        """Set massCenterZ"""
        self.__massCenterZ = float(value)

    @property
    def buoyancyCenterY(self) -> float:
        """Buoyancy center Y-coordinate in beam element system"""
        return self.__buoyancyCenterY

    @buoyancyCenterY.setter
    def buoyancyCenterY(self, value: float):
        """Set buoyancyCenterY"""
        self.__buoyancyCenterY = float(value)

    @property
    def buoyancyCenterZ(self) -> float:
        """Buoyancy center Z-coordinate in beam element system"""
        return self.__buoyancyCenterZ

    @buoyancyCenterZ.setter
    def buoyancyCenterZ(self, value: float):
        """Set buoyancyCenterZ"""
        self.__buoyancyCenterZ = float(value)

    @property
    def areaCenterY(self) -> float:
        """Area center Y-coordinate in beam element system"""
        return self.__areaCenterY

    @areaCenterY.setter
    def areaCenterY(self, value: float):
        """Set areaCenterY"""
        self.__areaCenterY = float(value)

    @property
    def areaCenterZ(self) -> float:
        """Area center Z-coordinate in beam element system"""
        return self.__areaCenterZ

    @areaCenterZ.setter
    def areaCenterZ(self, value: float):
        """Set areaCenterZ"""
        self.__areaCenterZ = float(value)

    @property
    def principalAxesOrientation(self) -> float:
        """Orientation (theta) of principal axes V and W"""
        return self.__principalAxesOrientation

    @principalAxesOrientation.setter
    def principalAxesOrientation(self, value: float):
        """Set principalAxesOrientation"""
        self.__principalAxesOrientation = float(value)

    @property
    def shearCenterY(self) -> float:
        """Shear center Y-coordinate in beam element system"""
        return self.__shearCenterY

    @shearCenterY.setter
    def shearCenterY(self, value: float):
        """Set shearCenterY"""
        self.__shearCenterY = float(value)

    @property
    def shearCenterZ(self) -> float:
        """Shear center Z-coordinate in beam element system"""
        return self.__shearCenterZ

    @shearCenterZ.setter
    def shearCenterZ(self, value: float):
        """Set shearCenterZ"""
        self.__shearCenterZ = float(value)

    @property
    def massCoefficient(self) -> float:
        """Mass / unit length"""
        return self.__massCoefficient

    @massCoefficient.setter
    def massCoefficient(self, value: float):
        """Set massCoefficient"""
        self.__massCoefficient = float(value)

    @property
    def extCrossSectionalArea(self) -> float:
        """External cross-sectional area"""
        return self.__extCrossSectionalArea

    @extCrossSectionalArea.setter
    def extCrossSectionalArea(self, value: float):
        """Set extCrossSectionalArea"""
        self.__extCrossSectionalArea = float(value)

    @property
    def intCrossSectionalArea(self) -> float:
        """Internal cross-sectional area"""
        return self.__intCrossSectionalArea

    @intCrossSectionalArea.setter
    def intCrossSectionalArea(self, value: float):
        """Set intCrossSectionalArea"""
        self.__intCrossSectionalArea = float(value)

    @property
    def gyrationRadius(self) -> float:
        """Radius of gyration about local x-axis"""
        return self.__gyrationRadius

    @gyrationRadius.setter
    def gyrationRadius(self, value: float):
        """Set gyrationRadius"""
        self.__gyrationRadius = float(value)

    @property
    def torsionStiffness(self) -> float:
        """Torsion stiffness"""
        return self.__torsionStiffness

    @torsionStiffness.setter
    def torsionStiffness(self, value: float):
        """Set torsionStiffness"""
        self.__torsionStiffness = float(value)

    @property
    def bendingStiffnessV(self) -> float:
        """Bending stiffness around principal V-axis"""
        return self.__bendingStiffnessV

    @bendingStiffnessV.setter
    def bendingStiffnessV(self, value: float):
        """Set bendingStiffnessV"""
        self.__bendingStiffnessV = float(value)

    @property
    def bendingStiffnessW(self) -> float:
        """Bending stiffness around principal W-axis"""
        return self.__bendingStiffnessW

    @bendingStiffnessW.setter
    def bendingStiffnessW(self, value: float):
        """Set bendingStiffnessW"""
        self.__bendingStiffnessW = float(value)

    @property
    def shearStiffnessW(self) -> float:
        """Shear stiffness in principal W-direction. Infinite shear stiffness if equal to zero"""
        return self.__shearStiffnessW

    @shearStiffnessW.setter
    def shearStiffnessW(self, value: float):
        """Set shearStiffnessW"""
        self.__shearStiffnessW = float(value)

    @property
    def shearStiffnessV(self) -> float:
        """Shear stiffness in principal V-direction. Infinite shear stiffness if equal to zero"""
        return self.__shearStiffnessV

    @shearStiffnessV.setter
    def shearStiffnessV(self, value: float):
        """Set shearStiffnessV"""
        self.__shearStiffnessV = float(value)
