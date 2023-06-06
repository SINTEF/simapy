"""
Reader that handles SIMA specific JSON
"""

from typing import Sequence
from dmt.entity import Entity
from dmt.dmt_reader import DMTReader
from .sima.modelcontent import ModelContent

class SIMAReader():
    """ Creates entities from Dicts or file """

    def read(self, filename) -> Sequence[Entity]:
        """ Read entity from file """
        res = DMTReader(root_package="simapy").read(filename)
        if isinstance(res, Sequence):
            modelcontent: ModelContent =  res[0]
        else:
            modelcontent: ModelContent =  res
        return modelcontent.contents
