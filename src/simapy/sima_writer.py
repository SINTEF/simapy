""" Export entites with package information"""

import json
from sima.packageinfo import PackageInfo
from dmt.entity import Entity
from typing import Dict, Sequence
from dmt.dmt_writer import DMTWriter
from sima.modelcontent import ModelContent
from sima.header import Header
from sima.package_info import packages

class SIMAWriter():
    """ Export entites as SIMA objects"""


    def write(self, models: Sequence[Entity], filename: str, indent=0):
        with open(filename, 'w', encoding="utf-8") as fp:
            dict=self.to_dict(models)
            json.dump(dict,fp,indent=indent)


    def to_dict(self, models: Sequence[Entity]) -> Dict:
        """Convert to SIMA dictionary"""
        content = ModelContent()
        header = Header()

        for package in packages:
            header.packages.append(PackageInfo(**package))

        content.header = header
        content.contents.extend(models)
        return DMTWriter().to_dict(content)
