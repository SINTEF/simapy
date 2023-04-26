"""
Reader that handles SIMA specific .json or .s5 files.
"""

import os
from typing import Sequence
from dmt.entity import Entity
from dmt.dmt_reader import DMTReader
from sima.modelcontent import ModelContent
from simapy.signals.s5_reader import S5Reader

class SIMAReader():
    """ Creates entities from Dicts or file """

    def read(self, filename) -> Sequence[Entity]:
        """ Read entity from file """
        if self.__is_s5(filename):
            return  S5Reader().read(filename)
        else:
            modelcontent: ModelContent =  DMTReader().read(filename)
            return modelcontent.contents

    def __is_s5(self,filename):
        _, extension = os.path.splitext(filename)
        extension = extension.lower()
        return extension=='.s5'
