# This an autogenerated file
# 
# Generated with Axis
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.axis import AxisBlueprint
from typing import Dict
from marmo.report.font import Font

class Axis(Entity):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    font : Font
    log : bool
         (default True)
    autoformat : bool
         (default True)
    format : str
         (default "")
    autoscale : bool
         (default True)
    showgrid : bool
         (default True)
    dashgridline : bool
         (default True)
    """

    def __init__(self , name="", description="", log=True, autoformat=True, format="", autoscale=True, showgrid=True, dashgridline=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.font = None
        self.log = log
        self.autoformat = autoformat
        self.format = format
        self.autoscale = autoscale
        self.showgrid = showgrid
        self.dashgridline = dashgridline
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AxisBlueprint()


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
    def font(self) -> Font:
        """"""
        return self.__font

    @font.setter
    def font(self, value: Font):
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
    def autoformat(self) -> bool:
        """"""
        return self.__autoformat

    @autoformat.setter
    def autoformat(self, value: bool):
        """Set autoformat"""
        self.__autoformat = bool(value)

    @property
    def format(self) -> str:
        """"""
        return self.__format

    @format.setter
    def format(self, value: str):
        """Set format"""
        self.__format = str(value)

    @property
    def autoscale(self) -> bool:
        """"""
        return self.__autoscale

    @autoscale.setter
    def autoscale(self, value: bool):
        """Set autoscale"""
        self.__autoscale = bool(value)

    @property
    def showgrid(self) -> bool:
        """"""
        return self.__showgrid

    @showgrid.setter
    def showgrid(self, value: bool):
        """Set showgrid"""
        self.__showgrid = bool(value)

    @property
    def dashgridline(self) -> bool:
        """"""
        return self.__dashgridline

    @dashgridline.setter
    def dashgridline(self, value: bool):
        """Set dashgridline"""
        self.__dashgridline = bool(value)
