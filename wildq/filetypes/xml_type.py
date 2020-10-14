# coding: utf-8
"""XML type"""

import json
from collections import OrderedDict

import xmltodict
from pygments import highlight, lexers, formatters

FILETYPE_NAME = "XML"
FILETYPE_EXAMPLE_LOADER = """OrderedDict([
            ('root', OrderedDict([
                ('general', OrderedDict([
                    ('user', 'admin')
                ])),
                ('keys', OrderedDict([
                    ('element', [
                        OrderedDict([('key', 'value1')]),
                        OrderedDict([('key', 'value2')]),
                        'alone'
                    ])
                ]))
            ]))
        ])
"""
FILETYPE_EXAMPLE_DUMPER = """<?xml version="1.0" encoding="UTF-8"?>
        <root>
           <general>
              <user>admin</user>
           </general>
           <keys>
              <element>
                 <key>value1</key>
              </element>
              <element>
                 <key>value2</key>
              </element>
              <element>alone</element>
           </keys>
        </root>
"""


# local


def loader(data_string):
    return xmltodict.parse(data_string)


def dumper(data):
    if isinstance(data, dict) and len(data.keys()) == 1:
        return xmltodict.unparse(data, pretty=True, indent="   ")
    else:
        return xmltodict.unparse(
            {"virtualroot": data}, pretty=True, indent="   "
        )


def colorizer(content):
    return highlight(content, lexers.XmlLexer(), formatters.TerminalFormatter())
