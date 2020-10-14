# coding: utf-8
"""JSON type"""

# standard
import json
from collections import OrderedDict

# third
from pygments import highlight, lexers, formatters

FILETYPE_NAME = "JSON"
FILETYPE_EXAMPLE_LOADER = """{
            'general': {
                'user': 'admin'
            },
            'keys': [
                {'key': 'value1'},
                {'key': 'value2'},
                'alone'
            ]
        }
"""
FILETYPE_EXAMPLE_DUMPER = """{
            "general": {
                "user": "admin"
            },
            "keys": [
                {"key": "value1"},
                {"key": "value2"},
                "alone"
            ]
        }
"""


def loader(data_string):
    return json.loads(data_string)


def dumper(data):
    return json.dumps(data, indent=4)


def colorizer(content):
    return highlight(
        content, lexers.JsonLexer(), formatters.TerminalFormatter()
    )
