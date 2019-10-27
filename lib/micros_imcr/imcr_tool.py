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

from micros_imcr.main import micros_imcr_main
from os.path import exists, isfile


class MicrosImcrData():
    """
    Structure to store the path to json. This is needed to use the
    micros_imcr_main from main

    :path_to_json: String that contains the path to the JSON file
    """
    def __init__(self, file_path):

        # Check that the path_to_json ends up in a existing file
        if exists(file_path):
            if not isfile(file_path):
                raise TypeError(
                    'Wrong path parameter: It must be an existing file'
                )
        else:
            raise TypeError(
                'Wrong path parameter: File not found'
            )
        self.path_to_json = file_path


def micros_imcr_tool(path_to_json):
    """
    Main call of the IMCR package via a tool
    Takes a path to a JSON file and creates a set of default images

    :param path_to_json: Relative path to the data.json file
    """

    # Initialize a MicrosImcrData class with the required filepath
    args = MicrosImcrData(path_to_json)

    # Call the micros_imcr_main method
    micros_imcr_main(args)
