import os
import json
import pandas as pd
import argparse
from get_data import read_params

def generate_schema_file(config_path):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    data_schema_path = config["data_schema"]["schema_path"]
    df = pd.read_csv(raw_data_path, sep=",")
    _range = df.describe().loc[["min", "max"], :].to_json(orient="columns")
    parsed = json.loads(_range)
    #print(parsed)
    with open(data_schema_path, "w") as jf:
        json.dump(parsed, jf)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    generate_schema_file(parsed_args.config)