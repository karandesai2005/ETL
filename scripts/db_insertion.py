import json
import psycopg2

# PostgreSQL connection parameters
db_params = {
    "host": "localhost",
    "database": "recolorado_reso",
    "user": "postgres",
    "password": "karanishu",
}

def insert_property_data(data):
    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                insert_sql = """
                    INSERT INTO property_ptnf (
                        mls_number, datasource, unit_number, address, city, state, zip, county, latitude, longitude, subtype
                    )
                    VALUES (
                        %(MLS_NUMBER)s, %(DATASOURCE)s, %(UNIT_NUMBER)s, %(ADDRESS)s, %(CITY)s, %(STATE)s, %(ZIP)s, 
                        %(COUNTY)s, %(latitude)s, %(longitude)s, %(SUBTYPE)s
                    )
                """ 
                cur.executemany(insert_sql, data)
                conn.commit()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

if __name__ == "__main__":
    # Load data from recolorado.json
    with open("/home/karan/python/internship/root/data/out/recolorado.json", "r") as json_file:
        data = json.load(json_file)
    
    # Extract the property data from the JSON file
    property_data = [entry["PROPERTY"] for entry in data.values() if "PROPERTY" in entry]

    # Insert property data into the database
    insert_property_data(property_data)
