import json

# Reading JSON file for field mappings
with open('field_mapping.json') as f:
    field_mappings_data = json.load(f)

# Read the JSON file
with open('mapfile1.json') as f:
    data = json.load(f)

# Restructure the data
restructured_data = []

for entry in data['value']:
    item = {}
    for field, mapping in field_mappings_data.items():
        if mapping is not None:
            item[field] = entry.get(mapping)
    restructured_data.append(item)

# Print the restructured data
for item in restructured_data:
    print(json.dumps(item, indent=4))

# Save the restructured data to a file
output_file = 'master.json'
with open(output_file, 'w') as f:
    json.dump(restructured_data, f, indent=4)

print(f"Data has been saved to {output_file}.")
