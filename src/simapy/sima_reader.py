"""
Reader that handles SIMA specific JSON
"""

from typing import Sequence
from dmt.entity import Entity
from dmt.dmt_reader import DMTReader
from .sima.modelcontent import ModelContent
from .sima.package_info import packages

class SIMAReader():
    """ Creates entities from Dicts or file """

    def read(self, filename) -> Sequence[Entity]:
        """ Read entity from file """
        res = DMTReader(root_package="simapy").read(filename)
        if isinstance(res, Sequence):
            modelcontent: ModelContent =  res[0]
        else:
            modelcontent: ModelContent =  res
        self.__check_version(modelcontent)
        return modelcontent.contents

    def __check_version(self, modelcontent: ModelContent):
        """ Check if imported model has the same version as the reader """
        header = modelcontent.header
        if header:
            pkgs = modelcontent.header.packages
            for pkg in pkgs:
                version = packages.get(pkg.name)
                if not version:
                    raise ValueError(f"Unknown package {pkg.name}")
                if version != pkg.version:
                    raise ValueError(f"Package {pkg.name} has version {pkg.version} but reader expects {version}. Please use the correct version of simapy for the corresponding version of SIMA.")
