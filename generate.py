#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Code generator for python
Will locate all folders within the input_dir and generate a package per folder
folder name will become the package name

Usage:
    generate.py [--cleanup] [--source] <input_dir> [<output_dir>]

Arguments:

Options:
    -h --help  Show this screen
    --version  Show version
    --cleanup  Delete the output folder before generation
    --source  Only generate source packages and skip library specific parts
"""

import os
import sys
from pathlib import Path
from docopt import docopt
from dmtpygen import generator

def __main():
    args = docopt(__doc__, version="Code generator version 1")

    input_dir = args["<input_dir>"]
    if not input_dir:
        raise ValueError("input model root folder does not exist: ", input_dir)

    source = args["--source"]
    root_dir = Path(os.path.dirname(sys.argv[0]))
    output_dir = args["<output_dir>"]
    if not output_dir:
        output_dir = root_dir / "output"

    cleanup = args["--cleanup"]

    config = {
        "source" : source,
        "cleanup" : cleanup,
        "version" : "0.1.0",
        "license" : "UNKNOWN"
    }

    generator.generate(Path(input_dir), Path(output_dir),config)


if __name__ == "__main__":
    __main()
