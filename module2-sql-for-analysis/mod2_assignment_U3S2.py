import psycopg2
import pandas as pd
import sqlite3

sl_conn = sqlite3.connect("/home/antony/Lambda/DS-Unit-3-Sprint-2-SQL"
                "-and-Databases/module1-introduction-to-sql/"
                "rpg_db.sqlite3")
sl_curs = sl_conn.cursor()

row_count = "SELECT COUNT(*) FROM charactercreator_character"
sl_curs.execute(row_count).fetchall()