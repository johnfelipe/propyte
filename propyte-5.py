#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# propyte-5                                                                    #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a template Python program that is suited to fast development #
# programs rather than taylored programs. It uses the propyte module and       #
# logging.                                                                     #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

Usage:
    program [options]

Options:
    -h, --help               display help message
    --version                display version and exit
    -v, --verbose            verbose logging
    -s, --silent             silent
    -u, --username=USERNAME  username
    --data=FILENAME          input data file [default: data.txt]
"""

name    = "propyte-5"
version = "2015-10-22T1630Z"
logo    = None

import os
import sys
import time
import docopt
import logging
import propyte

def main(options):

    global program
    program = propyte.Program(
        options = options,
        name    = name,
        version = version,
        logo    = logo
        )
    from propyte import log

    log.info("")

    # access options and arguments
    input_data_filename = options["--data"]

    log.info("input data file: {filename}".format(
        filename = input_data_filename
    ))

    log.debug("start to print log messages at various levels")

    log.debug("message at level DEBUG")
    log.info("message at level INFO")
    log.warning("message at level WARNING")
    log.error("message at level ERROR")
    log.critical("message at level CRITICAL")

    log.debug("stop printing log messages at various levels")

    log.info("")

    program.terminate()

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
