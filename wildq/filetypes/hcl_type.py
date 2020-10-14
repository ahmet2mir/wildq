# coding: utf-8
"""HCL type"""

# standard
import json
from collections import OrderedDict

# third
import hcl
from pygments import highlight, lexers, formatters

FILETYPE_NAME = "HCL"
FILETYPE_EXAMPLE_LOADER = """{
            'general': {
                'user': 'admin'
            },
            'keys': [
                {'key': 'value1'},
                {'key': 'value2'}
            ]
        }
"""
FILETYPE_EXAMPLE_DUMPER = """general {
            user = "admin"
        }
        keys {
            key = "value1"
        }
        keys {
            key = "value2"
        }
"""


def loader(data_string):
    return hcl.loads(data_string)


def dumper(data):
    return json.dumps(data, indent=4)


def colorizer(content):
    # dump to hcl is not supported, so fallback to json
    return highlight(
        content,
        lexers.JsonLexer(),  # lexers.TerraformLexer()
        formatters.TerminalFormatter(),
    )
