# This an autogenerated file
# 
# Generated with SeaSurface
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.seasurface import SeaSurfaceBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simacolor import SIMAColor

class SeaSurface(MOAO):
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
    centerX : float
         Center of surface in x(default 0.0)
    centerY : float
         Center of surface in y(default 0.0)
    sizeX : float
         Size of surface in x(default 500.0)
    sizeY : float
         Size of surface in y(default 500.0)
    color : SIMAColor
    transparency : float
         Transparency of surface(default 0.0)
    meshGridSize : float
         Size of grids in the mesh(default 100.0)
    showMesh : bool
         Show mesh grid on surface(default True)
    z : float
         Depth of surface(default -100.0)
    lcWaveLength : float
         Length of long-crested wave field(default 300.0)
    lcWaveWidth : float
         Width of long-crested wave field(default 100.0)
    lcWaveNumPoints : int
         Number of points in long-crested wave field(default 61)
    """

    def __init__(self , name:str="", description:str="", _id:str="", centerX:float=0.0, centerY:float=0.0, sizeX:float=500.0, sizeY:float=500.0, transparency:float=0.0, meshGridSize:float=100.0, showMesh:bool=True, z:float=-100.0, lcWaveLength:float=300.0, lcWaveWidth:float=100.0, lcWaveNumPoints:int=61, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__centerX = centerX
        self.__centerY = centerY
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__color = SIMAColor()
        self.__transparency = transparency
        self.__meshGridSize = meshGridSize
        self.__showMesh = showMesh
        self.__z = z
        self.__lcWaveLength = lcWaveLength
        self.__lcWaveWidth = lcWaveWidth
        self.__lcWaveNumPoints = lcWaveNumPoints
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SeaSurfaceBlueprint()


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
    def centerX(self) -> float:
        """Center of surface in x"""
        return self.__centerX

    @centerX.setter
    def centerX(self, value: float):
        """Set centerX"""
        self.__centerX = float(value)

    @property
    def centerY(self) -> float:
        """Center of surface in y"""
        return self.__centerY

    @centerY.setter
    def centerY(self, value: float):
        """Set centerY"""
        self.__centerY = float(value)

    @property
    def sizeX(self) -> float:
        """Size of surface in x"""
        return self.__sizeX

    @sizeX.setter
    def sizeX(self, value: float):
        """Set sizeX"""
        self.__sizeX = float(value)

    @property
    def sizeY(self) -> float:
        """Size of surface in y"""
        return self.__sizeY

    @sizeY.setter
    def sizeY(self, value: float):
        """Set sizeY"""
        self.__sizeY = float(value)

    @property
    def color(self) -> SIMAColor:
        """"""
        return self.__color

    @color.setter
    def color(self, value: SIMAColor):
        """Set color"""
        self.__color = value

    @property
    def transparency(self) -> float:
        """Transparency of surface"""
        return self.__transparency

    @transparency.setter
    def transparency(self, value: float):
        """Set transparency"""
        self.__transparency = float(value)

    @property
    def meshGridSize(self) -> float:
        """Size of grids in the mesh"""
        return self.__meshGridSize

    @meshGridSize.setter
    def meshGridSize(self, value: float):
        """Set meshGridSize"""
        self.__meshGridSize = float(value)

    @property
    def showMesh(self) -> bool:
        """Show mesh grid on surface"""
        return self.__showMesh

    @showMesh.setter
    def showMesh(self, value: bool):
        """Set showMesh"""
        self.__showMesh = bool(value)

    @property
    def z(self) -> float:
        """Depth of surface"""
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)

    @property
    def lcWaveLength(self) -> float:
        """Length of long-crested wave field"""
        return self.__lcWaveLength

    @lcWaveLength.setter
    def lcWaveLength(self, value: float):
        """Set lcWaveLength"""
        self.__lcWaveLength = float(value)

    @property
    def lcWaveWidth(self) -> float:
        """Width of long-crested wave field"""
        return self.__lcWaveWidth

    @lcWaveWidth.setter
    def lcWaveWidth(self, value: float):
        """Set lcWaveWidth"""
        self.__lcWaveWidth = float(value)

    @property
    def lcWaveNumPoints(self) -> int:
        """Number of points in long-crested wave field"""
        return self.__lcWaveNumPoints

    @lcWaveNumPoints.setter
    def lcWaveNumPoints(self, value: int):
        """Set lcWaveNumPoints"""
        self.__lcWaveNumPoints = int(value)
