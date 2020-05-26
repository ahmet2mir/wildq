# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
wildq - Command-line TOML/JSON/INI/YAML/XML processor using jq c bindings.

Licence
```````
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
__author__ = "Ahmet Demir <me@ahmet2mir.eu>"

from setuptools import setup, find_packages

from wildq.release import __version__

setup(
    name="wildq",
    version=__version__,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ahmet2mir/wildq.git",
    author="Ahmet Demir",
    author_email="me@ahmet2mir.eu",
    description="Command-line TOML/JSON/INI/YAML/XML processor using jq c bindings",
    license="Apache 2.0",
    keywords=[
        "wildq",
        "jq",
        "yaml",
        "json",
        "toml",
        "xml",
        "ini",
        "parser",
        "shell",
    ],
    packages=find_packages(),
    package_data={"": ["README.md"]},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["wildq=wildq.wildq:main", "wq=wildq.wildq:main"]},
    install_requires=[
        "setuptools",
        "PyYAML >= 3.11",
        "toml >= 0.9.4",
        "xmltodict >= 0.12.0",
        "jq >= 1.0.1",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Build Tools",
    ]
)
