import sqlite3 as sql

DB_PATH = "C:/Users/Facundo/Dropbox/Task-App/database/tasks.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        task text,
        done boolean
    )""")
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    createDB()
