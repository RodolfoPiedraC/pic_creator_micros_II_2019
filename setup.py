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

import setuptools


def read(filename):
    """
    Read a file relative to setup.py location.
    """
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, filename)) as fd:
        return fd.read()


def find_requirements(filename):
    """
    Find requirements in file.
    This reads a file and leaves the requirements as an array of strings
    """
    import string
    content = read(filename)
    requirements = []
    for line in content.splitlines():
        line = line.strip()
        if line and line[:1] in string.ascii_letters:
            requirements.append(line)
    return requirements


with open("README.md", "r") as fh:
    long_description = fh.read()

# Setup Call
setuptools.setup(
    name="micros_imcr",
    version="0.1.0",

    # Packages and executables
    # All python packages will be located under the lib folder
    # This is not a requirement but allows a better order
    package_dir={'': 'lib'},
    packages=setuptools.find_packages('lib'),

    # Scripts are located under the bin directory
    scripts=['bin/micros_imcr'],

    # Dependencies
    install_requires=find_requirements('requirements.txt'),

    # Metadata
    author="Rodolfo Piedra Camacho",
    author_email="rjpiedra@itcr.ac.cr",
    description="Image Creator package",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/RodolfoPiedraC/pic_creator_micros_II_2019",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Intended Audience :: Users'
    ],
    python_requires='>=3.5',
)
