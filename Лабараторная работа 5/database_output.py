import sqlite3 as sq
from typing import Callable

def database_output(func: Callable) -> str:
    with sq.connect("lab5.db") as con:
        cur = con.cursor()
        cur.execute(
            """
            SELECT * FROM logging;
            """)
        rows = cur.fetchall()
        for result in rows:
            print(result)