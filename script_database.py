import sqlite3

DB_FILE = 'mydatabase.db'

# Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# # Create the table
# c.execute("""
# CREATE TABLE mytable (
#     id INTEGER PRIMARY KEY,
#     date DATE,
#     time TIME,
#     operator TEXT,
#     shift TEXT,
#     planned_time INTEGER,
#     planned_stops INTEGER,
#     activation_time INTEGER,
#     productive_time INTEGER,
#     availability INTEGER,
#     utilization INTEGER,
#     effective_utilization INTEGER
# )
# """)

# # Insert some data into the table
# c.execute("INSERT INTO mytable (id, date, time, operator, shift, planned_time) VALUES (1, '2022-04-01', '22:30:00', 'Anand', 'day', 12)")
# c.execute("INSERT INTO mytable (id, date, time, operator, shift, planned_time) VALUES (2, '2022-04-01', '21:30:00', 'Anand', 'day', 8)")
# c.execute("INSERT INTO mytable (id, date, time, operator, shift, planned_time) VALUES (3, '2022-04-01', '20:30:00', 'Anand', 'night', 8)")
# c.execute("INSERT INTO mytable (id, date, time, operator, shift, planned_time) VALUES (4, '2022-04-01', '22:30:00', 'Anand', 'day', 10)")

c.execute("UPDATE mytable SET date=?, operator=?, shift=?, planned_time=? WHERE id=?", ('2022-04-01', 'Greg', 'day', 12, 3))

# Commit the changes and close the connection
conn.commit()
conn.close()
