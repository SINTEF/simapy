# This an autogenerated file
# 
# Generated with FishNet
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fishnet import FishNetBlueprint
from typing import Dict
from sima.riflex.axialstiffness import AxialStiffness
from sima.riflex.axialstiffnessitem import AxialStiffnessItem
from sima.riflex.crosssection import CrossSection
from sima.riflex.crsaxialdamping import CRSAxialDamping
from sima.riflex.crsaxialfrictionmodel import CRSAxialFrictionModel
from sima.riflex.crsmassdamping import CRSMassDamping
from sima.riflex.crsstiffnessdamping import CRSStiffnessDamping
from sima.sima.scriptablevalue import ScriptableValue

class FishNet(CrossSection,CRSAxialFrictionModel):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
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
    massDampingSpecification : bool
         Mass proportional Rayleigh damping(default False)
    stiffnessDampingSpecification : bool
         Stiffness proportional Rayleigh damping(default False)
    axialDampingSpecification : bool
         Local axial damping model(default False)
    temperature : float
         Temperature at which the specification applies(default 0.0)
    mass : float
         Mass / unit length(default 0.0)
    externalVolume : float
         External volume per length(default 0.0)
    axialStiffnessInput : AxialStiffness
         Axial stiffness input specification
    axialStiffness : float
         Axial stiffness(default 0.0)
    axialStiffnessCharacteristics : List[AxialStiffnessItem]
    solidityRatio : float
         Solidity ratio.(default 0.0)
    netWidthEnd1 : float
         Net width at segment end 1(default 0.0)
    netWidthEnd2 : float
         Net width at segment end 2(default 0.0)
    currentVelocityReduction : float
         Reduction factor for current velocity.(default 1.0)
    massDamping : CRSMassDamping
    stiffnessDamping : CRSStiffnessDamping
    axialDamping : CRSAxialDamping
    amx : float
         Added mass per length, tangential direction(default 0.0)
    amy : float
         Added mass per length, normal direction(default 0.0)
    tensionCapacity : float
         Tension capacity(default 0.0)
    maxCurvature : float
         Maximum curvature(default 0.0)
    """

    def __init__(self , description="", _id=None, name=None, staticFriction=0.0, staticElongation=0.0, dynamicFriction=0.0, dynamicElongation=0.0, axialFriction=False, massDampingSpecification=False, stiffnessDampingSpecification=False, axialDampingSpecification=False, temperature=0.0, mass=0.0, externalVolume=0.0, axialStiffnessInput=AxialStiffness.CONSTANT, axialStiffness=0.0, solidityRatio=0.0, netWidthEnd1=0.0, netWidthEnd2=0.0, currentVelocityReduction=1.0, amx=0.0, amy=0.0, tensionCapacity=0.0, maxCurvature=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.staticFriction = staticFriction
        self.staticElongation = staticElongation
        self.dynamicFriction = dynamicFriction
        self.dynamicElongation = dynamicElongation
        self.axialFriction = axialFriction
        self.massDampingSpecification = massDampingSpecification
        self.stiffnessDampingSpecification = stiffnessDampingSpecification
        self.axialDampingSpecification = axialDampingSpecification
        self.temperature = temperature
        self.mass = mass
        self.externalVolume = externalVolume
        self.axialStiffnessInput = axialStiffnessInput
        self.axialStiffness = axialStiffness
        self.axialStiffnessCharacteristics = list()
        self.solidityRatio = solidityRatio
        self.netWidthEnd1 = netWidthEnd1
        self.netWidthEnd2 = netWidthEnd2
        self.currentVelocityReduction = currentVelocityReduction
        self.massDamping = None
        self.stiffnessDamping = None
        self.axialDamping = None
        self.amx = amx
        self.amy = amy
        self.tensionCapacity = tensionCapacity
        self.maxCurvature = maxCurvature
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FishNetBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def temperature(self) -> float:
        """Temperature at which the specification applies"""
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        """Set temperature"""
        self.__temperature = float(value)

    @property
    def mass(self) -> float:
        """Mass / unit length"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def externalVolume(self) -> float:
        """External volume per length"""
        return self.__externalVolume

    @externalVolume.setter
    def externalVolume(self, value: float):
        """Set externalVolume"""
        self.__externalVolume = float(value)

    @property
    def axialStiffnessInput(self) -> AxialStiffness:
        """Axial stiffness input specification"""
        return self.__axialStiffnessInput

    @axialStiffnessInput.setter
    def axialStiffnessInput(self, value: AxialStiffness):
        """Set axialStiffnessInput"""
        self.__axialStiffnessInput = value

    @property
    def axialStiffness(self) -> float:
        """Axial stiffness"""
        return self.__axialStiffness

    @axialStiffness.setter
    def axialStiffness(self, value: float):
        """Set axialStiffness"""
        self.__axialStiffness = float(value)

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
    def solidityRatio(self) -> float:
        """Solidity ratio."""
        return self.__solidityRatio

    @solidityRatio.setter
    def solidityRatio(self, value: float):
        """Set solidityRatio"""
        self.__solidityRatio = float(value)

    @property
    def netWidthEnd1(self) -> float:
        """Net width at segment end 1"""
        return self.__netWidthEnd1

    @netWidthEnd1.setter
    def netWidthEnd1(self, value: float):
        """Set netWidthEnd1"""
        self.__netWidthEnd1 = float(value)

    @property
    def netWidthEnd2(self) -> float:
        """Net width at segment end 2"""
        return self.__netWidthEnd2

    @netWidthEnd2.setter
    def netWidthEnd2(self, value: float):
        """Set netWidthEnd2"""
        self.__netWidthEnd2 = float(value)

    @property
    def currentVelocityReduction(self) -> float:
        """Reduction factor for current velocity."""
        return self.__currentVelocityReduction

    @currentVelocityReduction.setter
    def currentVelocityReduction(self, value: float):
        """Set currentVelocityReduction"""
        self.__currentVelocityReduction = float(value)

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
    def amx(self) -> float:
        """Added mass per length, tangential direction"""
        return self.__amx

    @amx.setter
    def amx(self, value: float):
        """Set amx"""
        self.__amx = float(value)

    @property
    def amy(self) -> float:
        """Added mass per length, normal direction"""
        return self.__amy

    @amy.setter
    def amy(self, value: float):
        """Set amy"""
        self.__amy = float(value)

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
