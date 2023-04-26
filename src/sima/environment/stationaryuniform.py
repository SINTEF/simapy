# This an autogenerated file
# 
# Generated with StationaryUniform
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stationaryuniform import StationaryUniformBlueprint
from typing import Dict
from .shearprofile import ShearProfile
from .shearwindvelocityprofile import ShearWindVelocityProfile
from .wind import Wind
from sima.sima import ScriptableValue

class StationaryUniform(Wind):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Wind propagation direction(default 0.0)
    horizontalVelocity : float
         Horizontal wind velocity component(default 0.0)
    verticalVelocity : float
         Vertical wind velocity component(default 0.0)
    velocityProfiles : List[ShearWindVelocityProfile]
    lowerEdgeZ : float
         Z coordinate of the lower edge of the wind field domain(default 0.0)
    domainResolution : float
         Domain resolution in Z- (vertical) direction(default 0.0)
    numGridPoints : int
         Number of grid points in Z- (vertical) direction(default 0)
    shearProfile : ShearProfile
    referenceHeight : float
         Reference height for which the horizontal and vertical wind velocity values are given.(default 0.0)
    windShearExponent : float
         Exponent in the power shear profile(default 0.0)
    roughnessLength : float
         (default 0.0)
    """

    def __init__(self , description="", direction=0.0, horizontalVelocity=0.0, verticalVelocity=0.0, lowerEdgeZ=0.0, domainResolution=0.0, numGridPoints=0, shearProfile=ShearProfile.NONE, referenceHeight=0.0, windShearExponent=0.0, roughnessLength=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.direction = direction
        self.horizontalVelocity = horizontalVelocity
        self.verticalVelocity = verticalVelocity
        self.velocityProfiles = list()
        self.lowerEdgeZ = lowerEdgeZ
        self.domainResolution = domainResolution
        self.numGridPoints = numGridPoints
        self.shearProfile = shearProfile
        self.referenceHeight = referenceHeight
        self.windShearExponent = windShearExponent
        self.roughnessLength = roughnessLength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StationaryUniformBlueprint()


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
    def direction(self) -> float:
        """Wind propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def horizontalVelocity(self) -> float:
        """Horizontal wind velocity component"""
        return self.__horizontalVelocity

    @horizontalVelocity.setter
    def horizontalVelocity(self, value: float):
        """Set horizontalVelocity"""
        self.__horizontalVelocity = float(value)

    @property
    def verticalVelocity(self) -> float:
        """Vertical wind velocity component"""
        return self.__verticalVelocity

    @verticalVelocity.setter
    def verticalVelocity(self, value: float):
        """Set verticalVelocity"""
        self.__verticalVelocity = float(value)

    @property
    def velocityProfiles(self) -> List[ShearWindVelocityProfile]:
        """"""
        return self.__velocityProfiles

    @velocityProfiles.setter
    def velocityProfiles(self, value: List[ShearWindVelocityProfile]):
        """Set velocityProfiles"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__velocityProfiles = value

    @property
    def lowerEdgeZ(self) -> float:
        """Z coordinate of the lower edge of the wind field domain"""
        return self.__lowerEdgeZ

    @lowerEdgeZ.setter
    def lowerEdgeZ(self, value: float):
        """Set lowerEdgeZ"""
        self.__lowerEdgeZ = float(value)

    @property
    def domainResolution(self) -> float:
        """Domain resolution in Z- (vertical) direction"""
        return self.__domainResolution

    @domainResolution.setter
    def domainResolution(self, value: float):
        """Set domainResolution"""
        self.__domainResolution = float(value)

    @property
    def numGridPoints(self) -> int:
        """Number of grid points in Z- (vertical) direction"""
        return self.__numGridPoints

    @numGridPoints.setter
    def numGridPoints(self, value: int):
        """Set numGridPoints"""
        self.__numGridPoints = int(value)

    @property
    def shearProfile(self) -> ShearProfile:
        """"""
        return self.__shearProfile

    @shearProfile.setter
    def shearProfile(self, value: ShearProfile):
        """Set shearProfile"""
        self.__shearProfile = value

    @property
    def referenceHeight(self) -> float:
        """Reference height for which the horizontal and vertical wind velocity values are given."""
        return self.__referenceHeight

    @referenceHeight.setter
    def referenceHeight(self, value: float):
        """Set referenceHeight"""
        self.__referenceHeight = float(value)

    @property
    def windShearExponent(self) -> float:
        """Exponent in the power shear profile"""
        return self.__windShearExponent

    @windShearExponent.setter
    def windShearExponent(self, value: float):
        """Set windShearExponent"""
        self.__windShearExponent = float(value)

    @property
    def roughnessLength(self) -> float:
        """"""
        return self.__roughnessLength

    @roughnessLength.setter
    def roughnessLength(self, value: float):
        """Set roughnessLength"""
        self.__roughnessLength = float(value)