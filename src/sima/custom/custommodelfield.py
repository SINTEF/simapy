# This an autogenerated file
# 
# Generated with CustomModelField
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.custommodelfield import CustomModelFieldBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class CustomModelField(CustomComponent):
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
    label : str
         (default "")
    tooltip : str
         (default "")
    model : MOAO
    customTooltip : bool
         (default False)
    customLabel : bool
         (default False)
    readOnly : bool
         (default False)
    featureName : str
         (default "")
    """

    def __init__(self , name="", description="", _id="", label="", tooltip="", customTooltip=False, customLabel=False, readOnly=False, featureName="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.label = label
        self.tooltip = tooltip
        self.model = None
        self.customTooltip = customTooltip
        self.customLabel = customLabel
        self.readOnly = readOnly
        self.featureName = featureName
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomModelFieldBlueprint()


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
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = str(value)

    @property
    def model(self) -> MOAO:
        """"""
        return self.__model

    @model.setter
    def model(self, value: MOAO):
        """Set model"""
        self.__model = value

    @property
    def customTooltip(self) -> bool:
        """"""
        return self.__customTooltip

    @customTooltip.setter
    def customTooltip(self, value: bool):
        """Set customTooltip"""
        self.__customTooltip = bool(value)

    @property
    def customLabel(self) -> bool:
        """"""
        return self.__customLabel

    @customLabel.setter
    def customLabel(self, value: bool):
        """Set customLabel"""
        self.__customLabel = bool(value)

    @property
    def readOnly(self) -> bool:
        """"""
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, value: bool):
        """Set readOnly"""
        self.__readOnly = bool(value)

    @property
    def featureName(self) -> str:
        """"""
        return self.__featureName

    @featureName.setter
    def featureName(self, value: str):
        """Set featureName"""
        self.__featureName = str(value)
