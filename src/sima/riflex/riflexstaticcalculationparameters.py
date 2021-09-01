# This an autogenerated file
# 
# Generated with RIFLEXStaticCalculationParameters
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.riflexstaticcalculationparameters import RIFLEXStaticCalculationParametersBlueprint
from sima.riflex.loadandmassformulation import LoadAndMassFormulation
from sima.riflex.matrixplotstorage import MatrixPlotStorage
from sima.riflex.matrixstorage import MatrixStorage
from sima.riflex.parametervariation import ParameterVariation
from sima.riflex.staticloadcomponent import StaticLoadComponent
from sima.riflex.staticloadtypeitem import StaticLoadTypeItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class RIFLEXStaticCalculationParameters(MOAO):
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
    loadTypeItems : List[StaticLoadTypeItem]
    matrixStorage : MatrixStorage
    currentProfileScaling : float
         Scaling factor to amplify or reduce the referred current profile(default 1.0)
    staticLoadComponents : List[StaticLoadComponent]
    stressFreeConfiguration : bool
         Whether a stress free configuration has been defined for the Slender system.(default False)
    stressfreeFile : str
         (default "")
    loadAndMassFormulation : LoadAndMassFormulation
    parameterVariation : ParameterVariation
    storeVisualisationResponses : bool
         Store visualisation responses indicator(default True)
    matrixPlotStorage : MatrixPlotStorage
         Storage option for Matrix Plot
    startAtZero : bool
         Start arc length at zero for each line(default True)
    """

    def __init__(self , name:str="", description:str="", _id:str="", matrixStorage:MatrixStorage=MatrixStorage.SKYLINE, currentProfileScaling:float=1.0, stressFreeConfiguration:bool=False, stressfreeFile:str="", loadAndMassFormulation:LoadAndMassFormulation=LoadAndMassFormulation.LUMPED, storeVisualisationResponses:bool=True, matrixPlotStorage:MatrixPlotStorage=MatrixPlotStorage.LOAD_GROUP, startAtZero:bool=True, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__loadTypeItems = list()
        self.__matrixStorage = matrixStorage
        self.__currentProfileScaling = currentProfileScaling
        self.__staticLoadComponents = list()
        self.__stressFreeConfiguration = stressFreeConfiguration
        self.__stressfreeFile = stressfreeFile
        self.__loadAndMassFormulation = loadAndMassFormulation
        self.__parameterVariation = ParameterVariation()
        self.__storeVisualisationResponses = storeVisualisationResponses
        self.__matrixPlotStorage = matrixPlotStorage
        self.__startAtZero = startAtZero
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXStaticCalculationParametersBlueprint()


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
    def loadTypeItems(self) -> List[StaticLoadTypeItem]:
        """"""
        return self.__loadTypeItems

    @loadTypeItems.setter
    def loadTypeItems(self, value: List[StaticLoadTypeItem]):
        """Set loadTypeItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__loadTypeItems = value

    @property
    def matrixStorage(self) -> MatrixStorage:
        """"""
        return self.__matrixStorage

    @matrixStorage.setter
    def matrixStorage(self, value: MatrixStorage):
        """Set matrixStorage"""
        self.__matrixStorage = value

    @property
    def currentProfileScaling(self) -> float:
        """Scaling factor to amplify or reduce the referred current profile"""
        return self.__currentProfileScaling

    @currentProfileScaling.setter
    def currentProfileScaling(self, value: float):
        """Set currentProfileScaling"""
        self.__currentProfileScaling = float(value)

    @property
    def staticLoadComponents(self) -> List[StaticLoadComponent]:
        """"""
        return self.__staticLoadComponents

    @staticLoadComponents.setter
    def staticLoadComponents(self, value: List[StaticLoadComponent]):
        """Set staticLoadComponents"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__staticLoadComponents = value

    @property
    def stressFreeConfiguration(self) -> bool:
        """Whether a stress free configuration has been defined for the Slender system."""
        return self.__stressFreeConfiguration

    @stressFreeConfiguration.setter
    def stressFreeConfiguration(self, value: bool):
        """Set stressFreeConfiguration"""
        self.__stressFreeConfiguration = bool(value)

    @property
    def stressfreeFile(self) -> str:
        """"""
        return self.__stressfreeFile

    @stressfreeFile.setter
    def stressfreeFile(self, value: str):
        """Set stressfreeFile"""
        self.__stressfreeFile = str(value)

    @property
    def loadAndMassFormulation(self) -> LoadAndMassFormulation:
        """"""
        return self.__loadAndMassFormulation

    @loadAndMassFormulation.setter
    def loadAndMassFormulation(self, value: LoadAndMassFormulation):
        """Set loadAndMassFormulation"""
        self.__loadAndMassFormulation = value

    @property
    def parameterVariation(self) -> ParameterVariation:
        """"""
        return self.__parameterVariation

    @parameterVariation.setter
    def parameterVariation(self, value: ParameterVariation):
        """Set parameterVariation"""
        self.__parameterVariation = value

    @property
    def storeVisualisationResponses(self) -> bool:
        """Store visualisation responses indicator"""
        return self.__storeVisualisationResponses

    @storeVisualisationResponses.setter
    def storeVisualisationResponses(self, value: bool):
        """Set storeVisualisationResponses"""
        self.__storeVisualisationResponses = bool(value)

    @property
    def matrixPlotStorage(self) -> MatrixPlotStorage:
        """Storage option for Matrix Plot"""
        return self.__matrixPlotStorage

    @matrixPlotStorage.setter
    def matrixPlotStorage(self, value: MatrixPlotStorage):
        """Set matrixPlotStorage"""
        self.__matrixPlotStorage = value

    @property
    def startAtZero(self) -> bool:
        """Start arc length at zero for each line"""
        return self.__startAtZero

    @startAtZero.setter
    def startAtZero(self, value: bool):
        """Set startAtZero"""
        self.__startAtZero = bool(value)
