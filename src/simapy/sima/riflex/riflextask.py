# This an autogenerated file
# 
# Generated with RIFLEXTask
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflextask import RIFLEXTaskBlueprint
from typing import Dict
from ..condition import ConditionTaskCondition
from ..condition import InitialCondition
from ..condition import ModelVariation
from ..sima import DoubleVariable
from ..sima import IntegerVariable
from ..sima import ModelReferenceVariable
from ..sima import SIMAScript
from ..sima import ScriptableValue
from ..sima import StringVariable
from ..simo import MassUnit
from ..simo import SIMOTask
from .riflexmodel import RIFLEXModel

class RIFLEXTask(SIMOTask):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    doubleVariables : List[DoubleVariable]
    integerVariables : List[IntegerVariable]
    stringVariables : List[StringVariable]
    runNumber : int
         (default 0)
    scripts : List[SIMAScript]
    variations : List[ModelVariation]
    referenceVariables : List[ModelReferenceVariable]
    initialCondition : InitialCondition
    conditions : List[ConditionTaskCondition]
    model : RIFLEXModel
    simoMemory : int
         Enables override of the default memory settings for SIMO. Given in MB(default 128)
    removeIntermediateFiles : bool
         (default True)
    exportMassUnit : MassUnit
         Used as export unit for mass ( and indirectly force)
    riflexStamodMemory : int
         Enables override of the default memory settings. Given in MB(default 512)
    numRiflexStamodArrays : int
         Enables override of the default memory settings(default 20000)
    riflexDynmodMemory : int
         Enables override of the default memory settings. Given in MB. Also used for VIVANA and Eigenvalue analysis(default 512)
    vivanaWorkArraySize : int
         Enables override of the default memory settings(default 9000000)
    maxRiflexArrays : int
         Enables override of the default memory settings(default 2000)
    riflexOutmodMemory : int
         Enables override of the default memory settings. Given in MB(default 32)
    skipRiflexDynmodTransformation : bool
         (default True)
    """

    def __init__(self , description="", runNumber=0, simoMemory=128, removeIntermediateFiles=True, exportMassUnit=MassUnit.MG, riflexStamodMemory=512, numRiflexStamodArrays=20000, riflexDynmodMemory=512, vivanaWorkArraySize=9000000, maxRiflexArrays=2000, riflexOutmodMemory=32, skipRiflexDynmodTransformation=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.doubleVariables = list()
        self.integerVariables = list()
        self.stringVariables = list()
        self.runNumber = runNumber
        self.scripts = list()
        self.variations = list()
        self.referenceVariables = list()
        self.initialCondition = None
        self.conditions = list()
        self.model = None
        self.simoMemory = simoMemory
        self.removeIntermediateFiles = removeIntermediateFiles
        self.exportMassUnit = exportMassUnit
        self.riflexStamodMemory = riflexStamodMemory
        self.numRiflexStamodArrays = numRiflexStamodArrays
        self.riflexDynmodMemory = riflexDynmodMemory
        self.vivanaWorkArraySize = vivanaWorkArraySize
        self.maxRiflexArrays = maxRiflexArrays
        self.riflexOutmodMemory = riflexOutmodMemory
        self.skipRiflexDynmodTransformation = skipRiflexDynmodTransformation
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXTaskBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def doubleVariables(self) -> List[DoubleVariable]:
        """"""
        return self.__doubleVariables

    @doubleVariables.setter
    def doubleVariables(self, value: List[DoubleVariable]):
        """Set doubleVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__doubleVariables = value

    @property
    def integerVariables(self) -> List[IntegerVariable]:
        """"""
        return self.__integerVariables

    @integerVariables.setter
    def integerVariables(self, value: List[IntegerVariable]):
        """Set integerVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__integerVariables = value

    @property
    def stringVariables(self) -> List[StringVariable]:
        """"""
        return self.__stringVariables

    @stringVariables.setter
    def stringVariables(self, value: List[StringVariable]):
        """Set stringVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scripts = value

    @property
    def variations(self) -> List[ModelVariation]:
        """"""
        return self.__variations

    @variations.setter
    def variations(self, value: List[ModelVariation]):
        """Set variations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variations = value

    @property
    def referenceVariables(self) -> List[ModelReferenceVariable]:
        """"""
        return self.__referenceVariables

    @referenceVariables.setter
    def referenceVariables(self, value: List[ModelReferenceVariable]):
        """Set referenceVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__referenceVariables = value

    @property
    def initialCondition(self) -> InitialCondition:
        """"""
        return self.__initialCondition

    @initialCondition.setter
    def initialCondition(self, value: InitialCondition):
        """Set initialCondition"""
        self.__initialCondition = value

    @property
    def conditions(self) -> List[ConditionTaskCondition]:
        """"""
        return self.__conditions

    @conditions.setter
    def conditions(self, value: List[ConditionTaskCondition]):
        """Set conditions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__conditions = value

    @property
    def model(self) -> RIFLEXModel:
        """"""
        return self.__model

    @model.setter
    def model(self, value: RIFLEXModel):
        """Set model"""
        self.__model = value

    @property
    def simoMemory(self) -> int:
        """Enables override of the default memory settings for SIMO. Given in MB"""
        return self.__simoMemory

    @simoMemory.setter
    def simoMemory(self, value: int):
        """Set simoMemory"""
        self.__simoMemory = int(value)

    @property
    def removeIntermediateFiles(self) -> bool:
        """"""
        return self.__removeIntermediateFiles

    @removeIntermediateFiles.setter
    def removeIntermediateFiles(self, value: bool):
        """Set removeIntermediateFiles"""
        self.__removeIntermediateFiles = bool(value)

    @property
    def exportMassUnit(self) -> MassUnit:
        """Used as export unit for mass ( and indirectly force)"""
        return self.__exportMassUnit

    @exportMassUnit.setter
    def exportMassUnit(self, value: MassUnit):
        """Set exportMassUnit"""
        self.__exportMassUnit = value

    @property
    def riflexStamodMemory(self) -> int:
        """Enables override of the default memory settings. Given in MB"""
        return self.__riflexStamodMemory

    @riflexStamodMemory.setter
    def riflexStamodMemory(self, value: int):
        """Set riflexStamodMemory"""
        self.__riflexStamodMemory = int(value)

    @property
    def numRiflexStamodArrays(self) -> int:
        """Enables override of the default memory settings"""
        return self.__numRiflexStamodArrays

    @numRiflexStamodArrays.setter
    def numRiflexStamodArrays(self, value: int):
        """Set numRiflexStamodArrays"""
        self.__numRiflexStamodArrays = int(value)

    @property
    def riflexDynmodMemory(self) -> int:
        """Enables override of the default memory settings. Given in MB. Also used for VIVANA and Eigenvalue analysis"""
        return self.__riflexDynmodMemory

    @riflexDynmodMemory.setter
    def riflexDynmodMemory(self, value: int):
        """Set riflexDynmodMemory"""
        self.__riflexDynmodMemory = int(value)

    @property
    def vivanaWorkArraySize(self) -> int:
        """Enables override of the default memory settings"""
        return self.__vivanaWorkArraySize

    @vivanaWorkArraySize.setter
    def vivanaWorkArraySize(self, value: int):
        """Set vivanaWorkArraySize"""
        self.__vivanaWorkArraySize = int(value)

    @property
    def maxRiflexArrays(self) -> int:
        """Enables override of the default memory settings"""
        return self.__maxRiflexArrays

    @maxRiflexArrays.setter
    def maxRiflexArrays(self, value: int):
        """Set maxRiflexArrays"""
        self.__maxRiflexArrays = int(value)

    @property
    def riflexOutmodMemory(self) -> int:
        """Enables override of the default memory settings. Given in MB"""
        return self.__riflexOutmodMemory

    @riflexOutmodMemory.setter
    def riflexOutmodMemory(self, value: int):
        """Set riflexOutmodMemory"""
        self.__riflexOutmodMemory = int(value)

    @property
    def skipRiflexDynmodTransformation(self) -> bool:
        """"""
        return self.__skipRiflexDynmodTransformation

    @skipRiflexDynmodTransformation.setter
    def skipRiflexDynmodTransformation(self, value: bool):
        """Set skipRiflexDynmodTransformation"""
        self.__skipRiflexDynmodTransformation = bool(value)
