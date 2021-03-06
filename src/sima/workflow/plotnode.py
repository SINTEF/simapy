# This an autogenerated file
# 
# Generated with PlotNode
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.plotnode import PlotNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.figuretemplate import FigureTemplate
from sima.post.inputslot import InputSlot
from sima.post.outputnode import OutputNode
from sima.post.outputslot import OutputSlot
from sima.post.traceconfiguration import TraceConfiguration
from sima.sima.scriptablevalue import ScriptableValue

class PlotNode(OutputNode):
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
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    inputSlot : InputSlot
    figureTemplate : FigureTemplate
    traces : List[TraceConfiguration]
    fixed : bool
         (default False)
    title : str
         (default "")
    xLabel : str
         (default "")
    yLabel : str
         (default "")
    selectAll : bool
         Will export all signals as plot(default False)
    outputSlot : OutputSlot
    createImages : bool
         Create images and store these to disk. The output will then be the paths to the images(default True)
    """

    def __init__(self , name="", description="", _id="", x=0, y=0, h=0, w=0, fixed=False, title="", xLabel="", yLabel="", selectAll=False, createImages=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.inputSlot = None
        self.figureTemplate = None
        self.traces = list()
        self.fixed = fixed
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.selectAll = selectAll
        self.outputSlot = None
        self.createImages = createImages
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PlotNodeBlueprint()


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
    def x(self) -> int:
        """"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """Set x"""
        self.__x = int(value)

    @property
    def y(self) -> int:
        """"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """Set y"""
        self.__y = int(value)

    @property
    def h(self) -> int:
        """"""
        return self.__h

    @h.setter
    def h(self, value: int):
        """Set h"""
        self.__h = int(value)

    @property
    def w(self) -> int:
        """"""
        return self.__w

    @w.setter
    def w(self, value: int):
        """Set w"""
        self.__w = int(value)

    @property
    def controlSignalInputSlots(self) -> List[ControlSignalInputSlot]:
        """"""
        return self.__controlSignalInputSlots

    @controlSignalInputSlots.setter
    def controlSignalInputSlots(self, value: List[ControlSignalInputSlot]):
        """Set controlSignalInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def inputSlot(self) -> InputSlot:
        """"""
        return self.__inputSlot

    @inputSlot.setter
    def inputSlot(self, value: InputSlot):
        """Set inputSlot"""
        self.__inputSlot = value

    @property
    def figureTemplate(self) -> FigureTemplate:
        """"""
        return self.__figureTemplate

    @figureTemplate.setter
    def figureTemplate(self, value: FigureTemplate):
        """Set figureTemplate"""
        self.__figureTemplate = value

    @property
    def traces(self) -> List[TraceConfiguration]:
        """"""
        return self.__traces

    @traces.setter
    def traces(self, value: List[TraceConfiguration]):
        """Set traces"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__traces = value

    @property
    def fixed(self) -> bool:
        """"""
        return self.__fixed

    @fixed.setter
    def fixed(self, value: bool):
        """Set fixed"""
        self.__fixed = bool(value)

    @property
    def title(self) -> str:
        """"""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = str(value)

    @property
    def xLabel(self) -> str:
        """"""
        return self.__xLabel

    @xLabel.setter
    def xLabel(self, value: str):
        """Set xLabel"""
        self.__xLabel = str(value)

    @property
    def yLabel(self) -> str:
        """"""
        return self.__yLabel

    @yLabel.setter
    def yLabel(self, value: str):
        """Set yLabel"""
        self.__yLabel = str(value)

    @property
    def selectAll(self) -> bool:
        """Will export all signals as plot"""
        return self.__selectAll

    @selectAll.setter
    def selectAll(self, value: bool):
        """Set selectAll"""
        self.__selectAll = bool(value)

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value

    @property
    def createImages(self) -> bool:
        """Create images and store these to disk. The output will then be the paths to the images"""
        return self.__createImages

    @createImages.setter
    def createImages(self, value: bool):
        """Set createImages"""
        self.__createImages = bool(value)
