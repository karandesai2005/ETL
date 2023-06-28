import json
import mysql.connector
from datetime import datetime
# Read the JSON file
with open('master.json') as f:
    data = json.load(f)

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='karanishu',
                              host='localhost', database='RECOLORADO_RESO')

# Create a cursor object
cursor = cnx.cursor()

# Iterate over the data and insert into the table
for i in range(len(data['TERABITZ_ID'])):
    terabitz_id = data['TERABITZ_ID'][i]
    prop_id = data['ID'][i]
    datasource = data['DATASOURCE'][i]
    unit_number = data['UNIT_NUMBER'][i]
    address = data['ADDRESS'][i] 
    city = data['CITY'][i]
    state = data['STATE'][i]
    zip_code = data['ZIP'][i]
    county = data['COUNTY'][i]
    latitude = data['latitude'][i]
    longitude = data['longitude'][i]
    prop_type = data['TYPE'][i]
    subtype = data['SUBTYPE'][i]
    description = data['DESCRIPTION'][i]
    parselnumber = data['PARCEL_NUMBER'][i]
    beds = data['BEDS'][i]
    mls_number = data['MLS_NUMBER'][i]
    status = data['STATUS'][i]
    orignalprice = data['ORIG_LISTPRICE'][i]
    currentprice = data['CURR_LISTPRICE'][i]
    modif_stamp = datetime.strptime(data['MODIF_TIMESTAMP'][i], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
    # Insert the values into the table
    query = "INSERT INTO property_ptnf (TERABITZ_ID, ID, DATASOURCE, UNIT_NUMBER, ADDRESS,  CITY, STATE, ZIP, COUNTY, LATITUDE, LONGITUDE, TYPE, SUBTYPE, DESCRIPTION, PARCEL_NUMBER, BEDS,  MLS_NUMBER, STATUS, ORIG_LISTPRICE, CURR_LISTPRICE, MODIF_TIMESTAMP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)"
    values = (terabitz_id, prop_id, datasource,unit_number,address, city, state, zip_code, county, latitude, longitude, prop_type, subtype, description, parselnumber,beds, mls_number, status, orignalprice, currentprice, modif_stamp)
    cursor.execute(query, values)

# Commit the changes to the database
cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()

print("Data has been inserted into the table.")
