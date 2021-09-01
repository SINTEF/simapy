# This an autogenerated file
# 
# Generated with AxisConfiguration
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.axisconfiguration import AxisConfigurationBlueprint
from sima.sima.fontdescription import FontDescription
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class AxisConfiguration(MOAO):
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
    font : FontDescription
    log : bool
         (default False)
    autoFormat : bool
         (default True)
    format : str
         (default '0.####E0')
    showGrid : bool
         (default True)
    dashGridLine : bool
         (default False)
    autoScale : bool
         (default True)
    minimum : float
         (default 0.0)
    maximum : float
         (default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", log:bool=False, autoFormat:bool=True, format:str='0.####E0', showGrid:bool=True, dashGridLine:bool=False, autoScale:bool=True, minimum:float=0.0, maximum:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__font = FontDescription()
        self.__log = log
        self.__autoFormat = autoFormat
        self.__format = format
        self.__showGrid = showGrid
        self.__dashGridLine = dashGridLine
        self.__autoScale = autoScale
        self.__minimum = minimum
        self.__maximum = maximum
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AxisConfigurationBlueprint()


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
    def font(self) -> FontDescription:
        """"""
        return self.__font

    @font.setter
    def font(self, value: FontDescription):
        """Set font"""
        self.__font = value

    @property
    def log(self) -> bool:
        """"""
        return self.__log

    @log.setter
    def log(self, value: bool):
        """Set log"""
        self.__log = bool(value)

    @property
    def autoFormat(self) -> bool:
        """"""
        return self.__autoFormat

    @autoFormat.setter
    def autoFormat(self, value: bool):
        """Set autoFormat"""
        self.__autoFormat = bool(value)

    @property
    def format(self) -> str:
        """"""
        return self.__format

    @format.setter
    def format(self, value: str):
        """Set format"""
        self.__format = str(value)

    @property
    def showGrid(self) -> bool:
        """"""
        return self.__showGrid

    @showGrid.setter
    def showGrid(self, value: bool):
        """Set showGrid"""
        self.__showGrid = bool(value)

    @property
    def dashGridLine(self) -> bool:
        """"""
        return self.__dashGridLine

    @dashGridLine.setter
    def dashGridLine(self, value: bool):
        """Set dashGridLine"""
        self.__dashGridLine = bool(value)

    @property
    def autoScale(self) -> bool:
        """"""
        return self.__autoScale

    @autoScale.setter
    def autoScale(self, value: bool):
        """Set autoScale"""
        self.__autoScale = bool(value)

    @property
    def minimum(self) -> float:
        """"""
        return self.__minimum

    @minimum.setter
    def minimum(self, value: float):
        """Set minimum"""
        self.__minimum = float(value)

    @property
    def maximum(self) -> float:
        """"""
        return self.__maximum

    @maximum.setter
    def maximum(self, value: float):
        """Set maximum"""
        self.__maximum = float(value)
