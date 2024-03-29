# This an autogenerated file
# 
# Generated with RiserSoilContact
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.risersoilcontact import RiserSoilContactBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .seafloorcontact import SeafloorContact

class RiserSoilContact(SeafloorContact):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    axialStiffness : float
         Horizontal stiffness parameter for seafloor in axial direction(default 0.0)
    axialFriction : float
         Horizontal friction parameter for seafloor in axial direction(default 0.0)
    axialDamping : float
         Axial seafloor damping (default 0.0)
    lateralStiffness : float
         Horizontal stiffness parameter for seafloor in lateral direction(default 0.0)
    lateralFriction : float
         Horizontal stiffness parameter for seafloor in lateral direction(default 0.0)
    lateralDamping : float
         Lateral seafloor damping(default 0.0)
    soilSubmergedWeight : float
         Soil submerged weight(default 0.0)
    soilShearStrength : float
          Soil shear strength at seabed(default 0.0)
    soilShearStrengthGradient : float
         Soil shear strength vertical gradient(default 0.0)
    soilPoissonRatio : float
         Soil Poisson ratio(default 0.0)
    soilGModulus : float
         Soil G-modulus/compressive strength(default 0.0)
    stiffnessModulusRelationship : float
         Relationship between dynamic stiffness and G-modulus(default 0.88)
    alpha : float
         Scaling factor for peak soil suction relative to peak soil compression(default 1.0)
    beta : float
         Scaling factor for peak soil suction relative to peak soil compression(default 1.0)
    kbc : float
         Mobilization displacement for soil bearing capacity as fraction of pipe soil contact width(default 0.05)
    kt : float
         Mobilization displacement for max soil suction as fraction of pipe soil contact width(default 0.08)
    """

    def __init__(self , description="", axialStiffness=0.0, axialFriction=0.0, axialDamping=0.0, lateralStiffness=0.0, lateralFriction=0.0, lateralDamping=0.0, soilSubmergedWeight=0.0, soilShearStrength=0.0, soilShearStrengthGradient=0.0, soilPoissonRatio=0.0, soilGModulus=0.0, stiffnessModulusRelationship=0.88, alpha=1.0, beta=1.0, kbc=0.05, kt=0.08, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.axialStiffness = axialStiffness
        self.axialFriction = axialFriction
        self.axialDamping = axialDamping
        self.lateralStiffness = lateralStiffness
        self.lateralFriction = lateralFriction
        self.lateralDamping = lateralDamping
        self.soilSubmergedWeight = soilSubmergedWeight
        self.soilShearStrength = soilShearStrength
        self.soilShearStrengthGradient = soilShearStrengthGradient
        self.soilPoissonRatio = soilPoissonRatio
        self.soilGModulus = soilGModulus
        self.stiffnessModulusRelationship = stiffnessModulusRelationship
        self.alpha = alpha
        self.beta = beta
        self.kbc = kbc
        self.kt = kt
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RiserSoilContactBlueprint()


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
    def axialStiffness(self) -> float:
        """Horizontal stiffness parameter for seafloor in axial direction"""
        return self.__axialStiffness

    @axialStiffness.setter
    def axialStiffness(self, value: float):
        """Set axialStiffness"""
        self.__axialStiffness = float(value)

    @property
    def axialFriction(self) -> float:
        """Horizontal friction parameter for seafloor in axial direction"""
        return self.__axialFriction

    @axialFriction.setter
    def axialFriction(self, value: float):
        """Set axialFriction"""
        self.__axialFriction = float(value)

    @property
    def axialDamping(self) -> float:
        """Axial seafloor damping """
        return self.__axialDamping

    @axialDamping.setter
    def axialDamping(self, value: float):
        """Set axialDamping"""
        self.__axialDamping = float(value)

    @property
    def lateralStiffness(self) -> float:
        """Horizontal stiffness parameter for seafloor in lateral direction"""
        return self.__lateralStiffness

    @lateralStiffness.setter
    def lateralStiffness(self, value: float):
        """Set lateralStiffness"""
        self.__lateralStiffness = float(value)

    @property
    def lateralFriction(self) -> float:
        """Horizontal stiffness parameter for seafloor in lateral direction"""
        return self.__lateralFriction

    @lateralFriction.setter
    def lateralFriction(self, value: float):
        """Set lateralFriction"""
        self.__lateralFriction = float(value)

    @property
    def lateralDamping(self) -> float:
        """Lateral seafloor damping"""
        return self.__lateralDamping

    @lateralDamping.setter
    def lateralDamping(self, value: float):
        """Set lateralDamping"""
        self.__lateralDamping = float(value)

    @property
    def soilSubmergedWeight(self) -> float:
        """Soil submerged weight"""
        return self.__soilSubmergedWeight

    @soilSubmergedWeight.setter
    def soilSubmergedWeight(self, value: float):
        """Set soilSubmergedWeight"""
        self.__soilSubmergedWeight = float(value)

    @property
    def soilShearStrength(self) -> float:
        """ Soil shear strength at seabed"""
        return self.__soilShearStrength

    @soilShearStrength.setter
    def soilShearStrength(self, value: float):
        """Set soilShearStrength"""
        self.__soilShearStrength = float(value)

    @property
    def soilShearStrengthGradient(self) -> float:
        """Soil shear strength vertical gradient"""
        return self.__soilShearStrengthGradient

    @soilShearStrengthGradient.setter
    def soilShearStrengthGradient(self, value: float):
        """Set soilShearStrengthGradient"""
        self.__soilShearStrengthGradient = float(value)

    @property
    def soilPoissonRatio(self) -> float:
        """Soil Poisson ratio"""
        return self.__soilPoissonRatio

    @soilPoissonRatio.setter
    def soilPoissonRatio(self, value: float):
        """Set soilPoissonRatio"""
        self.__soilPoissonRatio = float(value)

    @property
    def soilGModulus(self) -> float:
        """Soil G-modulus/compressive strength"""
        return self.__soilGModulus

    @soilGModulus.setter
    def soilGModulus(self, value: float):
        """Set soilGModulus"""
        self.__soilGModulus = float(value)

    @property
    def stiffnessModulusRelationship(self) -> float:
        """Relationship between dynamic stiffness and G-modulus"""
        return self.__stiffnessModulusRelationship

    @stiffnessModulusRelationship.setter
    def stiffnessModulusRelationship(self, value: float):
        """Set stiffnessModulusRelationship"""
        self.__stiffnessModulusRelationship = float(value)

    @property
    def alpha(self) -> float:
        """Scaling factor for peak soil suction relative to peak soil compression"""
        return self.__alpha

    @alpha.setter
    def alpha(self, value: float):
        """Set alpha"""
        self.__alpha = float(value)

    @property
    def beta(self) -> float:
        """Scaling factor for peak soil suction relative to peak soil compression"""
        return self.__beta

    @beta.setter
    def beta(self, value: float):
        """Set beta"""
        self.__beta = float(value)

    @property
    def kbc(self) -> float:
        """Mobilization displacement for soil bearing capacity as fraction of pipe soil contact width"""
        return self.__kbc

    @kbc.setter
    def kbc(self, value: float):
        """Set kbc"""
        self.__kbc = float(value)

    @property
    def kt(self) -> float:
        """Mobilization displacement for max soil suction as fraction of pipe soil contact width"""
        return self.__kt

    @kt.setter
    def kt(self, value: float):
        """Set kt"""
        self.__kt = float(value)
