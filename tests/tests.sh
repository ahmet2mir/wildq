#!/bin/bash

echo "Query with old format"
./artifacts/binaries/wildq --hcl examples/hcl.hcl    . | jq .
./artifacts/binaries/wildq --ini examples/ini.ini    . | jq .
./artifacts/binaries/wildq --json examples/json.json . | jq .
./artifacts/binaries/wildq --toml examples/toml.toml . | jq .
./artifacts/binaries/wildq --xml  examples/xml.xml   . | jq .
./artifacts/binaries/wildq --yaml examples/yaml.yaml . | jq .

echo "Query with same in and out"
./artifacts/binaries/wildq -i hcl  examples/hcl.hcl   .
./artifacts/binaries/wildq -i ini  examples/ini.ini   .
./artifacts/binaries/wildq -i json examples/json.json .
./artifacts/binaries/wildq -i toml examples/toml.toml .
./artifacts/binaries/wildq -i xml  examples/xml.xml   .
./artifacts/binaries/wildq -i yaml examples/yaml.yaml .

echo "Query with json out"
./artifacts/binaries/wildq -i hcl  -o json examples/hcl.hcl   .
./artifacts/binaries/wildq -i ini  -o json examples/ini.ini   .
./artifacts/binaries/wildq -i json -o json examples/json.json .
./artifacts/binaries/wildq -i toml -o json examples/toml.toml .
./artifacts/binaries/wildq -i xml  -o json examples/xml.xml   .
./artifacts/binaries/wildq -i yaml -o json examples/yaml.yaml .

echo "Query with yaml out"
./artifacts/binaries/wildq -i hcl  -o yaml examples/hcl.hcl   .
./artifacts/binaries/wildq -i ini  -o yaml examples/ini.ini   .
./artifacts/binaries/wildq -i json -o yaml examples/json.json .
./artifacts/binaries/wildq -i toml -o yaml examples/toml.toml .
./artifacts/binaries/wildq -i xml  -o yaml examples/xml.xml   .
./artifacts/binaries/wildq -i yaml -o yaml examples/yaml.yaml .
