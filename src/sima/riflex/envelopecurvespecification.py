# This an autogenerated file
# 
# Generated with EnvelopeCurveSpecification
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.envelopecurvespecification import EnvelopeCurveSpecificationBlueprint
from typing import Dict
from sima.riflex.matrixplotfileoption import MatrixPlotFileOption
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class EnvelopeCurveSpecification(MOAO):
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
    compDisplacement : bool
         Compute displacement envelopes?(default False)
    compForce : bool
         Compute force envelopes?(default False)
    compCurvature : bool
         Compute curvature envelopes?(default False)
    startTime : float
         Simulation start time for computing envelopes(default 0.0)
    endTime : float
         Simulation end time for computing envelopes(default 10000000.0)
    printDisplacement : bool
         Print displacement envelopes?(default False)
    printForce : bool
         Print force envelopes?(default False)
    printCurvature : bool
         Print curvature envelopes?(default False)
    plotOption : MatrixPlotFileOption
    """

    def __init__(self , name="", description="", _id="", compDisplacement=False, compForce=False, compCurvature=False, startTime=0.0, endTime=10000000.0, printDisplacement=False, printForce=False, printCurvature=False, plotOption=MatrixPlotFileOption.MAX_AND_STANDARD_DEV, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.compDisplacement = compDisplacement
        self.compForce = compForce
        self.compCurvature = compCurvature
        self.startTime = startTime
        self.endTime = endTime
        self.printDisplacement = printDisplacement
        self.printForce = printForce
        self.printCurvature = printCurvature
        self.plotOption = plotOption
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return EnvelopeCurveSpecificationBlueprint()


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
    def compDisplacement(self) -> bool:
        """Compute displacement envelopes?"""
        return self.__compDisplacement

    @compDisplacement.setter
    def compDisplacement(self, value: bool):
        """Set compDisplacement"""
        self.__compDisplacement = bool(value)

    @property
    def compForce(self) -> bool:
        """Compute force envelopes?"""
        return self.__compForce

    @compForce.setter
    def compForce(self, value: bool):
        """Set compForce"""
        self.__compForce = bool(value)

    @property
    def compCurvature(self) -> bool:
        """Compute curvature envelopes?"""
        return self.__compCurvature

    @compCurvature.setter
    def compCurvature(self, value: bool):
        """Set compCurvature"""
        self.__compCurvature = bool(value)

    @property
    def startTime(self) -> float:
        """Simulation start time for computing envelopes"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def endTime(self) -> float:
        """Simulation end time for computing envelopes"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: float):
        """Set endTime"""
        self.__endTime = float(value)

    @property
    def printDisplacement(self) -> bool:
        """Print displacement envelopes?"""
        return self.__printDisplacement

    @printDisplacement.setter
    def printDisplacement(self, value: bool):
        """Set printDisplacement"""
        self.__printDisplacement = bool(value)

    @property
    def printForce(self) -> bool:
        """Print force envelopes?"""
        return self.__printForce

    @printForce.setter
    def printForce(self, value: bool):
        """Set printForce"""
        self.__printForce = bool(value)

    @property
    def printCurvature(self) -> bool:
        """Print curvature envelopes?"""
        return self.__printCurvature

    @printCurvature.setter
    def printCurvature(self, value: bool):
        """Set printCurvature"""
        self.__printCurvature = bool(value)

    @property
    def plotOption(self) -> MatrixPlotFileOption:
        """"""
        return self.__plotOption

    @plotOption.setter
    def plotOption(self, value: MatrixPlotFileOption):
        """Set plotOption"""
        self.__plotOption = value
