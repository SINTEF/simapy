# This an autogenerated file
# 
# Generated with FluctuatingThreeComponent
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fluctuatingthreecomponent import FluctuatingThreeComponentBlueprint
from typing import Dict
from sima.environment.fluctuatingwindvelocityprofile import FluctuatingWindVelocityProfile
from sima.environment.wind import Wind
from sima.sima.scriptablevalue import ScriptableValue

class FluctuatingThreeComponent(Wind):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Wind propagation direction(default 0.0)
    meanSpeed : float
         Mean wind speed (along wind propagation direction)(default 0.0)
    velocityProfiles : List[FluctuatingWindVelocityProfile]
    longitudinalFileName : str
         Path and filename for the fluctuating longitudinal wind time series(default None)
    lateralFileName : str
         Path and filename for the fluctuating lateral wind time series(default None)
    verticalFileName : str
         Path and filename for the fluctuating vertical wind time series(default None)
    lowerLeftX : float
         X-coordinate of the lower left corner of the upstream border of the wind(default 0.0)
    lowerLeftY : float
         Y-coordinate of the lower left corner of the wind field domain(default 0.0)
    lowerLeftZ : float
         Z-coordinate of the lower left corner of the wind field domain(default 0.0)
    numPointsX : int
         Number of grid points in X- (longitudinal) direction(default 0)
    numPointsY : int
         Number of grid points in Y- (lateral) direction(default 0)
    numPointsZ : int
         Number of grid points in Z- (vertical) direction(default 0)
    sizeX : float
         Field size in X- (longitudinal) direction(default 0.0)
    sizeY : float
         Field size in Y- (lateral) direction(default 0.0)
    sizeZ : float
         Field size in Z- (vertical) direction(default 0.0)
    numSlices : int
         Buffer size: Number of wind crossectional planes (Slices) in memory(default 800)
    """

    def __init__(self , description="", direction=0.0, meanSpeed=0.0, lowerLeftX=0.0, lowerLeftY=0.0, lowerLeftZ=0.0, numPointsX=0, numPointsY=0, numPointsZ=0, sizeX=0.0, sizeY=0.0, sizeZ=0.0, numSlices=800, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.direction = direction
        self.meanSpeed = meanSpeed
        self.velocityProfiles = list()
        self.longitudinalFileName = None
        self.lateralFileName = None
        self.verticalFileName = None
        self.lowerLeftX = lowerLeftX
        self.lowerLeftY = lowerLeftY
        self.lowerLeftZ = lowerLeftZ
        self.numPointsX = numPointsX
        self.numPointsY = numPointsY
        self.numPointsZ = numPointsZ
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.sizeZ = sizeZ
        self.numSlices = numSlices
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FluctuatingThreeComponentBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def meanSpeed(self) -> float:
        """Mean wind speed (along wind propagation direction)"""
        return self.__meanSpeed

    @meanSpeed.setter
    def meanSpeed(self, value: float):
        """Set meanSpeed"""
        self.__meanSpeed = float(value)

    @property
    def velocityProfiles(self) -> List[FluctuatingWindVelocityProfile]:
        """"""
        return self.__velocityProfiles

    @velocityProfiles.setter
    def velocityProfiles(self, value: List[FluctuatingWindVelocityProfile]):
        """Set velocityProfiles"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__velocityProfiles = value

    @property
    def longitudinalFileName(self) -> str:
        """Path and filename for the fluctuating longitudinal wind time series"""
        return self.__longitudinalFileName

    @longitudinalFileName.setter
    def longitudinalFileName(self, value: str):
        """Set longitudinalFileName"""
        self.__longitudinalFileName = value

    @property
    def lateralFileName(self) -> str:
        """Path and filename for the fluctuating lateral wind time series"""
        return self.__lateralFileName

    @lateralFileName.setter
    def lateralFileName(self, value: str):
        """Set lateralFileName"""
        self.__lateralFileName = value

    @property
    def verticalFileName(self) -> str:
        """Path and filename for the fluctuating vertical wind time series"""
        return self.__verticalFileName

    @verticalFileName.setter
    def verticalFileName(self, value: str):
        """Set verticalFileName"""
        self.__verticalFileName = value

    @property
    def lowerLeftX(self) -> float:
        """X-coordinate of the lower left corner of the upstream border of the wind"""
        return self.__lowerLeftX

    @lowerLeftX.setter
    def lowerLeftX(self, value: float):
        """Set lowerLeftX"""
        self.__lowerLeftX = float(value)

    @property
    def lowerLeftY(self) -> float:
        """Y-coordinate of the lower left corner of the wind field domain"""
        return self.__lowerLeftY

    @lowerLeftY.setter
    def lowerLeftY(self, value: float):
        """Set lowerLeftY"""
        self.__lowerLeftY = float(value)

    @property
    def lowerLeftZ(self) -> float:
        """Z-coordinate of the lower left corner of the wind field domain"""
        return self.__lowerLeftZ

    @lowerLeftZ.setter
    def lowerLeftZ(self, value: float):
        """Set lowerLeftZ"""
        self.__lowerLeftZ = float(value)

    @property
    def numPointsX(self) -> int:
        """Number of grid points in X- (longitudinal) direction"""
        return self.__numPointsX

    @numPointsX.setter
    def numPointsX(self, value: int):
        """Set numPointsX"""
        self.__numPointsX = int(value)

    @property
    def numPointsY(self) -> int:
        """Number of grid points in Y- (lateral) direction"""
        return self.__numPointsY

    @numPointsY.setter
    def numPointsY(self, value: int):
        """Set numPointsY"""
        self.__numPointsY = int(value)

    @property
    def numPointsZ(self) -> int:
        """Number of grid points in Z- (vertical) direction"""
        return self.__numPointsZ

    @numPointsZ.setter
    def numPointsZ(self, value: int):
        """Set numPointsZ"""
        self.__numPointsZ = int(value)

    @property
    def sizeX(self) -> float:
        """Field size in X- (longitudinal) direction"""
        return self.__sizeX

    @sizeX.setter
    def sizeX(self, value: float):
        """Set sizeX"""
        self.__sizeX = float(value)

    @property
    def sizeY(self) -> float:
        """Field size in Y- (lateral) direction"""
        return self.__sizeY

    @sizeY.setter
    def sizeY(self, value: float):
        """Set sizeY"""
        self.__sizeY = float(value)

    @property
    def sizeZ(self) -> float:
        """Field size in Z- (vertical) direction"""
        return self.__sizeZ

    @sizeZ.setter
    def sizeZ(self, value: float):
        """Set sizeZ"""
        self.__sizeZ = float(value)

    @property
    def numSlices(self) -> int:
        """Buffer size: Number of wind crossectional planes (Slices) in memory"""
        return self.__numSlices

    @numSlices.setter
    def numSlices(self, value: int):
        """Set numSlices"""
        self.__numSlices = int(value)
