# coding: utf-8
"""YAML type"""

# standard
from collections import OrderedDict

# third
import yaml
from pygments import highlight, lexers, formatters

FILETYPE_NAME = "YAML"
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
FILETYPE_EXAMPLE_DUMPER = """general:
          user: "admin"
        keys:
          - key1: value1
          - key2: value2
          - alone
"""


def loader(data_string):
    return yaml.safe_load(data_string)


def dumper(data):
    # Dump YAML thanks to https://github.com/dale3h/python-lovelace.
    def ordered_dump(content, stream=None, Dumper=yaml.Dumper, **kwargs):
        """YAML dumper for OrderedDict."""

        class OrderedDumper(Dumper):
            """Wrapper class for YAML dumper."""

            def ignore_aliases(self, content):
                """Disable aliases in YAML dump."""
                return True

            def increase_indent(self, flow=False, indentless=False):
                """Increase indent on YAML lists."""
                return super(OrderedDumper, self).increase_indent(flow, False)

        def _dict_representer(dumper, content):
            """Function to represent OrderDict and derivitives."""
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, content.items()
            )

        OrderedDumper.add_multi_representer(OrderedDict, _dict_representer)

        OrderedDumper.add_representer(
            str, yaml.representer.SafeRepresenter.represent_str
        )

        return yaml.dump(content, stream, OrderedDumper, **kwargs)

    return ordered_dump(
        content=data, Dumper=yaml.SafeDumper, default_flow_style=False
    )


def colorizer(content):
    return highlight(
        content, lexers.YamlLexer(), formatters.TerminalFormatter()
    )
