# This an autogenerated file
# 
# Generated with ContactSurfacePoint
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.contactsurfacepoint import ContactSurfacePointBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .end import End
from .segmentreference import SegmentReference
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .arline import ARLine
    from .tensioner import Tensioner
    from .rollercontact import RollerContact
    from .tubularcontact import TubularContact

class ContactSurfacePoint(SegmentReference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    segmentEnd : End
         Local segment end (1 or 2).
    tensioner : Tensioner
         Reference to tensioner contact type.
    rollerContact : RollerContact
         Reference to roller contact type.
    tubularContact : TubularContact
         Reference to tubular contact type.
    """

    def __init__(self , description="", segment=1, allSegments=False, segmentEnd=End.ONE, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.segmentEnd = segmentEnd
        self.tensioner = None
        self.rollerContact = None
        self.tubularContact = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ContactSurfacePointBlueprint()


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
    def segmentEnd(self) -> End:
        """Local segment end (1 or 2)."""
        return self.__segmentEnd

    @segmentEnd.setter
    def segmentEnd(self, value: End):
        """Set segmentEnd"""
        self.__segmentEnd = value

    @property
    def tensioner(self) -> Tensioner:
        """Reference to tensioner contact type."""
        return self.__tensioner

    @tensioner.setter
    def tensioner(self, value: Tensioner):
        """Set tensioner"""
        self.__tensioner = value

    @property
    def rollerContact(self) -> RollerContact:
        """Reference to roller contact type."""
        return self.__rollerContact

    @rollerContact.setter
    def rollerContact(self, value: RollerContact):
        """Set rollerContact"""
        self.__rollerContact = value

    @property
    def tubularContact(self) -> TubularContact:
        """Reference to tubular contact type."""
        return self.__tubularContact

    @tubularContact.setter
    def tubularContact(self, value: TubularContact):
        """Set tubularContact"""
        self.__tubularContact = value
