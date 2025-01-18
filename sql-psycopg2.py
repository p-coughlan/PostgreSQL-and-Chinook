import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Create a cursor object using the cursor() method - this is used to execute SQL commands 
cursor = connection.cursor()

# fetch the results (multiple), setting a variable to hold the results
results = cursor.fetchall()

# fetch the results (single), setting a variable to hold the results
# results = cursor.fetchone()

# close the connection
connection.close()

# print the results using a loop
for result in results:
    print(result)

