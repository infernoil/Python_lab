#Task 1: JSON Parsing and Data Retrieval
#Objective: Parse a JSON file and return a list of names of individuals above a certain age.
import json
def task1(filee,age):
    with open(filee) as filee:
        data= json.load(filee)
        return[entry['name'] for entry in data if entry['age'] > age]


#Task 2: Data Transformation and JSON Serialization
#Objective: Transform a list of dictionaries into a JSON string and write it to a file.
def task2(data,feli):
    with open(feli,'w') as feli:
        json.dump(data,feli)


#Task 3: JSON Schema Validation
#Objective: Validate JSON files against a given schema.
def task3(sch, fale):
    invalid_files = []
    for file_path in fale:
        try:
            with open(file_path) as file:
                json.load(file)
        except json.JSONDecodeError:
            invalid_files.append(file_path)
    return invalid_files




#Task 4: Nested JSON Data Handling
#Objective: Extract specific information from a complex nested JSON structure.
import json

def task4(filei, keys):
    def extract_values(obj, keys):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == keys:
                    yield v
                elif isinstance(v, (dict, list)):
                    yield from extract_values(v, keys)
        elif isinstance(obj, list):
            for item in obj:
                yield from extract_values(item, keys)

    with open(filei) as file:
        data = json.load(file)
    return list(extract_values(data, keys))

#Task 5: Updating JSON Data
#Objective: Update certain fields in a JSON file based on given criteria.

import json

def task5(filee, category, updatef):
    with open(filee, 'r+') as file:
        data = json.load(file)
        [updatef(item) for item in data if item.get('category') == category]
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    def increase_price(item):
        item['price'] += 10

