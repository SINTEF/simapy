# This an autogenerated file
# 
# Generated with VolumeConeItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.volumeconeitem import VolumeConeItemBlueprint
from typing import Dict
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.axis import Axis
from sima.simo.volume import Volume
from sima.simo.volumemassportion import VolumeMassPortion

class VolumeConeItem(VolumeMassPortion):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    volume : Volume
         Add or subtract volume
    centerPoint : Point3
         Location of center of bottom plane in local coordinates
    length : float
         Length of cone(default 0.0)
    diameterBottomPlane : float
         Diameter of plane 1 (bottom plane)(default 0.0)
    diameterTopPlane : float
         Diameter of plane 2(default 0.0)
    axis : Axis
         Cone axis direction:\nX: parallell to Tank x-axis\nY: parallell to Tank y-axis\nZ: parallell to Tank z-axis
    """

    def __init__(self , _id="", volume=Volume.ADD, length=0.0, diameterBottomPlane=0.0, diameterTopPlane=0.0, axis=Axis.Z, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.volume = volume
        self.centerPoint = None
        self.length = length
        self.diameterBottomPlane = diameterBottomPlane
        self.diameterTopPlane = diameterTopPlane
        self.axis = axis
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VolumeConeItemBlueprint()


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
    def volume(self) -> Volume:
        """Add or subtract volume"""
        return self.__volume

    @volume.setter
    def volume(self, value: Volume):
        """Set volume"""
        self.__volume = value

    @property
    def centerPoint(self) -> Point3:
        """Location of center of bottom plane in local coordinates"""
        return self.__centerPoint

    @centerPoint.setter
    def centerPoint(self, value: Point3):
        """Set centerPoint"""
        self.__centerPoint = value

    @property
    def length(self) -> float:
        """Length of cone"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def diameterBottomPlane(self) -> float:
        """Diameter of plane 1 (bottom plane)"""
        return self.__diameterBottomPlane

    @diameterBottomPlane.setter
    def diameterBottomPlane(self, value: float):
        """Set diameterBottomPlane"""
        self.__diameterBottomPlane = float(value)

    @property
    def diameterTopPlane(self) -> float:
        """Diameter of plane 2"""
        return self.__diameterTopPlane

    @diameterTopPlane.setter
    def diameterTopPlane(self, value: float):
        """Set diameterTopPlane"""
        self.__diameterTopPlane = float(value)

    @property
    def axis(self) -> Axis:
        """Cone axis direction:
X: parallell to Tank x-axis
Y: parallell to Tank y-axis
Z: parallell to Tank z-axis"""
        return self.__axis

    @axis.setter
    def axis(self, value: Axis):
        """Set axis"""
        self.__axis = value
