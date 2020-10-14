# coding: utf-8
"""INI type"""

# standard
import io
import sys
import configparser
from collections import OrderedDict

# third
from pygments import highlight, lexers, formatters

FILETYPE_NAME = "INI"
FILETYPE_EXAMPLE_LOADER = """OrderedDict([
            ('general', OrderedDict([
                ('user', 'admin')
            ])),
            ('keys', OrderedDict([
                ('key1', 'value1'),
                ('key2', 'value2')
            ]))
        ])
"""
FILETYPE_EXAMPLE_DUMPER = """[general]
        user = admin
        [keys]
        key1 = value1
        key2 = value2
"""


def loader(data_string):
    config = configparser.ConfigParser()
    config.read_string(data_string)
    return config._sections


def dumper(data):
    parser = configparser.ConfigParser()
    parser.read_dict(data)

    buf = io.StringIO()
    parser.write(buf)

    return buf.getvalue()


def colorizer(content):
    return highlight(content, lexers.IniLexer(), formatters.TerminalFormatter())
