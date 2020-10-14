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

import sys

# exit immediatly
assert sys.version_info >= (3, 6, 0), "wildq requires Python 3.6+"

import os
from pathlib import Path  # noqa E402
from setuptools import setup, find_packages

from wildq._wildq_version import version


CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


setup(
    extras_require={
        "dev": [
            "alabaster==0.7.12",
            "altgraph==0.17",
            "appdirs==1.4.4",
            "attrs==20.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "babel==2.8.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "bandit==1.6.2",
            "black==19.10b0",
            "cached-property==1.5.2",
            "cerberus==1.3.2",
            "certifi==2020.6.20",
            "cfgv==3.2.0; python_full_version >= '3.6.1'",
            "chardet==3.0.4",
            "click==7.1.2",
            "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "coverage==5.3",
            "distlib==0.3.1",
            "docutils==0.16; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "filelock==3.0.12",
            "flake8==3.8.4",
            "flake8-bugbear==20.1.4",
            "gitdb==4.0.5; python_version >= '3.4'",
            "gitpython==3.1.9; python_version >= '3.4'",
            "identify==1.5.6; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "imagesize==1.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "importlib-metadata==2.0.0; python_version < '3.8'",
            "importlib-resources==3.0.0; python_version < '3.7'",
            "jinja2==2.11.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "markupsafe==1.1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "mccabe==0.6.1",
            "nodeenv==1.5.0",
            "orderedmultidict==1.0.1",
            "packaging==20.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pathspec==0.8.0",
            "pbr==5.5.0; python_version >= '2.6'",
            "pep517==0.8.2",
            "pip-shims==0.5.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "pipenv==2020.8.13",
            "pipenv-setup==3.1.1",
            "pipfile==0.0.2",
            "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pre-commit==2.7.1",
            "pycodestyle==2.6.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pyflakes==2.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pygments==2.7.1",
            "pyinstaller==4.0",
            "pyinstaller-hooks-contrib==2020.9",
            "pyparsing==2.4.7; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pytz==2020.1",
            "pyyaml==5.3.1",
            "regex==2020.10.11",
            "requests==2.24.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "requirementslib==1.5.13; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "smmap==3.0.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "snowballstemmer==2.0.0",
            "sphinx==3.2.1",
            "sphinx-rtd-theme==0.5.0",
            "sphinxcontrib-applehelp==1.0.2; python_version >= '3.5'",
            "sphinxcontrib-devhelp==1.0.2; python_version >= '3.5'",
            "sphinxcontrib-htmlhelp==1.0.3; python_version >= '3.5'",
            "sphinxcontrib-jsmath==1.0.1; python_version >= '3.5'",
            "sphinxcontrib-qthelp==1.0.3; python_version >= '3.5'",
            "sphinxcontrib-serializinghtml==1.1.4; python_version >= '3.5'",
            "stevedore==3.2.2; python_version >= '3.6'",
            "toml==0.10.1",
            "tomlkit==0.7.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "typed-ast==1.4.1",
            "typing==3.7.4.3; python_version < '3.7'",
            "urllib3==1.25.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
            "virtualenv==20.0.34; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "virtualenv-clone==0.5.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "wheel==0.35.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "zipp==3.3.0; python_version < '3.8'",
        ]
    },
    install_requires=[
        "click==7.1.2",
        "jq==1.1.1",
        "pygments==2.7.1",
        "pyhcl==0.4.4",
        "pyyaml==5.3.1",
        "toml==0.10.1",
        "xmltodict==0.12.0",
    ],
    name="wildq",
    # use_scm_version={"local_scheme": "no-local-version"},
    # setup_requires=["setuptools_scm"],
    # py_modules=["_wildq_version"],
    version=version,
    description="Command-line TOML/JSON/INI/YAML/XML processor using jq c bindings.",
    long_description=(CURRENT_DIR / "README.md").read_text(encoding="utf8"),
    long_description_content_type="text/markdown",
    author="Ahmet Demir",
    author_email="me@ahmet2mir.eu",
    url="https://github.com/ahmet2mir/wildq",
    project_urls={
        "Changelog": "https://wildq.readthedocs.io/en/latest/changelog.html"
    },
    license="Apache 2.0",

    python_requires=">=3.6",
    zip_safe=False,
    entry_points={
        "console_scripts": ["wildq=wildq.wildq:main", "wq=wildq.__main__:main"]
    },
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
        "hcl",
        "color",
        "highlight",
    ],
    test_suite="tests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Build Tools",
    ],
)
