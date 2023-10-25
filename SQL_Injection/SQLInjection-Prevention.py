import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.sqlite3')


# Create a cursor
cursor = conn.cursor()


# Define the parameterized query
query = "SELECT * FROM users WHERE username = ?"


# Execute the query with the user-supplied username
cursor.execute(query, (username,))


# Get the results
results = cursor.fetchall()


# Close the cursor and connection
cursor.close()
conn.close()