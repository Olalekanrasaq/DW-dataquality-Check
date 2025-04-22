import os
import psycopg2
pgpassword = "********"
conn = None
try:
    conn = psycopg2.connect(
        user = "olalekanrasaq1331",
        password = pgpassword,
        host = "pgdb",
        port = "5432",
        database = "billingDW")
except Exception as e:
    print("Error connecting to data warehouse")
    print(e)
else:
    print("Successfully connected to warehouse")
finally:
    if conn:
        conn.close()
        print("Connection closed")
