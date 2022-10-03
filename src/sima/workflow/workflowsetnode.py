# This an autogenerated file
# 
# Generated with WorkflowSetNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowsetnode import WorkflowSetNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.iteration import Iteration
from sima.workflow.modelreferenceinputslot import ModelReferenceInputSlot
from sima.workflow.variableinputset import VariableInputSet
from sima.workflow.variableinputsetslot import VariableInputSetSlot
from sima.workflow.variableinputslot import VariableInputSlot
from sima.workflow.workflowinputslot import WorkflowInputSlot
from sima.workflow.workflowoutputslot import WorkflowOutputSlot
from sima.workflow.workflowreferencenode import WorkflowReferenceNode
from sima.workflow.workflowsetinput import WorkflowSetInput
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.workflow.workflow import Workflow

class WorkflowSetNode(WorkflowReferenceNode):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
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
         (default "")
    variableInputSets : List[VariableInputSet]
    variableInputSetSlots : List[VariableInputSetSlot]
    writeRunStatus : bool
         Write a text file with the run status after running all the cases(default False)
    runStatusFolder : str
         If provided the status file(s) will  to exported to this location(default "")
    input : WorkflowSetInput
         Specify variable values from file.
    filename : str
         Import variable values from file. Expected file format:\n' any comment specified with '\n'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  \n1.0      2.0    3\n4.0      5.0    4\n'any comment\n           (default "")
    iteration : Iteration
         Switch to change type of iteration
    distribute : bool
         Distribute workflow using SIMACompute(default False)
    grouping : int
         Group given amount of runs together in the same process. Should be used if workflow within takes a relative short amount of time compared to forking off a new process(default 1)
    iterateOverInput : bool
         Enable iteration over workflow inputs. The iteration will loop over all input folders with type=workflow(default False)
    workflowInputVariationSlots : List[WorkflowInputSlot]
    """

    def __init__(self , _id="", name="", x=0, y=0, h=0, w=0, inputWorkflow=False, setFolderName=False, folderName="", writeRunStatus=False, runStatusFolder="", input=WorkflowSetInput.MANUAL, filename="", iteration=Iteration.COLUMN, distribute=False, grouping=1, iterateOverInput=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
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
        self.folderName = folderName
        self.variableInputSets = list()
        self.variableInputSetSlots = list()
        self.writeRunStatus = writeRunStatus
        self.runStatusFolder = runStatusFolder
        self.input = input
        self.filename = filename
        self.iteration = iteration
        self.distribute = distribute
        self.grouping = grouping
        self.iterateOverInput = iterateOverInput
        self.workflowInputVariationSlots = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowSetNodeBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def variableInputSlots(self) -> List[VariableInputSlot]:
        """"""
        return self.__variableInputSlots

    @variableInputSlots.setter
    def variableInputSlots(self, value: List[VariableInputSlot]):
        """Set variableInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
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
            raise Exception("Expected sequense, but was " , type(value))
        self.__workflowOutputSlots = value

    @property
    def workflowInputSlots(self) -> List[WorkflowInputSlot]:
        """"""
        return self.__workflowInputSlots

    @workflowInputSlots.setter
    def workflowInputSlots(self, value: List[WorkflowInputSlot]):
        """Set workflowInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
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
        self.__folderName = str(value)

    @property
    def variableInputSets(self) -> List[VariableInputSet]:
        """"""
        return self.__variableInputSets

    @variableInputSets.setter
    def variableInputSets(self, value: List[VariableInputSet]):
        """Set variableInputSets"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variableInputSets = value

    @property
    def variableInputSetSlots(self) -> List[VariableInputSetSlot]:
        """"""
        return self.__variableInputSetSlots

    @variableInputSetSlots.setter
    def variableInputSetSlots(self, value: List[VariableInputSetSlot]):
        """Set variableInputSetSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variableInputSetSlots = value

    @property
    def writeRunStatus(self) -> bool:
        """Write a text file with the run status after running all the cases"""
        return self.__writeRunStatus

    @writeRunStatus.setter
    def writeRunStatus(self, value: bool):
        """Set writeRunStatus"""
        self.__writeRunStatus = bool(value)

    @property
    def runStatusFolder(self) -> str:
        """If provided the status file(s) will  to exported to this location"""
        return self.__runStatusFolder

    @runStatusFolder.setter
    def runStatusFolder(self, value: str):
        """Set runStatusFolder"""
        self.__runStatusFolder = str(value)

    @property
    def input(self) -> WorkflowSetInput:
        """Specify variable values from file."""
        return self.__input

    @input.setter
    def input(self, value: WorkflowSetInput):
        """Set input"""
        self.__input = value

    @property
    def filename(self) -> str:
        """Import variable values from file. Expected file format:
' any comment specified with '
'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  
1.0      2.0    3
4.0      5.0    4
'any comment
           """
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        """Set filename"""
        self.__filename = str(value)

    @property
    def iteration(self) -> Iteration:
        """Switch to change type of iteration"""
        return self.__iteration

    @iteration.setter
    def iteration(self, value: Iteration):
        """Set iteration"""
        self.__iteration = value

    @property
    def distribute(self) -> bool:
        """Distribute workflow using SIMACompute"""
        return self.__distribute

    @distribute.setter
    def distribute(self, value: bool):
        """Set distribute"""
        self.__distribute = bool(value)

    @property
    def grouping(self) -> int:
        """Group given amount of runs together in the same process. Should be used if workflow within takes a relative short amount of time compared to forking off a new process"""
        return self.__grouping

    @grouping.setter
    def grouping(self, value: int):
        """Set grouping"""
        self.__grouping = int(value)

    @property
    def iterateOverInput(self) -> bool:
        """Enable iteration over workflow inputs. The iteration will loop over all input folders with type=workflow"""
        return self.__iterateOverInput

    @iterateOverInput.setter
    def iterateOverInput(self, value: bool):
        """Set iterateOverInput"""
        self.__iterateOverInput = bool(value)

    @property
    def workflowInputVariationSlots(self) -> List[WorkflowInputSlot]:
        """"""
        return self.__workflowInputVariationSlots

    @workflowInputVariationSlots.setter
    def workflowInputVariationSlots(self, value: List[WorkflowInputSlot]):
        """Set workflowInputVariationSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__workflowInputVariationSlots = value
