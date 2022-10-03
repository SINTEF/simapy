# This an autogenerated file
# 
# Generated with ProplibTunnelThruster
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.proplibtunnelthruster import ProplibTunnelThrusterBlueprint
from typing import Dict
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.ithruster import IThruster
from sima.simo.thrustercontrolsequence import ThrusterControlSequence
from sima.simo.thrusterdynamics import ThrusterDynamics
from sima.simo.thrusterfailurespecification import ThrusterFailureSpecification

class ProplibTunnelThruster(IThruster):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    minForce : float
         Minimum thruster force(default 0.0)
    maxForce : float
         Maximum thruster force(default 0.0)
    position : Point3
    force : float
         Resulting force, initial value if controlled by a DP-system(default 0.0)
    forceDirection : float
         Direction of thrust force in body x-y plane, initial value if controlled by a DP-system(default 0.0)
    thrusterDynamics : ThrusterDynamics
    controlSequence : ThrusterControlSequence
    failureSpecification : ThrusterFailureSpecification
    includeSurfaceProximityLoss : bool
         Should surface proximity loss be included?(default True)
    includeThrusterHullInteraction : bool
         Should thruster-hull interaction be included?(default True)
    includeThrusterThrusterInteraction : bool
         Should thruster-thruster interaction be included?(default True)
    maxRps : float
         The RPS giving maximum force(default 0.0)
    diameter : float
         Thruster diameter(default 0.0)
    tunnelLength : float
         Tunnel length(default 0.0)
    baselineAngle : float
         Hull angle relative to baseline (front view)(default 0.0)
    centerlineAngle : float
         Hull angle relative to centerline (top view)(default 0.0)
    numberOfGrids : int
         Number of grids(default 0)
    pitchRatio : float
         Propeller Pitch Ratio(default 0.0)
    bilgeRadius : float
         Bilge radius(default 0.0)
    verticalDistanceHull : float
         Vertical distance from propeller center to hull(default 0.0)
    """

    def __init__(self , _id="", name="", minForce=0.0, maxForce=0.0, force=0.0, forceDirection=0.0, includeSurfaceProximityLoss=True, includeThrusterHullInteraction=True, includeThrusterThrusterInteraction=True, maxRps=0.0, diameter=0.0, tunnelLength=0.0, baselineAngle=0.0, centerlineAngle=0.0, numberOfGrids=0, pitchRatio=0.0, bilgeRadius=0.0, verticalDistanceHull=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.minForce = minForce
        self.maxForce = maxForce
        self.position = None
        self.force = force
        self.forceDirection = forceDirection
        self.thrusterDynamics = None
        self.controlSequence = None
        self.failureSpecification = None
        self.includeSurfaceProximityLoss = includeSurfaceProximityLoss
        self.includeThrusterHullInteraction = includeThrusterHullInteraction
        self.includeThrusterThrusterInteraction = includeThrusterThrusterInteraction
        self.maxRps = maxRps
        self.diameter = diameter
        self.tunnelLength = tunnelLength
        self.baselineAngle = baselineAngle
        self.centerlineAngle = centerlineAngle
        self.numberOfGrids = numberOfGrids
        self.pitchRatio = pitchRatio
        self.bilgeRadius = bilgeRadius
        self.verticalDistanceHull = verticalDistanceHull
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ProplibTunnelThrusterBlueprint()


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
    def minForce(self) -> float:
        """Minimum thruster force"""
        return self.__minForce

    @minForce.setter
    def minForce(self, value: float):
        """Set minForce"""
        self.__minForce = float(value)

    @property
    def maxForce(self) -> float:
        """Maximum thruster force"""
        return self.__maxForce

    @maxForce.setter
    def maxForce(self, value: float):
        """Set maxForce"""
        self.__maxForce = float(value)

    @property
    def position(self) -> Point3:
        """"""
        return self.__position

    @position.setter
    def position(self, value: Point3):
        """Set position"""
        self.__position = value

    @property
    def force(self) -> float:
        """Resulting force, initial value if controlled by a DP-system"""
        return self.__force

    @force.setter
    def force(self, value: float):
        """Set force"""
        self.__force = float(value)

    @property
    def forceDirection(self) -> float:
        """Direction of thrust force in body x-y plane, initial value if controlled by a DP-system"""
        return self.__forceDirection

    @forceDirection.setter
    def forceDirection(self, value: float):
        """Set forceDirection"""
        self.__forceDirection = float(value)

    @property
    def thrusterDynamics(self) -> ThrusterDynamics:
        """"""
        return self.__thrusterDynamics

    @thrusterDynamics.setter
    def thrusterDynamics(self, value: ThrusterDynamics):
        """Set thrusterDynamics"""
        self.__thrusterDynamics = value

    @property
    def controlSequence(self) -> ThrusterControlSequence:
        """"""
        return self.__controlSequence

    @controlSequence.setter
    def controlSequence(self, value: ThrusterControlSequence):
        """Set controlSequence"""
        self.__controlSequence = value

    @property
    def failureSpecification(self) -> ThrusterFailureSpecification:
        """"""
        return self.__failureSpecification

    @failureSpecification.setter
    def failureSpecification(self, value: ThrusterFailureSpecification):
        """Set failureSpecification"""
        self.__failureSpecification = value

    @property
    def includeSurfaceProximityLoss(self) -> bool:
        """Should surface proximity loss be included?"""
        return self.__includeSurfaceProximityLoss

    @includeSurfaceProximityLoss.setter
    def includeSurfaceProximityLoss(self, value: bool):
        """Set includeSurfaceProximityLoss"""
        self.__includeSurfaceProximityLoss = bool(value)

    @property
    def includeThrusterHullInteraction(self) -> bool:
        """Should thruster-hull interaction be included?"""
        return self.__includeThrusterHullInteraction

    @includeThrusterHullInteraction.setter
    def includeThrusterHullInteraction(self, value: bool):
        """Set includeThrusterHullInteraction"""
        self.__includeThrusterHullInteraction = bool(value)

    @property
    def includeThrusterThrusterInteraction(self) -> bool:
        """Should thruster-thruster interaction be included?"""
        return self.__includeThrusterThrusterInteraction

    @includeThrusterThrusterInteraction.setter
    def includeThrusterThrusterInteraction(self, value: bool):
        """Set includeThrusterThrusterInteraction"""
        self.__includeThrusterThrusterInteraction = bool(value)

    @property
    def maxRps(self) -> float:
        """The RPS giving maximum force"""
        return self.__maxRps

    @maxRps.setter
    def maxRps(self, value: float):
        """Set maxRps"""
        self.__maxRps = float(value)

    @property
    def diameter(self) -> float:
        """Thruster diameter"""
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float):
        """Set diameter"""
        self.__diameter = float(value)

    @property
    def tunnelLength(self) -> float:
        """Tunnel length"""
        return self.__tunnelLength

    @tunnelLength.setter
    def tunnelLength(self, value: float):
        """Set tunnelLength"""
        self.__tunnelLength = float(value)

    @property
    def baselineAngle(self) -> float:
        """Hull angle relative to baseline (front view)"""
        return self.__baselineAngle

    @baselineAngle.setter
    def baselineAngle(self, value: float):
        """Set baselineAngle"""
        self.__baselineAngle = float(value)

    @property
    def centerlineAngle(self) -> float:
        """Hull angle relative to centerline (top view)"""
        return self.__centerlineAngle

    @centerlineAngle.setter
    def centerlineAngle(self, value: float):
        """Set centerlineAngle"""
        self.__centerlineAngle = float(value)

    @property
    def numberOfGrids(self) -> int:
        """Number of grids"""
        return self.__numberOfGrids

    @numberOfGrids.setter
    def numberOfGrids(self, value: int):
        """Set numberOfGrids"""
        self.__numberOfGrids = int(value)

    @property
    def pitchRatio(self) -> float:
        """Propeller Pitch Ratio"""
        return self.__pitchRatio

    @pitchRatio.setter
    def pitchRatio(self, value: float):
        """Set pitchRatio"""
        self.__pitchRatio = float(value)

    @property
    def bilgeRadius(self) -> float:
        """Bilge radius"""
        return self.__bilgeRadius

    @bilgeRadius.setter
    def bilgeRadius(self, value: float):
        """Set bilgeRadius"""
        self.__bilgeRadius = float(value)

    @property
    def verticalDistanceHull(self) -> float:
        """Vertical distance from propeller center to hull"""
        return self.__verticalDistanceHull

    @verticalDistanceHull.setter
    def verticalDistanceHull(self, value: float):
        """Set verticalDistanceHull"""
        self.__verticalDistanceHull = float(value)
