
import psycopg2

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="color_frequency_db",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor object
cur = conn.cursor()

# Create the color_frequencies table
cur.execute("""
    CREATE TABLE color_frequencies (
        id SERIAL PRIMARY KEY,
        color VARCHAR(50),
        frequency INT
    )
""")

# Define the colors and their frequencies
colors_data = [
    ("Red", 10),
    ("Blue", 7),
    ("Green", 5),
    ("Yellow", 3)
]

# Insert the colors and their frequencies into the table
for color, frequency in colors_data:
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
