import json

# Read the JSON file
with open('mapfile1.json') as f:
    data = json.load(f)

# Define the field mappings
field_mappings = {
    "TERABITZ_ID": "ListingId",
    "ID": "ListingId",
    "DATASOURCE": "MlsStatus",
    "UNIT_NUMBER": "UnitNumber",
    "ADDRESS": "UnparsedAddress",
    "CITY": "City",
    "STATE": "StateOrProvince",
    "ZIP": "PostalCode",
    "COUNTY": "CountyOrParish",
    "latitude": "Latitude",
    "longitude": "Longitude",
    "TYPE": "PropertyType",
    "SUBTYPE": "PropertySubType",
    "TITLE": None,
    "DESCRIPTION": "LongDescription",
    "PARCEL_NUMBER": "ParcelNumber",
    "BEDS": "BedroomsTotal",
    "BATHS": None,
    "FULLBATHS": None,
    "HALFBATHS": None,
    "AREASQFT": None,
    "LOTSQFT": None,
    "YEAR_BUILT": None,
    "DISPLAY_ADDRESS": None,
    "DISPLAY_LISTING": None,
    "MLS_NUMBER": "ListingKey",
    "STATUS": "MlsStatus",
    "SALEDATE": None,
    "SALEPRICE": None,
    "LISTDATE": None,
    "ORIG_LISTPRICE": "OriginalListPrice",
    "CURR_LISTPRICE": "ListPrice",
    "DAYS_ON_MARKET": None,
    "DATE_PRICE_ADJUST": None,
    "LISTING_URL": None,
    "VTOUR_URL": None,
    "MODIF_TIMESTAMP": "ModificationTimestamp",
    "EXPIRY_DATE": None,
    "MISC": None,
    "PHOTO_COUNT": None,
    "VIDEO_COUNT": None,
    "PHOTO_MODIF_DATE": None,
    "VIDEO_MODIF_DATE": None,
    "DIST_SCHOOL": None,
    "ELEM_SCHOOL": None,
    "MIDL_SCHOOL": None,
    "HIGH_SCHOOL": None,
    "NABRHD_NAME": None,
    "NABRHD_DESC": None,
    "NEARBY_URL": None,
    "IDENTIFIER": None,
    "GEOLEVEL": None,
    "MAIN_PHOTO": None,
    "PRICE_CHANGE": None,
    "STATUS_CHANGE": None,
    "BROKER_CODE": None,
    "BROKER_NAME": None,
    "OFFICE_LISTING_YN": None
}

# Map the values to the fields
mapped_data = {}

for field, mapping in field_mappings.items():
    if mapping is None:
        mapped_data[field] = None
    else:
        mapped_data[field] = [entry.get(mapping) for entry in data['value']]

# Print the mapped data
for key, value in mapped_data.items():
    print(f"{key}: {value}")

# Save the mapped data to a file
output_file = 'master.json'
with open(output_file, 'w') as f:
    json.dump(mapped_data, f, indent=4)

print(f"Data has been saved to {output_file}.")
