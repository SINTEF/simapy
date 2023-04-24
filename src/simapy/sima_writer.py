""" Export entites with package information"""

import json
from typing import Dict, Sequence

from dmt.dmt_writer import DMTWriter
from dmt.entity import Entity

from sima.header import Header
from sima.modelcontent import ModelContent
from sima.package_info import packages
from sima.packageinfo import PackageInfo


class SIMAWriter():
    """ Export entites as SIMA objects"""


    def write(self, models: Sequence[Entity], filename: str, indent=0):
        """Write to file"""
        with open(filename, 'w', encoding="utf-8") as fp:
            asdict=self.to_dict(models)
            json.dump(asdict,fp,indent=indent)


    def to_dict(self, models: Sequence[Entity]) -> Dict:
        """Convert to SIMA dictionary"""
        content = ModelContent()
        header = Header()

        for package in packages:
            header.packages.append(PackageInfo(**package))

        content.header = header
        content.contents.extend(models)
        return DMTWriter().to_dict(content)
