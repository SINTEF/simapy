""" Export entites with package information"""

from typing import Dict, Sequence

from dmt.dmt_writer import DMTWriter
from dmt.entity import Entity

from .sima.header import Header
from .sima.modelcontent import ModelContent
from .sima.package_info import packages
from .sima.packageinfo import PackageInfo
from .sima.sima.moao import MOAO


class SIMAWriter():
    """ Export entites as SIMA objects"""

    def write(self, models: Sequence[MOAO], filename: str, indent=0):
        """Write SIMA models to file"""
        content = self.__to_model_content(models)
        DMTWriter().write(content, filename, indent=indent)

    def __to_model_content(self, models: Sequence[Entity]) -> ModelContent:
        content = ModelContent()
        header = Header()

        for name,version in packages.items():
            header.packages.append(PackageInfo(name=name,version=version))

        content.header = header
        content.contents.extend(models)
        return content

    def to_dict(self, models: Sequence[MOAO]) -> Dict:
        """Convert to SIMA dictionary"""
        content = self.__to_model_content(models)
        return DMTWriter().to_dict(content)
