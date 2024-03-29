# This an autogenerated file
# 
# Generated with RequirementOutputSlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.requirementoutputslot import RequirementOutputSlotBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .outputslot import OutputSlot
from .requirement import Requirement

class RequirementOutputSlot(OutputSlot):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    useQuery : bool
         Use boolean expressions using operators =, !=,&&,|| to create more advanced queries(default False)
    query : str
         (default None)
    userRequirements : List[Requirement]
    flatten : bool
         (default False)
    """

    def __init__(self , description="", useQuery=False, flatten=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.useQuery = useQuery
        self.query = None
        self.userRequirements = list()
        self.flatten = flatten
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RequirementOutputSlotBlueprint()


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
    def useQuery(self) -> bool:
        """Use boolean expressions using operators =, !=,&&,|| to create more advanced queries"""
        return self.__useQuery

    @useQuery.setter
    def useQuery(self, value: bool):
        """Set useQuery"""
        self.__useQuery = bool(value)

    @property
    def query(self) -> str:
        """"""
        return self.__query

    @query.setter
    def query(self, value: str):
        """Set query"""
        self.__query = value

    @property
    def userRequirements(self) -> List[Requirement]:
        """"""
        return self.__userRequirements

    @userRequirements.setter
    def userRequirements(self, value: List[Requirement]):
        """Set userRequirements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__userRequirements = value

    @property
    def flatten(self) -> bool:
        """"""
        return self.__flatten

    @flatten.setter
    def flatten(self, value: bool):
        """Set flatten"""
        self.__flatten = bool(value)
