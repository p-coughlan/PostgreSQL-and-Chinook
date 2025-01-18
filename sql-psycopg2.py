import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Create a cursor object using the cursor() method - this is used to execute SQL commands 
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# Directly includes the value in the query string, which is less secure.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = \'Queen\'') # backslash is used to escape the single quote

# Uses a parameterized query, which is more secure and the recommended practice.
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ['Queen']) # using a placeholder to avoid SQL injection (passing a list)

# Query 4 - Select only by "ArtistId" # 51 (using a placeholder)
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistId" # 51 on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])

# fetch the results (multiple), setting a variable to hold the results
results = cursor.fetchall()

# fetch the results (single), setting a variable to hold the results
# results = cursor.fetchone()

# close the connection
connection.close()

# print the results using a loop
for result in results:
    print(result)

