# This an autogenerated file
# 
# Generated with HLATask
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.hlatask import HLATaskBlueprint
from typing import Dict
from sima.hla.controlpanel import ControlPanel
from sima.hla.hladatatable import HLADataTable
from sima.hla.hlafederate import HLAFederate
from sima.hla.hlamodel import HLAModel
from sima.hla.hlasignalplot import HLASignalPlot
from sima.sima.doublevariable import DoubleVariable
from sima.sima.integervariable import IntegerVariable
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simascript import SIMAScript
from sima.sima.stringvariable import StringVariable
from sima.sima.task import Task

class HLATask(Task):
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
    doubleVariables : List[DoubleVariable]
    integerVariables : List[IntegerVariable]
    stringVariables : List[StringVariable]
    runNumber : int
         (default 0)
    scripts : List[SIMAScript]
    model : HLAModel
    federates : List[HLAFederate]
    accelerationFactor : float
         Acceleration factor. (1 means real time)(default 1.0)
    restartAutomatically : bool
         If automatic restart is checked, the HLA federation will be restarted when it ends (even if it ends because of an error)(default True)
    dataTables : List[HLADataTable]
    plots : List[HLASignalPlot]
    controlPanels : List[ControlPanel]
    """

    def __init__(self , name="", description="", _id="", runNumber=0, accelerationFactor=1.0, restartAutomatically=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.doubleVariables = list()
        self.integerVariables = list()
        self.stringVariables = list()
        self.runNumber = runNumber
        self.scripts = list()
        self.model = None
        self.federates = list()
        self.accelerationFactor = accelerationFactor
        self.restartAutomatically = restartAutomatically
        self.dataTables = list()
        self.plots = list()
        self.controlPanels = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLATaskBlueprint()


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
    def doubleVariables(self) -> List[DoubleVariable]:
        """"""
        return self.__doubleVariables

    @doubleVariables.setter
    def doubleVariables(self, value: List[DoubleVariable]):
        """Set doubleVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__doubleVariables = value

    @property
    def integerVariables(self) -> List[IntegerVariable]:
        """"""
        return self.__integerVariables

    @integerVariables.setter
    def integerVariables(self, value: List[IntegerVariable]):
        """Set integerVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__integerVariables = value

    @property
    def stringVariables(self) -> List[StringVariable]:
        """"""
        return self.__stringVariables

    @stringVariables.setter
    def stringVariables(self, value: List[StringVariable]):
        """Set stringVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__stringVariables = value

    @property
    def runNumber(self) -> int:
        """"""
        return self.__runNumber

    @runNumber.setter
    def runNumber(self, value: int):
        """Set runNumber"""
        self.__runNumber = int(value)

    @property
    def scripts(self) -> List[SIMAScript]:
        """"""
        return self.__scripts

    @scripts.setter
    def scripts(self, value: List[SIMAScript]):
        """Set scripts"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scripts = value

    @property
    def model(self) -> HLAModel:
        """"""
        return self.__model

    @model.setter
    def model(self, value: HLAModel):
        """Set model"""
        self.__model = value

    @property
    def federates(self) -> List[HLAFederate]:
        """"""
        return self.__federates

    @federates.setter
    def federates(self, value: List[HLAFederate]):
        """Set federates"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__federates = value

    @property
    def accelerationFactor(self) -> float:
        """Acceleration factor. (1 means real time)"""
        return self.__accelerationFactor

    @accelerationFactor.setter
    def accelerationFactor(self, value: float):
        """Set accelerationFactor"""
        self.__accelerationFactor = float(value)

    @property
    def restartAutomatically(self) -> bool:
        """If automatic restart is checked, the HLA federation will be restarted when it ends (even if it ends because of an error)"""
        return self.__restartAutomatically

    @restartAutomatically.setter
    def restartAutomatically(self, value: bool):
        """Set restartAutomatically"""
        self.__restartAutomatically = bool(value)

    @property
    def dataTables(self) -> List[HLADataTable]:
        """"""
        return self.__dataTables

    @dataTables.setter
    def dataTables(self, value: List[HLADataTable]):
        """Set dataTables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__dataTables = value

    @property
    def plots(self) -> List[HLASignalPlot]:
        """"""
        return self.__plots

    @plots.setter
    def plots(self, value: List[HLASignalPlot]):
        """Set plots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__plots = value

    @property
    def controlPanels(self) -> List[ControlPanel]:
        """"""
        return self.__controlPanels

    @controlPanels.setter
    def controlPanels(self, value: List[ControlPanel]):
        """Set controlPanels"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlPanels = value
