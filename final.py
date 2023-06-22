import json

# Load the field mapping from field_mapping.json
with open('field_mapping.json') as file:
    field_mapping = json.load(file)

with open('mapfile1.json') as file:
    map_data = json.load(file)

print("Original map_data:")
print(json.dumps(map_data, indent=4))

master_json = {}

for key, value in field_mapping.items():
    if '.' in value:
        nested_keys = value.split('.')
        temp_data = map_data['value']
        for nested_key in nested_keys:
            if nested_key in temp_data:
                temp_data = temp_data[nested_key]
            else:
                temp_data = None
                break
        master_json[key] = temp_data
    elif value in map_data['value'][0]:
        master_json[key] = map_data['value'][0][value]
    else:
        master_json[key] = None

print("Master JSON:")
print(json.dumps(master_json, indent=4))

# Save the master JSON to a file
with open('master.json', 'w') as file:
    json.dump(master_json, file, indent=4)
