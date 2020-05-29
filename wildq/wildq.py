# coding: utf-8
import io
import os
import sys
import json
import configparser

# third parties
import jq
import hcl
import yaml
import toml
import xmltodict


def usage():
    print("wildq <--yaml|--json|--toml|--ini|--xml|--hcl> <jq filter> [file]")
    return 0


def ini_load_string(string):
    config = configparser.ConfigParser()
    config.read_string(string)
    return config._sections


def run(filetype, jq_filter, content):

    filetypes = {
        "--yaml": yaml.safe_load,
        "--json": json.loads,
        "--toml": toml.loads,
        "--ini": ini_load_string,
        "--xml": xmltodict.parse,
        "--hcl": hcl.loads,
    }

    data = filetypes[filetype](content)

    for item in jq.compile(jq_filter).input(data):
        print(json.dumps(item, indent=4, sort_keys=True).strip('"'))


def cli(args):
    if len(args) < 3:
        usage()
        return 1

    if args[1] not in ["--yaml", "--json", "--toml", "--ini", "--xml", "--hcl"]:
        print("Bad format " + args[1])
        usage()
        return 2

    file = sys.stdin
    if len(sys.argv) >= 4:
        if not os.path.exists(sys.argv[3]):
            print("Unable to open file " + sys.argv[3])
            return 1
        file = sys.argv[3]

    if isinstance(file, io.TextIOWrapper):
        content = file.read()
    else:
        with open(file, "r") as fd:
            content = fd.read()

    # skip silently if content is empty
    if not content:
        return 0

    return run(sys.argv[1], sys.argv[2], content)


def main():
    sys.exit(cli(sys.argv))


if __name__ == "__main__":
    main()
