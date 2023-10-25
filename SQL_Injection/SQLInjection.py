def query_database(sql):
  """Queries the database with the given SQL statement."""
  cursor.execute(sql)
  results = cursor.fetchall()
  return results

# Without input validation:
user_input = "SELECT * FROM users WHERE username = 'admin'"
sql = "SELECT * FROM users WHERE username = '{}'".format(user_input)

results = query_database(sql)
print(results)

# With input validation:
user_input = input("Enter a username: ")

# Validate the user input.
if not user_input.isalnum():
  print("Invalid username.")
  exit()

sql = "SELECT * FROM users WHERE username = '{}'".format(user_input)

results = query_database(sql)
print(results)