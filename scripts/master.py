import json

class Mapping:
    def __init__(self, field_mapping_file, data_file):
        self.field_mapping_file = field_mapping_file
        self.data_file = data_file
        self.field_mappings_data = {}

    def read_field_mappings(self):
        with open(self.field_mapping_file) as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    key, value = line.strip().split("|")
                    key = key.strip()
                    value = value.strip()
                    self.field_mappings_data[key] = value

    def restructure_data(self):
        self.read_field_mappings()

        with open(self.data_file) as f:
            data = json.load(f)

        restructured_data = {}

        for entry in data['value']:
            mls_number = entry.get(self.field_mappings_data['MLS_NUMBER'])
            if mls_number:
                item = {
                    'PROPERTY': {
                        'ADDRESS': entry.get(self.field_mappings_data['ADDRESS']),
                        'CITY': entry.get(self.field_mappings_data['CITY']),
                        'STATE': entry.get(self.field_mappings_data['STATE']),
                        'ZIP': entry.get(self.field_mappings_data['ZIP']),
                        'COUNTY': entry.get(self.field_mappings_data['COUNTY']),
                        'LOCATION': {
                            'latitude': entry.get(self.field_mappings_data['latitude']),
                            'longitude': entry.get(self.field_mappings_data['longitude'])
                        }
                    },
                    'MEDIA': {
                        'LISTING_URL': entry.get(self.field_mappings_data['LISTING_URL']),
                        'VTOUR_URL': entry.get(self.field_mappings_data['VTOUR_URL']),
                        'MODIF_TIMESTAMP': entry.get(self.field_mappings_data['MODIF_TIMESTAMP'])
                    },
                    'TERABITZ_ID': entry.get(self.field_mappings_data['TERABITZ_ID']),
                    'ID': entry.get(self.field_mappings_data['ID']),
                    'DATASOURCE': entry.get(self.field_mappings_data['DATASOURCE']),
                    'UNIT_NUMBER': entry.get(self.field_mappings_data['UNIT_NUMBER']),
                    'TYPE': entry.get(self.field_mappings_data['TYPE']),
                    'SUBTYPE': entry.get(self.field_mappings_data['SUBTYPE']),
                    'TITLE': entry.get(self.field_mappings_data['TITLE']),
                    'DESCRIPTION': entry.get(self.field_mappings_data['DESCRIPTION']),
                    'PARCEL_NUMBER': entry.get(self.field_mappings_data['PARCEL_NUMBER']),
                    'BEDS': entry.get(self.field_mappings_data['BEDS']),
                    'HALFBATHS': entry.get(self.field_mappings_data['HALFBATHS']),
                    'LOTSQFT': entry.get(self.field_mappings_data['LOTSQFT']),
                    'YEAR_BUILT': entry.get(self.field_mappings_data['YEAR_BUILT']),
                    'DISPLAY_ADDRESS': entry.get(self.field_mappings_data['DISPLAY_ADDRESS']),
                    'DISPLAY_LISTING': entry.get(self.field_mappings_data['DISPLAY_LISTING']),
                    'STATUS': entry.get(self.field_mappings_data['STATUS']),
                    'LISTDATE': entry.get(self.field_mappings_data['LISTDATE']),
                    'ORIG_LISTPRICE': entry.get(self.field_mappings_data['ORIG_LISTPRICE']),
                    'CURR_LISTPRICE': entry.get(self.field_mappings_data['CURR_LISTPRICE']),
                    'PHOTO_COUNT': entry.get(self.field_mappings_data['PHOTO_COUNT']),
                    'PHOTO_MODIF_DATE': entry.get(self.field_mappings_data['PHOTO_MODIF_DATE']),
                    'ELEM_SCHOOL': entry.get(self.field_mappings_data['ELEM_SCHOOL']),
                    'MIDL_SCHOOL': entry.get(self.field_mappings_data['MIDL_SCHOOL']),
                    'HIGH_SCHOOL': entry.get(self.field_mappings_data['HIGH_SCHOOL'])
                }
                restructured_data[mls_number] = item

        # Save the restructured data to a file
        output_file = '/home/karan/python/internship/root/data/out/master1.json'
        with open(output_file, 'w') as f:
            json.dump(restructured_data, f, indent=4)

        print(f"Data has been saved to {output_file}.")


# Create an instance of DataRestructurer and restructure the data
restructurer = DataRestructurer('/home/karan/python/internship/root/mappings/recolorado.properties', '/home/karan/python/internship/root/data/in/data1.json')
restructurer.restructure_data()
