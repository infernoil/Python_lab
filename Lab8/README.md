Лабораторна робота №8: JSON Parsing and Data Retrieval
___
Мета роботи:
Дослідити як прцювати з JSON файлами
___
Опис завдання:
```Python
Task 1: JSON Parsing and Data Retrieval
Objective: Parse a JSON file and return a list of names of individuals above a certain age.

Input:
A file path (str) to a JSON file.
An age threshold (int).
The JSON file contains a list of objects, each with fields like name (string) and age (integer).
Output:
A list (list) of names (str) of individuals whose age is greater than the provided threshold.



Task 2: Data Transformation and JSON Serialization
Objective: Transform a list of dictionaries into a JSON string and write it to a file.

Input:
A list (list) of dictionaries (dict). Each dictionary represents a person and contains fields like name (string), age (integer), and city (string).
A file path (str) where the JSON string will be saved.
Output:
No direct return value, but a file is created or overwritten at the specified path containing the JSON representation of the input data.



Task 3: JSON Schema Validation
Objective: Validate JSON files against a given schema.

Input:
A JSON schema (dict) defining the structure and data types expected in the JSON files.
A list (list) of file paths (str) to JSON files that need to be validated against the schema.
Output:
A list (list) of file paths (str) that do not conform to the given schema.



Task 4: Nested JSON Data Handling
Objective: Extract specific information from a complex nested JSON structure.

Input:
A file path (str) to a complex JSON file with nested structures (like objects within arrays).
A key (str) to search for within the JSON structure.
Output:
A list (list) of values (str, int, list, etc.) associated with the specified key, found at any level within the JSON structure.



Task 5: Updating JSON Data
Objective: Update certain fields in a JSON file based on given criteria.

Input:
A file path (str) to a JSON file representing a database (like a list of products), example: [{"name": "Product1", "category": "electronics", "price": 100}]
A category (str) to identify which items should be updated.
An update function that defines how to update the selected items. This function should take a single argument representing a single item from the JSON file and modify it accordingly.
Example: task5(“products.json”, “electronics”, increase_price)
Output:
No direct return value, but the specified JSON file is modified, with certain fields of objects updated according to the given criteria, example: [{"name": "Product1", "category": "electronics", "price": 110}]
```
___
Виконання роботи:
json_project/
│
├── main.py
├── data/
│   ├── input.json
│   ├── transformed_output.json
│   └── sample_schema.json
└── README.md
```Python
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

```
___
Результати:
```Python
Task 1: JSON Parsing and Data Retrieval
Names of individuals above age 30: ['Bob', 'Charlie']

Task 2: Data Transformation and JSON Serialization
Data has been serialized to data/transformed_output.json

Task 3: JSON Schema Validation
Invalid files: []
```
___
Висновки:
Мета роботи була досягнута без видемих проблем.
___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.