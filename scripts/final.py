import  json
class Mapping:
    def __init__(self, field_mapping_flags, data_file):
        self.field_mapping_flags = field_mapping_flags
        self.data_file = data_file

    def restructure_data(self):
        with open(self.data_file) as f:
            data = json.load(f)

        restructured_data = {}

        for entry in data['value']:
            mls_number = entry.get(self.field_mapping_flags['MLS_NUMBER']['value'])
            if mls_number:
                item = {}
                property_section = {}
                media_section = {}
                features_section = {}
                misc_section = {}  # Add a new section for MISC

                for key, field_mapping in self.field_mapping_flags.items():
                    field_value = entry.get(field_mapping['value'])
                    if field_mapping['flag'] == 'P':
                        property_section[key] = field_value if field_value is not None else None
                    elif field_mapping['flag'] == 'M':
                        media_section[key] = field_value if field_value is not None else None
                    elif field_mapping['flag'] == 'F':
                        features_section[key] = field_value if field_value is not None else None
                    elif field_mapping['flag'] == 'P' and key == 'MISC':  # Handle MISC field separately
                        misc_section.update({k.strip(): v.strip() for k, v in (pair.split(':') for pair in field_value.split(','))})
                    else:
                        item[key] = field_value if field_value is not None else None

                if property_section:
                    item['PROPERTY'] = property_section

                if media_section:
                    item['MEDIA'] = media_section

                if features_section:
                    item['FEATURES'] = features_section

                if misc_section:
                    item['MISC'] = misc_section  # Assign the extracted values to MISC field

                restructured_data[mls_number] = item

        return restructured_data
