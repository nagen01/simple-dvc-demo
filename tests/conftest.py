import pytest
import os
import yaml
import json

@pytest.fixture
def read_params(config_path="params.yaml"):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

@pytest.fixture
def get_schema(schema_path="schema.json"):
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)
    return schema
