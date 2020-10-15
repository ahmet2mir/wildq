# wildq - Command-line TOML/JSON/INI/YAML/XML/HCL processor using jq c bindings

![GitHub](https://img.shields.io/github/license/ahmet2mir/wildq.svg)
[![image](https://img.shields.io/pypi/pyversions/wildq.svg)](https://python.org/pypi/wildq)
[![Build Status](https://travis-ci.org/ahmet2mir/wildq.svg?branch=master)](https://travis-ci.org/ahmet2mir/wildq)

Purpose of this package is to provide a simple wrapper arround jq for different formats.
I'm tired of searching a package doing yaml jq, toml jq, ini jq etc. mainly used for scripting.

This script uses:
* @mwilliamson [Python bindings](https://github.com/mwilliamson/jq.py) on top of @stedolan famous [jq](https://github.com/stedolan/jq/) lib
* swiss knife for coloration [pygments](https://github.com/pygments/pygments)
* binary built with [pyinstaller](https://github.com/pyinstaller/pyinstaller)
* easy CLI with [click](https://github.com/pallets/click)
* for supported types sources, check table `Supported file types`

# Installation

## Pip

```sh
pip install wildq
```

A binary is also available for different platform, pick one (both of `wildq` and `wq` will be in the archive)

## MacOS

```
brew install ahmet2mir/tap/wildq
brew install ahmet2mir/tap/wq
```

## Debian (no gpg signature)

```
wget https://github.com/ahmet2mir/wildq/releases/download/v1.1.4/wildq_1.1.4-1_amd64.deb
dpkg -i wildq_1.1.4-1_amd64.deb
```

## Windows

Wildq use [jq.py](https://github.com/mwilliamson/jq.py) and it's not yet available on windows platforms.
I tried to compile it without windows machine and I failed, and I don't had the time to try to understand how Windows / C binding / Python works.
If anybody would contribute, there is an [open issue](https://github.com/mwilliamson/jq.py/issues/20) (jq and onigurama are 'compilable' on Windows so I think that someone confortable with that OS could make it);


# Supported file types

| type | color | ordering | output | source                                                              |
|------|-------|----------|--------|---------------------------------------------------------------------|
| hcl  |  json |    no    |  json  | [pyhcl](https://github.com/virtuald/pyhcl) by @virtuald             |
| ini  |  yes  |    no    |  yes   | [ConfigParser](https://docs.python.org/3/library/configparser.html) |
| json |  yes  |    yes   |  yes   | [json](https://docs.python.org/3/library/json.html)                 |
| toml |  yes  |    no    |  yes   | [toml](https://github.com/uiri/toml) by @uiri                       |
| xml  |  yes  |    no    |  yes   | [xmldict](https://github.com/martinblech/xmltodict) by @martinblech |
| yaml |  yes  |    yes   |  yes   | [pyyaml](https://github.com/yaml/pyyaml)                            |

# Usage

```
$ wildq -i help
Usage: wildq [OPTIONS] JQ_FILTER [FILE]

Options:
  -c, --compact-output            compact instead of pretty-printed output
  -r, --raw                       output raw strings, not content texts
  -C, --color-output              colorize content (default), mutally
                                  exclusive with --monochrome-output

  -M, --monochrome-output         monochrome (don't colorize content), mutally
                                  exclusive with --color-output

  --hcl                           Combine --input hcl --output json, mutally
                                  exclusive with other Combined options

  --ini                           Combine --input ini --output json, mutally
                                  exclusive with other Combined options

  --json                          Combine --input json --output json, mutally
                                  exclusive with other Combined options

  --toml                          Combine --input toml --output json, mutally
                                  exclusive with other Combined options

  --xml                           Combine --input xml --output json, mutally
                                  exclusive with other Combined options

  --yaml                          Combine --input yaml --output json, mutally
                                  exclusive with other Combined options

  -i, --input [hcl|ini|json|toml|xml|yaml]
                                  Define the content type of file, mutally
                                  exclusive with Combined option

  -o, --output [hcl|ini|json|toml|xml|yaml]
                                  Define the content type of printed output,
                                  mutally exclusive with Combined option
                                  (default input format)

  --help                          Show this message and exit.
```

For backward compatibility in previous version only `--[yaml|json|toml|ini|xml|hcl]` was possible with default to json output.
We still keep Monochrome, raw and json output with thoses options.
Output was similar to `jq -MCr` (no color, no compact and no quote on single value)

But now, by default it's colorized, not raw and if you specify input using `-i` or `--input` output will be the same format.

There is also a shorter command `wq` comming with the package.

Like `jq cli`, wildq supports both of stdin and file to the function

See examples to get some example.

Content of `examples/json.json`

```
{
    "general": {
        "user": "admin"
    },
    "keys": [
        {"key": "value1"},
        {"key": "value2"},
        "alone"
    ]
}
```

```sh
cat examples/json.json | wildq -i json ".keys[]"
{
    "key": "value1"
}
{
    "key": "value2"
}
alone
```

or

```sh
wildq -i json ".keys[]" examples/json.json
{
    "key": "value1"
}
{
    "key": "value2"
}
alone
```
or

```sh
wq -i json ".keys[]" examples/json.json
{
    "key": "value1"
}
{
    "key": "value2"
}
alone
```

For TOML
```sh
cat examples/toml.toml | wildq -i toml ".keys[]"
{
    "key": "value1"
}
{
    "key": "value2"
}
alone
```

For INI (no array)
```sh
cat examples/ini.ini | wildq -i ini ".keys"
{
    "key1": "value1",
    "key2": "value2"
}
```

For XML
```sh
cat examples/xml.xml | wildq -i xml "."
{
    "root": {
        "general": {
            "user": "admin"
        },
        "keys": {
            "element": [
                {
                    "key": "value1"
                },
                {
                    "key": "value2"
                },
                "alone"
            ]
        }
    }
}
```

For YAML
```sh
cat examples/yaml.yaml  | wildq -i yaml ".keys[]"
{
    "key1": "value1"
}
{
    "key2": "value2"
}
alone
```

For HCL
```sh
cat examples/hcl.hcl  | wildq -i hcl ".keys[]"
{
    "key": "value1"
}
{
    "key": "value2"
}
```

## Tips and tricks

Loop on keys in bash without creating a subshell

```sh
wildq -i toml "keys[]" examples/toml.toml | while read -r key 
do
    echo "Getting key ${key}"
done
```

## TODO

- [x] add tests...
- [x] add more control over filters and files
- [x] use click for the CLI
- [x] support different output
- [ ] detect automagically filetype
- [ ] support all jq types
- [ ] ordering

## Contributing

Merge requests are welcome :)


## License

Licensed under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).


## Repository URL

https://github.com/ahmet2mir/wildq
