# standard
import sys

# third
import jq
import click

# local
import wildq.filetypes
from wildq._wildq_version import __version__


class Config:
    pass


# could be replaced by importlib / getattr but explicit is better than implicit
SUPPORTED_FILETYPES = {
    "hcl": wildq.filetypes.hcl_type,
    "ini": wildq.filetypes.ini_type,
    "json": wildq.filetypes.json_type,
    "toml": wildq.filetypes.toml_type,
    "xml": wildq.filetypes.xml_type,
    "yaml": wildq.filetypes.yaml_type,
}

PASS_CONFIG = click.make_pass_decorator(Config, ensure=True)


def compiler(jq_filter, data):
    return jq.compile(jq_filter).input(data)


@click.command()
# @click.option('--input', help='compose file to work with', type=click.File('r'), default=sys.stdin)
# @click.option('--output', help='compose file to work with', type=click.File('r'), default=sys.stdin)
@click.option(
    "-c",
    "--compact-output",
    is_flag=True,
    default=False,
    help="compact instead of pretty-printed output",
)
@click.option(
    "-r",
    "--raw",
    is_flag=True,
    default=False,
    help="output raw strings, not content texts",
)
@click.option(
    "-C",
    "--color-output",
    is_flag=True,
    default=False,
    help="colorize content (default), mutally exclusive with --monochrome-output",
)
@click.option(
    "-M",
    "--monochrome-output",
    is_flag=True,
    default=False,
    help="monochrome (don't colorize content), mutally exclusive with --color-output",
)
# @click.option('-S', '--sort', is_flag=True, default=False, help="sort keys of objects on output")
@click.option(
    "--hcl",
    is_flag=True,
    default=False,
    help="Combine --input hcl --output hcl, mutally exclusive with other Combined options",
)
@click.option(
    "--ini",
    is_flag=True,
    default=False,
    help="Combine --input ini --output ini, mutally exclusive with other Combined options",
)
@click.option(
    "--json",
    is_flag=True,
    default=False,
    help="Combine --input json --output json, mutally exclusive with other Combined options",
)
@click.option(
    "--toml",
    is_flag=True,
    default=False,
    help="Combine --input toml --output toml, mutally exclusive with other Combined options",
)
@click.option(
    "--xml",
    is_flag=True,
    default=False,
    help="Combine --input xml --output xml, mutally exclusive with other Combined options",
)
@click.option(
    "--yaml",
    is_flag=True,
    default=False,
    help="Combine --input yaml --output yaml, mutally exclusive with other Combined options",
)
@click.option(
    "-i",
    "--input",
    type=click.Choice(list(SUPPORTED_FILETYPES.keys())),
    help="Define the content type of file, mutally exclusive with Combined option",
)
@click.option(
    "-o",
    "--output",
    type=click.Choice(list(SUPPORTED_FILETYPES.keys())),
    default=None,
    show_default=False,
    help="Define the content type of printed output, mutally exclusive with Combined option (default input format)",
)
@click.argument("jq_filter")
@click.argument("file", type=click.File("r"), default=sys.stdin)
@click.version_option(version=__version__)
def cli(*args, **kwargs):
    from pprint import pprint

    if (kwargs["input"] or kwargs["output"]) and any(
        [True for x in list(SUPPORTED_FILETYPES.keys()) if kwargs[x]]
    ):
        print(
            "When using combined option you can't use --input or --output, please use them explictly"
        )
        sys.exit(1)

    if kwargs["color_output"] and kwargs["monochrome_output"]:
        print(
            "--color-output and --monochrome-output are mutally exclusive, select one"
        )
        sys.exit(1)

    colorized = False
    if not kwargs["color_output"] and not kwargs["monochrome_output"]:
        colorized = True

    if kwargs["color_output"]:
        colorized = True

    if kwargs["monochrome_output"]:
        colorized = False

    input_fmt = None
    output_fmt = None

    raw = kwargs["raw"]

    # backward compatibility, if a type is specified without -i, output to json
    # enforce colorize to false and raw to true like first release of wq
    for spt in list(SUPPORTED_FILETYPES.keys()):
        if kwargs[spt]:
            input_fmt = spt
            output_fmt = "json"
            colorized = False
            raw = True

    # user specified input otherwise raise
    if not input_fmt:
        input_fmt = kwargs["input"]

    # if user specify input but not output, use default input format
    if not output_fmt:
        if kwargs.get("output") is None:
            output_fmt = input_fmt
        else:
            output_fmt = kwargs["output"]

    if not input_fmt or not output_fmt:
        if input_fmt is None:
            print("input option is empty")
        if output_fmt is None:
            print("output option is empty")
        print(
            "Issue when resolving input and output, getting confiuration %s",
            str(kwargs),
        )
        sys.exit(1)

    module_in = SUPPORTED_FILETYPES[input_fmt]
    module_out = SUPPORTED_FILETYPES[output_fmt]

    content = module_in.loader(kwargs["file"].read())

    # skip silently if content is empty
    if not content:
        return 0

    compiled = compiler(kwargs["jq_filter"], content)

    for line in compiled:
        if not isinstance(line, dict) and not isinstance(line, list):
            if raw:
                print(line.strip('"'))
            else:
                print(line)
            continue

        dumped = module_out.dumper(line)

        if colorized:
            print(module_out.colorizer(dumped))
        else:
            print(dumped)
