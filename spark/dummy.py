import json

# Reading JSON file for field mappings
with open('field_mapping.json') as f:
    field_mappings_data = json.load(f)

# Read the JSON file
with open('mapfile2.json') as f:
    data = json.load(f)

#structure the data
restructured_data = []

for entry in data['value']:
    item = {
        'MLS_NUMBER': entry.get(field_mappings_data['MLS_NUMBER']),
        'PROPERTY': {
            'ADDRESS': entry.get(field_mappings_data['ADDRESS']),
            'CITY': entry.get(field_mappings_data['CITY']),
            'STATE': entry.get(field_mappings_data['STATE']),
            'ZIP': entry.get(field_mappings_data['ZIP']),
            'COUNTY': entry.get(field_mappings_data['COUNTY']),
            'LOCATION': {
                'latitude': entry.get(field_mappings_data['latitude']),
                'longitude': entry.get(field_mappings_data['longitude'])
            }
        },
        'MEDIA': {
            'LISTING_URL': entry.get(field_mappings_data['LISTING_URL']),
            'VTOUR_URL': entry.get(field_mappings_data['VTOUR_URL']),
            'MODIF_TIMESTAMP': entry.get(field_mappings_data['MODIF_TIMESTAMP'])
        },
        'TERABITZ_ID': entry.get(field_mappings_data['TERABITZ_ID']),
        'ID': entry.get(field_mappings_data['ID']),
        'DATASOURCE': entry.get(field_mappings_data['DATASOURCE']),
        'UNIT_NUMBER': entry.get(field_mappings_data['UNIT_NUMBER']),
        'TYPE': entry.get(field_mappings_data['TYPE']),
        'SUBTYPE': entry.get(field_mappings_data['SUBTYPE']),
        'TITLE': entry.get(field_mappings_data['TITLE']),
        'DESCRIPTION': entry.get(field_mappings_data['DESCRIPTION']),
        'PARCEL_NUMBER': entry.get(field_mappings_data['PARCEL_NUMBER']),
        'BEDS': entry.get(field_mappings_data['BEDS']),
        'HALFBATHS': entry.get(field_mappings_data['HALFBATHS']),
        'LOTSQFT': entry.get(field_mappings_data['LOTSQFT']),
        'YEAR_BUILT': entry.get(field_mappings_data['YEAR_BUILT']),
        'DISPLAY_ADDRESS': entry.get(field_mappings_data['DISPLAY_ADDRESS']),
        'DISPLAY_LISTING': entry.get(field_mappings_data['DISPLAY_LISTING']),
        'STATUS': entry.get(field_mappings_data['STATUS']),
        'LISTDATE': entry.get(field_mappings_data['LISTDATE']),
        'ORIG_LISTPRICE': entry.get(field_mappings_data['ORIG_LISTPRICE']),
        'CURR_LISTPRICE': entry.get(field_mappings_data['CURR_LISTPRICE']),
        'PHOTO_COUNT': entry.get(field_mappings_data['PHOTO_COUNT']),
        'PHOTO_MODIF_DATE': entry.get(field_mappings_data['PHOTO_MODIF_DATE']),
        'ELEM_SCHOOL': entry.get(field_mappings_data['ELEM_SCHOOL']),
        'MIDL_SCHOOL': entry.get(field_mappings_data['MIDL_SCHOOL']),
        'HIGH_SCHOOL': entry.get(field_mappings_data['HIGH_SCHOOL'])
    }
    restructured_data.append(item)

# Print the restructured data
for item in restructured_data:
    print(json.dumps(item, indent=4))

# Save the restructured data to a file
output_file = 'master.json'
with open(output_file, 'w') as f:
    json.dump(restructured_data, f, indent=4)

print(f"Data has been saved to {output_file}.")
