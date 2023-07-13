import sys
import json
from data_restructurer import Mapping

# Get the command-line argument for the desired data source
if len(sys.argv) < 2:
    print("Please provide the desired data source as a command-line argument.")
    sys.exit(1)

desired_datasource = sys.argv[1]

# Create an instance of Mapping and restructure the data
restructurer = Mapping('field_mapping.txt', 'mapfile2.json')
restructured_data = restructurer.restructure_data()

# Filter the restructured_data based on the desired_datasource
filtered_data = {
    mls_number: item
    for mls_number, item in restructured_data.items()
    if item.get('DATASOURCE') == desired_datasource
}

# Save the filtered data to a JSON file
output_file = 'mlsnumber.json'
with open(output_file, 'w') as f:
    json.dump(filtered_data, f, indent=4)

print(f"Data with DATASOURCE '{desired_datasource}' has been saved to {output_file}.")
