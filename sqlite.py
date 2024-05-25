import sqlite3

# Step 1: Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('Books.db')

# Step 2: Create a cursor object
cursor = connection.cursor()

# Step 3: Execute a SQL command to create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    author TEXT NOT NULL
)
''')

# # Step 4: Commit the changes
connection.commit()

# # Step 5: Check the schema
# cursor.execute('''
# SELECT sql FROM sqlite_master WHERE type='table' AND name='books'
# ''')
# schema = cursor.fetchone()

# # Print the schema
# print("Schema for 'books' table:")
# print(schema[0])

# # Step 6: Close the connection
# connection.close()
