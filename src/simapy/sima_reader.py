"""
Reader that handles SIMA specific JSON
"""

from typing import Sequence
from dmt.entity import Entity
from dmt.dmt_reader import DMTReader
from sima.modelcontent import ModelContent

class SIMAReader():
    """ Creates entities from Dicts or file """

    def read(self, filename) -> Sequence[Entity]:
        """ Read entity from file """
        modelcontent: ModelContent =  DMTReader().read(filename)
        return modelcontent.contents
