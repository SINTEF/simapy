# This an autogenerated file
# 
# Generated with OptimizationWorkflowNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.optimizationworkflownode import OptimizationWorkflowNodeBlueprint
from typing import Dict
from .optimizationcalculationparameters import OptimizationCalculationParameters
from .optimizationvariableitem import OptimizationVariableItem
from sima.post import ControlSignalInputSlot
from sima.sima import ScriptableValue
from sima.workflow import ModelReferenceInputSlot
from sima.workflow import VariableInputSlot
from sima.workflow import WorkflowInputSlot
from sima.workflow import WorkflowOutputSlot
from sima.workflow import WorkflowReferenceNode
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.workflow import Workflow
    from sima.workflow import WorkflowOutput

class OptimizationWorkflowNode(WorkflowReferenceNode):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    variableInputSlots : List[VariableInputSlot]
    modelReferenceInputSlot : ModelReferenceInputSlot
    workflow : Workflow
    workflowOutputSlots : List[WorkflowOutputSlot]
    workflowInputSlots : List[WorkflowInputSlot]
    inputWorkflow : bool
         Set the workflow input from the outside. Use a model reference as source.(default False)
    setFolderName : bool
         Override the default folder name created. This folder will be relative to the running workflow. If left empty it will create the results directly in the workflow folder.(default False)
    folderName : str
         (default None)
    optimizationCalculationParameters : OptimizationCalculationParameters
    costFunction : WorkflowOutput
    constraints : WorkflowOutput
    variableItems : List[OptimizationVariableItem]
    result : WorkflowOutputSlot
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, inputWorkflow=False, setFolderName=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.variableInputSlots = list()
        self.modelReferenceInputSlot = None
        self.workflow = None
        self.workflowOutputSlots = list()
        self.workflowInputSlots = list()
        self.inputWorkflow = inputWorkflow
        self.setFolderName = setFolderName
        self.folderName = None
        self.optimizationCalculationParameters = None
        self.costFunction = None
        self.constraints = None
        self.variableItems = list()
        self.result = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OptimizationWorkflowNodeBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def variableInputSlots(self) -> List[VariableInputSlot]:
        """"""
        return self.__variableInputSlots

    @variableInputSlots.setter
    def variableInputSlots(self, value: List[VariableInputSlot]):
        """Set variableInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variableInputSlots = value

    @property
    def modelReferenceInputSlot(self) -> ModelReferenceInputSlot:
        """"""
        return self.__modelReferenceInputSlot

    @modelReferenceInputSlot.setter
    def modelReferenceInputSlot(self, value: ModelReferenceInputSlot):
        """Set modelReferenceInputSlot"""
        self.__modelReferenceInputSlot = value

    @property
    def workflow(self) -> Workflow:
        """"""
        return self.__workflow

    @workflow.setter
    def workflow(self, value: Workflow):
        """Set workflow"""
        self.__workflow = value

    @property
    def workflowOutputSlots(self) -> List[WorkflowOutputSlot]:
        """"""
        return self.__workflowOutputSlots

    @workflowOutputSlots.setter
    def workflowOutputSlots(self, value: List[WorkflowOutputSlot]):
        """Set workflowOutputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__workflowOutputSlots = value

    @property
    def workflowInputSlots(self) -> List[WorkflowInputSlot]:
        """"""
        return self.__workflowInputSlots

    @workflowInputSlots.setter
    def workflowInputSlots(self, value: List[WorkflowInputSlot]):
        """Set workflowInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__workflowInputSlots = value

    @property
    def inputWorkflow(self) -> bool:
        """Set the workflow input from the outside. Use a model reference as source."""
        return self.__inputWorkflow

    @inputWorkflow.setter
    def inputWorkflow(self, value: bool):
        """Set inputWorkflow"""
        self.__inputWorkflow = bool(value)

    @property
    def setFolderName(self) -> bool:
        """Override the default folder name created. This folder will be relative to the running workflow. If left empty it will create the results directly in the workflow folder."""
        return self.__setFolderName

    @setFolderName.setter
    def setFolderName(self, value: bool):
        """Set setFolderName"""
        self.__setFolderName = bool(value)

    @property
    def folderName(self) -> str:
        """"""
        return self.__folderName

    @folderName.setter
    def folderName(self, value: str):
        """Set folderName"""
        self.__folderName = value

    @property
    def optimizationCalculationParameters(self) -> OptimizationCalculationParameters:
        """"""
        return self.__optimizationCalculationParameters

    @optimizationCalculationParameters.setter
    def optimizationCalculationParameters(self, value: OptimizationCalculationParameters):
        """Set optimizationCalculationParameters"""
        self.__optimizationCalculationParameters = value

    @property
    def costFunction(self) -> WorkflowOutput:
        """"""
        return self.__costFunction

    @costFunction.setter
    def costFunction(self, value: WorkflowOutput):
        """Set costFunction"""
        self.__costFunction = value

    @property
    def constraints(self) -> WorkflowOutput:
        """"""
        return self.__constraints

    @constraints.setter
    def constraints(self, value: WorkflowOutput):
        """Set constraints"""
        self.__constraints = value

    @property
    def variableItems(self) -> List[OptimizationVariableItem]:
        """"""
        return self.__variableItems

    @variableItems.setter
    def variableItems(self, value: List[OptimizationVariableItem]):
        """Set variableItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variableItems = value

    @property
    def result(self) -> WorkflowOutputSlot:
        """"""
        return self.__result

    @result.setter
    def result(self, value: WorkflowOutputSlot):
        """Set result"""
        self.__result = value