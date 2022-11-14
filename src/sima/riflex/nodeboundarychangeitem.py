# This an autogenerated file
# 
# Generated with NodeBoundaryChangeItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.nodeboundarychangeitem import NodeBoundaryChangeItemBlueprint
from typing import Dict
from sima.riflex.boundarychangeoption import BoundaryChangeOption
from sima.riflex.boundarychangereference import BoundaryChangeReference
from sima.riflex.boundarycondition import BoundaryCondition
from sima.riflex.nodereference import NodeReference
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.supportvessel import SupportVessel
    from sima.simo.supernodereference import SuperNodeReference

class NodeBoundaryChangeItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    boundaryChangeOption : BoundaryChangeOption
         Boundary change option
    surgeConstraint : BoundaryCondition
         Boundary condition for translation in X-direction.
    swayConstraint : BoundaryCondition
         Boundary condition for translation in Y-direction.
    heaveConstraint : BoundaryCondition
         Boundary condition for translation in Z-direction.
    rollConstraint : BoundaryCondition
         Boundary condition for rotation about X-axis
    pitchConstraint : BoundaryCondition
         Boundary condition for rotation about Y-axis
    yawConstraint : BoundaryCondition
         Boundary condition for rotation about Z-axis
    supportVessel : SupportVessel
    _type : BoundaryChangeReference
    superNode : SuperNodeReference
    node : NodeReference
    masterType : BoundaryChangeReference
    master : SuperNodeReference
    masterNodeReference : NodeReference
    """

    def __init__(self , description="", _id=None, boundaryChangeOption=BoundaryChangeOption.FREE, surgeConstraint=BoundaryCondition.FIXED, swayConstraint=BoundaryCondition.FIXED, heaveConstraint=BoundaryCondition.FIXED, rollConstraint=BoundaryCondition.FIXED, pitchConstraint=BoundaryCondition.FIXED, yawConstraint=BoundaryCondition.FIXED, _type=BoundaryChangeReference.SUPERNODE, masterType=BoundaryChangeReference.SUPERNODE, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.boundaryChangeOption = boundaryChangeOption
        self.surgeConstraint = surgeConstraint
        self.swayConstraint = swayConstraint
        self.heaveConstraint = heaveConstraint
        self.rollConstraint = rollConstraint
        self.pitchConstraint = pitchConstraint
        self.yawConstraint = yawConstraint
        self.supportVessel = None
        self._type = _type
        self.superNode = None
        self.node = None
        self.masterType = masterType
        self.master = None
        self.masterNodeReference = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NodeBoundaryChangeItemBlueprint()


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
    def boundaryChangeOption(self) -> BoundaryChangeOption:
        """Boundary change option"""
        return self.__boundaryChangeOption

    @boundaryChangeOption.setter
    def boundaryChangeOption(self, value: BoundaryChangeOption):
        """Set boundaryChangeOption"""
        self.__boundaryChangeOption = value

    @property
    def surgeConstraint(self) -> BoundaryCondition:
        """Boundary condition for translation in X-direction."""
        return self.__surgeConstraint

    @surgeConstraint.setter
    def surgeConstraint(self, value: BoundaryCondition):
        """Set surgeConstraint"""
        self.__surgeConstraint = value

    @property
    def swayConstraint(self) -> BoundaryCondition:
        """Boundary condition for translation in Y-direction."""
        return self.__swayConstraint

    @swayConstraint.setter
    def swayConstraint(self, value: BoundaryCondition):
        """Set swayConstraint"""
        self.__swayConstraint = value

    @property
    def heaveConstraint(self) -> BoundaryCondition:
        """Boundary condition for translation in Z-direction."""
        return self.__heaveConstraint

    @heaveConstraint.setter
    def heaveConstraint(self, value: BoundaryCondition):
        """Set heaveConstraint"""
        self.__heaveConstraint = value

    @property
    def rollConstraint(self) -> BoundaryCondition:
        """Boundary condition for rotation about X-axis"""
        return self.__rollConstraint

    @rollConstraint.setter
    def rollConstraint(self, value: BoundaryCondition):
        """Set rollConstraint"""
        self.__rollConstraint = value

    @property
    def pitchConstraint(self) -> BoundaryCondition:
        """Boundary condition for rotation about Y-axis"""
        return self.__pitchConstraint

    @pitchConstraint.setter
    def pitchConstraint(self, value: BoundaryCondition):
        """Set pitchConstraint"""
        self.__pitchConstraint = value

    @property
    def yawConstraint(self) -> BoundaryCondition:
        """Boundary condition for rotation about Z-axis"""
        return self.__yawConstraint

    @yawConstraint.setter
    def yawConstraint(self, value: BoundaryCondition):
        """Set yawConstraint"""
        self.__yawConstraint = value

    @property
    def supportVessel(self) -> SupportVessel:
        """"""
        return self.__supportVessel

    @supportVessel.setter
    def supportVessel(self, value: SupportVessel):
        """Set supportVessel"""
        self.__supportVessel = value

    @property
    def _type(self) -> BoundaryChangeReference:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: BoundaryChangeReference):
        """Set _type"""
        self.___type = value

    @property
    def superNode(self) -> SuperNodeReference:
        """"""
        return self.__superNode

    @superNode.setter
    def superNode(self, value: SuperNodeReference):
        """Set superNode"""
        self.__superNode = value

    @property
    def node(self) -> NodeReference:
        """"""
        return self.__node

    @node.setter
    def node(self, value: NodeReference):
        """Set node"""
        self.__node = value

    @property
    def masterType(self) -> BoundaryChangeReference:
        """"""
        return self.__masterType

    @masterType.setter
    def masterType(self, value: BoundaryChangeReference):
        """Set masterType"""
        self.__masterType = value

    @property
    def master(self) -> SuperNodeReference:
        """"""
        return self.__master

    @master.setter
    def master(self, value: SuperNodeReference):
        """Set master"""
        self.__master = value

    @property
    def masterNodeReference(self) -> NodeReference:
        """"""
        return self.__masterNodeReference

    @masterNodeReference.setter
    def masterNodeReference(self, value: NodeReference):
        """Set masterNodeReference"""
        self.__masterNodeReference = value
