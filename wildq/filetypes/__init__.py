# coding: utf-8
from wildq.filetypes import hcl_type
from wildq.filetypes import ini_type
from wildq.filetypes import json_type
from wildq.filetypes import toml_type
from wildq.filetypes import xml_type
from wildq.filetypes import yaml_type

# Auto Doc
for ft in [hcl_type, ini_type, json_type, toml_type, xml_type, yaml_type]:
    ft.loader.__doc__ = f"""Pass data as string to {ft.FILETYPE_NAME} loader.

    Args:
        data_string (str): String content to load, usually a file content.

    Returns:
        Loaded content. Return type depends on content format,
        should be dict, list, string etc.

    Examples:
        >>> from wildq.filetypes import {ft.FILETYPE_NAME.lower()}_type
        >>> with open("examples/{ft.FILETYPE_NAME.lower()}.{ft.FILETYPE_NAME.lower()}", "r") as fd:
        ...   data_string = fd.read()
        >>> data = {ft.FILETYPE_NAME.lower()}_type.loader(data_string)
        {ft.FILETYPE_EXAMPLE_LOADER}
    """

    ft.dumper.__doc__ = f"""Pass loaded data to {ft.FILETYPE_NAME} dumper.

    Args:
        data: Should be dict, list, string etc.

    Returns:
        str: Dumped data.

    Examples:
        >>> from wildq.filetypes import {ft.FILETYPE_NAME.lower()}_type
        >>> data = {ft.FILETYPE_NAME.lower()}_type.dumper(data_string)
        {ft.FILETYPE_EXAMPLE_DUMPER}
    """

    ft.colorizer.__doc__ = f"""Pass dumped data to {ft.FILETYPE_NAME} colorize.

    Args:
        content (str): string representation of data, usually a dumped data. 

    Returns:
        str: Colorized data.

    Examples:
        >>> from wildq.filetypes import {ft.FILETYPE_NAME.lower()}_type
        >>> data = {ft.FILETYPE_NAME.lower()}_type.colorizer(data_string)
        ...
    """
