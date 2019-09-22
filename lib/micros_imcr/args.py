# -*- coding: utf-8 -*-
#
# Copyright 2019 Rodolfo José Piedra Camacho

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Argument management module.
"""

from os.path import exists, isfile

import logging

from . import __version__


# Log object
log = logging.getLogger(__name__)


FORMAT = '%(asctime)s:::%(levelname)s:::%(message)s'
V_LEVELS = {
    0: logging.ERROR,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}


def validate_args(args):
    """
    Validate that arguments are valid.

    :param args: An arguments namespace.
    :return: The validated namespace.
    """
    # Check that args were passed
    if args is None:
        log.error("No arguments were passed to the pvtrace script")
        return 0

    # Setup log level according to the -v argument
    level = V_LEVELS.get(args.verbose, logging.ERROR)
    logging.basicConfig(format=FORMAT, level=level)

    log.debug('Raw arguments:\n{}'.format(args))

    # Verify if the path_to_src directory exists
    if exists(args.path_to_json) is False:
        raise TypeError(
            'Path to Json does not exists'
        )

    # Check that the path_to_json ends up in a existing file
    if exists(args.path_to_json):
        if not isfile(args.path_to_json):
            raise TypeError(
                'Wrong path parameter: It must be an existing file'
            )
    else:
        raise TypeError(
            'Wrong path parameter: File not found'
        )

    return args


def parse_args(argv=None):
    """
    Argument parsing routine.

    :param argv: A list of argument strings.
    :rtype argv: list
    :return: A parsed and verified arguments namespace.
    :rtype: :py:class:`argparse.Namespace`
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description='Call tracer logging call generator'
    )

    # Obligatory Arguments
    # --------------------
    parser.add_argument(
        'path_to_json',
        default="default_data.json",
        help='Absolute path to the json file with the, size, color and format'
             ' information.'
    )

    # Misc Arguments
    # --------------
    parser.add_argument(
        '--version',
        action='version',
        version='Call micros_imcr v{}'.format(__version__)
    )

    # Optional Arguments
    # --------------------
    parser.add_argument(
        '-v', '--verbose',
        action='count',
        default=0,
        help='Increase verbosity level',
    )

    args = parser.parse_args(argv)
    args = validate_args(args)
    return args


__all__ = ['parse_args']
