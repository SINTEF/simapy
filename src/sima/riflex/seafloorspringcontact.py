# This an autogenerated file
# 
# Generated with SeafloorSpringContact
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.seafloorspringcontact import SeafloorSpringContactBlueprint
from typing import Dict
from sima.riflex.seafloorcontact import SeafloorContact
from sima.sima.scriptablevalue import ScriptableValue

class SeafloorSpringContact(SeafloorContact):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
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
    normalStiffness : float
         Normal stiffness parameter for seafloor(default 0.0)
    normalDamping : float
         Normal seafloor damping(default 0.0)
    applyLateralContactForces : bool
         Apply lateral contact forces at the external contact radius, giving a torsional moment(default False)
    """

    def __init__(self , _id="", name="", axialStiffness=0.0, axialFriction=0.0, axialDamping=0.0, lateralStiffness=0.0, lateralFriction=0.0, lateralDamping=0.0, normalStiffness=0.0, normalDamping=0.0, applyLateralContactForces=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.axialStiffness = axialStiffness
        self.axialFriction = axialFriction
        self.axialDamping = axialDamping
        self.lateralStiffness = lateralStiffness
        self.lateralFriction = lateralFriction
        self.lateralDamping = lateralDamping
        self.normalStiffness = normalStiffness
        self.normalDamping = normalDamping
        self.applyLateralContactForces = applyLateralContactForces
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SeafloorSpringContactBlueprint()


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
    def normalStiffness(self) -> float:
        """Normal stiffness parameter for seafloor"""
        return self.__normalStiffness

    @normalStiffness.setter
    def normalStiffness(self, value: float):
        """Set normalStiffness"""
        self.__normalStiffness = float(value)

    @property
    def normalDamping(self) -> float:
        """Normal seafloor damping"""
        return self.__normalDamping

    @normalDamping.setter
    def normalDamping(self, value: float):
        """Set normalDamping"""
        self.__normalDamping = float(value)

    @property
    def applyLateralContactForces(self) -> bool:
        """Apply lateral contact forces at the external contact radius, giving a torsional moment"""
        return self.__applyLateralContactForces

    @applyLateralContactForces.setter
    def applyLateralContactForces(self, value: bool):
        """Set applyLateralContactForces"""
        self.__applyLateralContactForces = bool(value)
