from django.conf import settings
import pandas as pd
import mysql.connector

data_frame = pd.read_excel('/home/mikeg/Downloadsd/Interests.xlsx')
databse_settings = settings.DATABASES['default']

cnx = mysql.connector.connect(
    host=databse_settings['HOST'],
    user=databse_settings['USER'],
    password=databse_settings['PASSWORD'],
    database='launchpad'
)
cursor = cnx.cursor()



# Iterate over each row in the DataFrame and insert data into MySQL
for _, row in data_frame.iterrows():
    # Extract the values from each column in the row
    column1 = row['Column1']
    column2 = row['Column2']
    # Add more columns as needed

    # Prepare the SQL query
    query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
    values = (column1, column2)
    # Add more values as needed

    # Execute the query
    cursor.execute(query, values)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
