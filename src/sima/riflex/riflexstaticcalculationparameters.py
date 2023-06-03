# This an autogenerated file
# 
# Generated with RIFLEXStaticCalculationParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexstaticcalculationparameters import RIFLEXStaticCalculationParametersBlueprint
from typing import Dict
from .loadandmassformulation import LoadAndMassFormulation
from .masssummary import MassSummary
from .matrixplotstorage import MatrixPlotStorage
from .matrixstorage import MatrixStorage
from .parametervariation import ParameterVariation
from .staticloadcomponent import StaticLoadComponent
from .staticloadtypeitem import StaticLoadTypeItem
from sima.sima import MOAO
from sima.sima import ScriptableValue

class RIFLEXStaticCalculationParameters(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
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
         (default None)
    loadAndMassFormulation : LoadAndMassFormulation
    parameterVariation : ParameterVariation
    storeVisualisationResponses : bool
         Store visualisation responses indicator(default True)
    matrixPlotStorage : MatrixPlotStorage
         Storage option for Matrix Plot
    startAtZero : bool
         Start arc length at zero for each line(default True)
    storeStructuralData : bool
         Store additional FEM data(default False)
    massSummary : MassSummary
    """

    def __init__(self , description="", matrixStorage=MatrixStorage.SPARSE, currentProfileScaling=1.0, stressFreeConfiguration=False, loadAndMassFormulation=LoadAndMassFormulation.LUMPED, storeVisualisationResponses=True, matrixPlotStorage=MatrixPlotStorage.LOAD_GROUP, startAtZero=True, storeStructuralData=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.loadTypeItems = list()
        self.matrixStorage = matrixStorage
        self.currentProfileScaling = currentProfileScaling
        self.staticLoadComponents = list()
        self.stressFreeConfiguration = stressFreeConfiguration
        self.stressfreeFile = None
        self.loadAndMassFormulation = loadAndMassFormulation
        self.parameterVariation = None
        self.storeVisualisationResponses = storeVisualisationResponses
        self.matrixPlotStorage = matrixPlotStorage
        self.startAtZero = startAtZero
        self.storeStructuralData = storeStructuralData
        self.massSummary = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXStaticCalculationParametersBlueprint()


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
    def loadTypeItems(self) -> List[StaticLoadTypeItem]:
        """"""
        return self.__loadTypeItems

    @loadTypeItems.setter
    def loadTypeItems(self, value: List[StaticLoadTypeItem]):
        """Set loadTypeItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
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
            raise ValueError("Expected sequense, but was " , type(value))
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
        self.__stressfreeFile = value

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

    @property
    def storeStructuralData(self) -> bool:
        """Store additional FEM data"""
        return self.__storeStructuralData

    @storeStructuralData.setter
    def storeStructuralData(self, value: bool):
        """Set storeStructuralData"""
        self.__storeStructuralData = bool(value)

    @property
    def massSummary(self) -> MassSummary:
        """"""
        return self.__massSummary

    @massSummary.setter
    def massSummary(self, value: MassSummary):
        """Set massSummary"""
        self.__massSummary = value
