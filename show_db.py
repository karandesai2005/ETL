import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(user='root', password='karanishu', host='localhost', database='RECOLORADO_RESO')
cursor = cnx.cursor()

# Execute SELECT query
cursor.execute("SELECT * FROM property_ptnf")

# Fetch all rows
rows = cursor.fetchall()

# Print the header row
header = [column[0] for column in cursor.description]
print('\t'.join(header))

# Print the rows
for row in rows:
    formatted_row = []
    for value in row:
        if value is None:
            formatted_row.append("NULL")
        else:
            formatted_row.append(str(value))
    print('\t'.join(formatted_row))

# Close the cursor and connection
cursor.close()
cnx.close()
