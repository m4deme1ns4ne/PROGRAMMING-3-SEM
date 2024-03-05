import json
import sqlite3 as sq


def database_connection(data: json) -> None:
    with sq.connect("lab5.db") as con:
        cur = con.cursor()
        json_string = json.dumps(data)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS logging (
                    datetime TEXT,
                    func_name TEXT,
                    params TEXT,
                    result TEXT
                    );
                    """)
        cur.execute(""" 
                    INSERT INTO logging (datetime, func_name, params, result) VALUES (?, ?, ?, ?)
                    """, (data['datetime'], data['func_name'], data['params'], data['result']))