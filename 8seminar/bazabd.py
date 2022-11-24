import sqlite3

def create_bd():
    conn = sqlite3.connect('orders.db')
    return conn
def create_schema_db(cur, conn):
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT,
        lname TEXT,
        telefon TEXT);
    """)
    conn.commit()

def vizual(cur):
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    return all_results

def add_us(cur, conn, femili, name, telehon):
    v = f"INSERT INTO users (fname, lname, telefon) VALUES ('{femili}', '{name}', '{telehon}');"
    cur.execute(v)
    conn.commit()

def delit(cur, conn, num):
    f = f"DELETE FROM users WHERE userid= {num}"
    cur.execute(f)
    conn.commit()
    print('Удалено')


    

