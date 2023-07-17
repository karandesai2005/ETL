import sys
import json
import os
from final import Mapping

# Get the command-line argument for the desired data source
if len(sys.argv) < 2:
    print("Please provide the desired data source as a command-line argument.")
    sys.exit(1)

desired_datasource = sys.argv[1]

# Read the file containing the mappings of data file from the connections folder
mapping_file = f"/home/karan/python/internship/root/connections/{desired_datasource}.connections"

if not os.path.exists(mapping_file):
    print(f"Mapping file '{mapping_file}' not found. Please create the file and provide valid mappings.")
    sys.exit(1)

try:
    with open(mapping_file, 'r') as f:
        file_mapping = json.load(f)
except json.JSONDecodeError:
    print(f"Invalid JSON format in mapping file '{mapping_file}'. Please provide valid JSON.")
    sys.exit(1)

# Get the file path for the desired data source from the mapping file
data_file = file_mapping.get(desired_datasource)

if data_file is None or not os.path.exists(data_file):
    print(f"No mapping found for '{desired_datasource}'. Please provide a valid data source.")
    sys.exit(1)

# Read the field mapping flags from the properties file
properties_file = f"/home/karan/python/internship/root/mappings/{desired_datasource}.properties"
field_mapping_flags = {}
with open(properties_file, 'r') as f:
    for line in f:
        if line.strip():
            key, value, flag = line.strip().split("|")
            key = key.strip()
            value = value.strip()
            flag = flag.strip()
            field_mapping_flags[key] = {'value': value, 'flag': flag}

# Create an instance of Mapping and restructure the data
restructurer = Mapping(field_mapping_flags, data_file)
restructured_data = restructurer.restructure_data()

# Filter the restructured_data based on the desired_datasource
filtered_data = {
    mls_number: item
    for mls_number, item in restructured_data.items()
   # if item.get('DATASOURCE', "").lower() == desired_datasource.lower()
    if item['PROPERTY'].get('DATASOURCE', "").lower() == desired_datasource.lower()

}


# Save the filtered data to a JSON file
output_file = f"/home/karan/python/internship/root/data/out/{desired_datasource}.json"
with open(output_file, 'w') as f:
    json.dump(filtered_data, f, indent=4)

print(f"Data with DATASOURCE '{desired_datasource}' has been saved to {output_file}.")

# Add print statements for debugging
#print(f"filtered_data: {filtered_data}")
#print(f"output_file path: {output_file}")
