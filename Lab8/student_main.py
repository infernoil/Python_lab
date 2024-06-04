import json
import os

def task1(filee, age):
    with open(filee) as filee:
        data = json.load(filee)
        return [entry['name'] for entry in data if entry['age'] > age]
names_above_age = task1('data/input.json', 30)
print(names_above_age)
import json

def task2(data, feli):
    with open(feli, 'w') as feli:
        json.dump(data, feli)
data_to_serialize = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
task2(data_to_serialize, 'data/transformed_output.json')
import json

def task3(sch, fale):
    invalid_files = []
    for file_path in fale:
        try:
            with open(file_path) as file:
                json.load(file)
        except json.JSONDecodeError:
            invalid_files.append(file_path)
    return invalid_files
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}
files_to_validate = ['data/input.json', 'data/transformed_output.json']
invalid_files = task3(schema, files_to_validate)
print(invalid_files)
names_above_age = task1('data/input.json', 30)
print(names_above_age)
data_to_serialize = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
task2(data_to_serialize, 'data/transformed_output.json')
import json

def task3(sch, fale):
    invalid_files = []
    for file_path in fale:
        try:
            with open(file_path) as file:
                json.load(file)
        except json.JSONDecodeError:
            invalid_files.append(file_path)
    return invalid_files
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}
files_to_validate = ['data/input.json', 'data/transformed_output.json']
invalid_files = task3(schema, files_to_validate)
print(invalid_files)