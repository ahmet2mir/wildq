#!/bin/bash

echo "Query with old format"
./dist/wildq --hcl examples/hcl.hcl    . | jq .
./dist/wildq --ini examples/ini.ini    . | jq .
./dist/wildq --json examples/json.json . | jq .
./dist/wildq --toml examples/toml.toml . | jq .
./dist/wildq --xml  examples/xml.xml   . | jq .
./dist/wildq --yaml examples/yaml.yaml . | jq .

echo "Query with same in and out"
./dist/wildq -i hcl  examples/hcl.hcl   .
./dist/wildq -i ini  examples/ini.ini   .
./dist/wildq -i json examples/json.json .
./dist/wildq -i toml examples/toml.toml .
./dist/wildq -i xml  examples/xml.xml   .
./dist/wildq -i yaml examples/yaml.yaml .

echo "Query with json out"
./dist/wildq -i hcl  -o json examples/hcl.hcl   .
./dist/wildq -i ini  -o json examples/ini.ini   .
./dist/wildq -i json -o json examples/json.json .
./dist/wildq -i toml -o json examples/toml.toml .
./dist/wildq -i xml  -o json examples/xml.xml   .
./dist/wildq -i yaml -o json examples/yaml.yaml .

echo "Query with yaml out"
./dist/wildq -i hcl  -o yaml examples/hcl.hcl   .
./dist/wildq -i ini  -o yaml examples/ini.ini   .
./dist/wildq -i json -o yaml examples/json.json .
./dist/wildq -i toml -o yaml examples/toml.toml .
./dist/wildq -i xml  -o yaml examples/xml.xml   .
./dist/wildq -i yaml -o yaml examples/yaml.yaml .
