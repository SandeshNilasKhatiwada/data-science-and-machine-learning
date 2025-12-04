import sqlite3
conn = sqlite3.connect('database.db')
try:
    cur = conn.cursor()
    print ("Connected to the database successfully.")
    query = "create table if not exists students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT);"
    cur.execute(query)
    conn.commit()
    print("Table created successfully.")

    query = "select * from students;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    cur.close()
    conn.close()
