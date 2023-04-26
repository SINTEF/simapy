# This an autogenerated file
# 
# Generated with HydrodynamicCrossSectionProperties
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hydrodynamiccrosssectionproperties import HydrodynamicCrossSectionPropertiesBlueprint
from typing import Dict
from sima.sima import MOAO
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .excitationzoneproperty import ExcitationZoneProperty
    from .addedmassproperty import AddedMassProperty
    from .excitationcoefficientsproperty import ExcitationCoefficientsProperty
    from .dampingfactorproperty import DampingFactorProperty
    from .strouhalspecificationproperty import StrouhalSpecificationProperty

class HydrodynamicCrossSectionProperties(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    itemNumber : int
         Global segment number(default 0)
    excitationZoneProperty : ExcitationZoneProperty
         Excitation zone
    addedMassCrossFlowProperty : AddedMassProperty
         Cross-flow added mass
    excitationCoefficientCrossFlowProperty : ExcitationCoefficientsProperty
         Cross-flow excitation coefficients
    dampingFactorProperty : DampingFactorProperty
         Hydrodynamic damping factor
    addedMassInLineProperty : AddedMassProperty
         In-line added mass
    excitationCoefficientInLineProperty : ExcitationCoefficientsProperty
         In-line excitation coefficients
    strouhalSpecificationProperty : StrouhalSpecificationProperty
         Strouhal number
    """

    def __init__(self , description="", itemNumber=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.itemNumber = itemNumber
        self.excitationZoneProperty = None
        self.addedMassCrossFlowProperty = None
        self.excitationCoefficientCrossFlowProperty = None
        self.dampingFactorProperty = None
        self.addedMassInLineProperty = None
        self.excitationCoefficientInLineProperty = None
        self.strouhalSpecificationProperty = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HydrodynamicCrossSectionPropertiesBlueprint()


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
    def itemNumber(self) -> int:
        """Global segment number"""
        return self.__itemNumber

    @itemNumber.setter
    def itemNumber(self, value: int):
        """Set itemNumber"""
        self.__itemNumber = int(value)

    @property
    def excitationZoneProperty(self) -> ExcitationZoneProperty:
        """Excitation zone"""
        return self.__excitationZoneProperty

    @excitationZoneProperty.setter
    def excitationZoneProperty(self, value: ExcitationZoneProperty):
        """Set excitationZoneProperty"""
        self.__excitationZoneProperty = value

    @property
    def addedMassCrossFlowProperty(self) -> AddedMassProperty:
        """Cross-flow added mass"""
        return self.__addedMassCrossFlowProperty

    @addedMassCrossFlowProperty.setter
    def addedMassCrossFlowProperty(self, value: AddedMassProperty):
        """Set addedMassCrossFlowProperty"""
        self.__addedMassCrossFlowProperty = value

    @property
    def excitationCoefficientCrossFlowProperty(self) -> ExcitationCoefficientsProperty:
        """Cross-flow excitation coefficients"""
        return self.__excitationCoefficientCrossFlowProperty

    @excitationCoefficientCrossFlowProperty.setter
    def excitationCoefficientCrossFlowProperty(self, value: ExcitationCoefficientsProperty):
        """Set excitationCoefficientCrossFlowProperty"""
        self.__excitationCoefficientCrossFlowProperty = value

    @property
    def dampingFactorProperty(self) -> DampingFactorProperty:
        """Hydrodynamic damping factor"""
        return self.__dampingFactorProperty

    @dampingFactorProperty.setter
    def dampingFactorProperty(self, value: DampingFactorProperty):
        """Set dampingFactorProperty"""
        self.__dampingFactorProperty = value

    @property
    def addedMassInLineProperty(self) -> AddedMassProperty:
        """In-line added mass"""
        return self.__addedMassInLineProperty

    @addedMassInLineProperty.setter
    def addedMassInLineProperty(self, value: AddedMassProperty):
        """Set addedMassInLineProperty"""
        self.__addedMassInLineProperty = value

    @property
    def excitationCoefficientInLineProperty(self) -> ExcitationCoefficientsProperty:
        """In-line excitation coefficients"""
        return self.__excitationCoefficientInLineProperty

    @excitationCoefficientInLineProperty.setter
    def excitationCoefficientInLineProperty(self, value: ExcitationCoefficientsProperty):
        """Set excitationCoefficientInLineProperty"""
        self.__excitationCoefficientInLineProperty = value

    @property
    def strouhalSpecificationProperty(self) -> StrouhalSpecificationProperty:
        """Strouhal number"""
        return self.__strouhalSpecificationProperty

    @strouhalSpecificationProperty.setter
    def strouhalSpecificationProperty(self, value: StrouhalSpecificationProperty):
        """Set strouhalSpecificationProperty"""
        self.__strouhalSpecificationProperty = value