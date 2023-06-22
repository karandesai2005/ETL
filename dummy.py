import json

# Load the field mapping from field_mapping.json
with open('field_mapping.json') as file:
    field_mapping = json.load(file)

with open('mapfile1.json') as file:
    map_data = json.load(file)

print("Original map_data:")
print(json.dumps(map_data, indent=4))

master_json = {}

def process_data(data):
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return {k: process_data(v) for k, v in data.items()}
    else:
        return [data]

for key, value in field_mapping.items():
    if '.' in value:
        nested_keys = value.split('.')
        temp_data = map_data
        for nested_key in nested_keys:
            if nested_key in temp_data:
                temp_data = temp_data[nested_key]
            else:
                temp_data = None
                break
        master_json[key] = process_data(temp_data)
    elif isinstance(map_data, list) and value in map_data[0]:
        master
