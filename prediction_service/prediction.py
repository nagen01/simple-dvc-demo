import yaml
import json
import numpy as np
import joblib
import os

params_path = "params.yaml"
schema_path = os.path.join("prediction_service","schema.json")

class NotInRange(Exception):
    def __init__(self, message="Entered values are not in range"):
        self.message = message
        super().__init__(self.message)

class NotInCols(Exception):
    def __init__(self, message="Not in columns"):
        self.message = message
        super().__init__(self.message)


def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    print(type(model))
    prediction = model.predict(data)[0]
    #prediction = model.predict(data).to_list()[0]
    print(prediction)

    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"

def get_schema(schema_path=schema_path):
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)
    return schema

def validate_input(dict_request):
    schema = get_schema()
    #print(schema)
    def _validate_cols(col):
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols

    def _validate_values(col, val):
        if not schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]:
            raise NotInRange

    #print(dict_request)
    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col, val)

    return True

def form_response(dict_request):
    if validate_input(dict_request):
        data = dict_request.values()
        data = [list(map(float, data))]
        #print(data)
        response = predict(data)
        #print(response)
        return response

def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = predict(data)
            response = {"response": response}
            return response
    except NotInRange as e:
        response = {"The expected range": get_schema(), "response":str(e)}
        return response

    except NotInCols as e:
        response = {"The expected columns": get_schema().keys(), "response":str(e)}
        return response

    except Exception as e:
        response = {"response":str(e)}
        return response