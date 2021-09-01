# This an autogenerated file
# 
# Generated with FatigueAnalysisItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.fatigueanalysisitem import FatigueAnalysisItemBlueprint
from sima.riflex.elementreference import ElementReference
from sima.riflex.end import End
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine
    from sima.riflex.sncurve import SNCurve

class FatigueAnalysisItem(ElementReference):
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
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    elementNumber : int
         Local element number on actual segment(default 1)
    allElements : bool
         All elements(default False)
    allEnds : bool
         All ends(default False)
    elementEnd : End
         End number 1 or 2
    stressConcentrationFactor : float
         Stress consentration factor(default 1.0)
    snCurve : SNCurve
    effectiveThickness : float
         Thickness used in thickness correction of the SN curves. Default value is the same as the wall thickness(default 0.0)
    crossSectionalArea : float
         Optional cross sectional area(default 0.0)
    sectionModulus : float
         Optional section modulus(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", segment:int=1, allSegments:bool=False, elementNumber:int=1, allElements:bool=False, allEnds:bool=False, elementEnd:End=End.ONE, stressConcentrationFactor:float=1.0, effectiveThickness:float=0.0, crossSectionalArea:float=0.0, sectionModulus:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__line = None
        self.__segment = segment
        self.__allSegments = allSegments
        self.__elementNumber = elementNumber
        self.__allElements = allElements
        self.__allEnds = allEnds
        self.__elementEnd = elementEnd
        self.__stressConcentrationFactor = stressConcentrationFactor
        self.__snCurve = None
        self.__effectiveThickness = effectiveThickness
        self.__crossSectionalArea = crossSectionalArea
        self.__sectionModulus = sectionModulus
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FatigueAnalysisItemBlueprint()


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
    def line(self) -> ARLine:
        """Line"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def segment(self) -> int:
        """Segment on given line"""
        return self.__segment

    @segment.setter
    def segment(self, value: int):
        """Set segment"""
        self.__segment = int(value)

    @property
    def allSegments(self) -> bool:
        """All segments"""
        return self.__allSegments

    @allSegments.setter
    def allSegments(self, value: bool):
        """Set allSegments"""
        self.__allSegments = bool(value)

    @property
    def elementNumber(self) -> int:
        """Local element number on actual segment"""
        return self.__elementNumber

    @elementNumber.setter
    def elementNumber(self, value: int):
        """Set elementNumber"""
        self.__elementNumber = int(value)

    @property
    def allElements(self) -> bool:
        """All elements"""
        return self.__allElements

    @allElements.setter
    def allElements(self, value: bool):
        """Set allElements"""
        self.__allElements = bool(value)

    @property
    def allEnds(self) -> bool:
        """All ends"""
        return self.__allEnds

    @allEnds.setter
    def allEnds(self, value: bool):
        """Set allEnds"""
        self.__allEnds = bool(value)

    @property
    def elementEnd(self) -> End:
        """End number 1 or 2"""
        return self.__elementEnd

    @elementEnd.setter
    def elementEnd(self, value: End):
        """Set elementEnd"""
        self.__elementEnd = value

    @property
    def stressConcentrationFactor(self) -> float:
        """Stress consentration factor"""
        return self.__stressConcentrationFactor

    @stressConcentrationFactor.setter
    def stressConcentrationFactor(self, value: float):
        """Set stressConcentrationFactor"""
        self.__stressConcentrationFactor = float(value)

    @property
    def snCurve(self) -> SNCurve:
        """"""
        return self.__snCurve

    @snCurve.setter
    def snCurve(self, value: SNCurve):
        """Set snCurve"""
        self.__snCurve = value

    @property
    def effectiveThickness(self) -> float:
        """Thickness used in thickness correction of the SN curves. Default value is the same as the wall thickness"""
        return self.__effectiveThickness

    @effectiveThickness.setter
    def effectiveThickness(self, value: float):
        """Set effectiveThickness"""
        self.__effectiveThickness = float(value)

    @property
    def crossSectionalArea(self) -> float:
        """Optional cross sectional area"""
        return self.__crossSectionalArea

    @crossSectionalArea.setter
    def crossSectionalArea(self, value: float):
        """Set crossSectionalArea"""
        self.__crossSectionalArea = float(value)

    @property
    def sectionModulus(self) -> float:
        """Optional section modulus"""
        return self.__sectionModulus

    @sectionModulus.setter
    def sectionModulus(self, value: float):
        """Set sectionModulus"""
        self.__sectionModulus = float(value)
