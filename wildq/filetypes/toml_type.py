# coding: utf-8
"""TOML type"""

# standard
from collections import OrderedDict

# third
import toml
from pygments import highlight, lexers, formatters

FILETYPE_NAME = "TOML"
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
FILETYPE_EXAMPLE_DUMPER = """# keys = [ "alone" ] # produce an error on dump only
        [[keys]]
        key = "value1"
        [[keys]]
        key = "value2"
        [general]
        user = "admin"
"""


def loader(data_string):
    return toml.loads(data_string)


def dumper(data):
    return toml.dumps(data)


def colorizer(content):
    return highlight(
        content, lexers.TOMLLexer(), formatters.TerminalFormatter()
    )
