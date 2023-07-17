import json

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

                for key, field_mapping in self.field_mapping_flags.items():
                    field_value = entry.get(field_mapping['value'])
                    if field_mapping['flag'] == 'P':
                        if key == 'MISC' and field_value is not None:  # Handle MISC field within PROPERTY section
                            misc_keys = [k.strip() for k in field_value.split(',')]
                            misc_values = [entry.get(k.strip()) for k in misc_keys]
                            print(misc_values)
                            property_section[key] = '|'.join([f"{k}:{v}" for k, v in zip(misc_keys, misc_values) if v is not None])
                            print(property_section)
                        else:
                            property_section[key] = field_value if field_value is not None else None
                    elif field_mapping['flag'] == 'M':
                        media_section[key] = field_value if field_value is not None else None
                    elif field_mapping['flag'] == 'F':
                        features_section[key] = field_value if field_value is not None else None

                if property_section:
                    item['PROPERTY'] = property_section

                if media_section:
                    item['MEDIA'] = media_section

                if features_section:
                    item['FEATURES'] = features_section

                restructured_data[mls_number] = item

        return restructured_data
