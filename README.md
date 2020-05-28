# wildq - Command-line TOML/JSON/INI/YAML/XML/HCL processor using jq c bindings

![GitHub](https://img.shields.io/github/license/ahmet2mir/wildq.svg)
[![image](https://img.shields.io/pypi/pyversions/wildq.svg)](https://python.org/pypi/wildq)
[![Build Status](https://travis-ci.org/ahmet2mir/wildq.svg?branch=master)](https://travis-ci.org/ahmet2mir/wildq)

Purpose of this package is to provide a simple wrapper arround jq for different formats.
I'm tired of searching a package doing yaml jq, toml jq, ini jq etc. mainly used for scripting.

This script uses:

* @mwilliamson [Python bindings](https://github.com/mwilliamson/jq.py) on top of @stedolan famous [jq](https://github.com/stedolan/jq/) lib
* @martinblech [xmldict](https://github.com/martinblech/xmltodict) to manage XML
* @uiri [toml](https://github.com/uiri/toml) to manage TOML
* @yaml [pyyaml](https://github.com/yaml/pyyaml) to manage YAML
* @virtuald [pyhcl](https://github.com/virtuald/pyhcl) to manage HCL
* for INI [ConfigParser](https://docs.python.org/3/library/configparser.html) is used.

# Installation

```sh
pip install wildq
```

# Usage

```
wildq [--yaml|--json|--toml|--ini|--xml|--hcl> <jq filter> [file]
```

There is also a shorter command `wq` comming with the package.

Output is similar to `jq -MCr` (no color, no compact and no quote on single value)

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
cat examples/json.json | wildq --json ".keys[]"
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
wildq --json ".keys[]" examples/json.json
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
wq --json ".keys[]" examples/json.json
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
cat examples/toml.toml | wildq --toml ".keys[]"
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
cat examples/ini.ini | wildq --ini ".keys"
{
    "key1": "value1",
    "key2": "value2"
}
```

For XML
```sh
cat examples/xml.xml | wildq --xml "."
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
cat examples/yaml.yaml  | wildq --yaml ".keys[]"
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
cat examples/hcl.hcl  | wildq --hcl ".keys[]"
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
wildq --toml "keys[]" examples/toml.toml | while read -r key 
do
    echo "Getting key ${key}"
done
```

## TODO

- [ ] support all jq types
- [ ] add tests...
- [ ] add more control over filters and files
- [ ] detect automagically filetype
- [ ] use click for the CLI

## Contributing

Merge requests are welcome :)


## License

Licensed under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
