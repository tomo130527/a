import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('database.sqlite')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value INTEGER
);
"""

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Insert some data into the table
data = [
    ('First row', 10),
    ('Second row', 20),
    ('Third row', 30)
]

# Define the SQL command to insert rows
insert_query = """
INSERT INTO my_table (title, value) VALUES (?, ?)
"""

# Execute the SQL command to insert rows
cursor.executemany(insert_query, data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Database created and data inserted successfully!")
