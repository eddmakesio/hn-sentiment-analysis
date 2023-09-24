import sqlite3

def create_tables(cur: sqlite3.Connection):
    with open("./db/sql/tables.sql", 'r') as sql_file:
        sql_script = sql_file.read()
        cur.executescript(sql_script)

if __name__ == '__main__':
    con = sqlite3.connect("./db/hn_sentiment_analysis.db")
    cur = con.cursor()
    create_tables(cur)
    con.commit()
    cur.close()
