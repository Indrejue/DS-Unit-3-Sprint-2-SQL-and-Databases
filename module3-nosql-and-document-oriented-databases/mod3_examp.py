#example of importing sqlite to pymongo

import sqlite3
import pymongo


PASSWORD="lGnXgiPkFfesDVQ3"
DBNAME="test2"


def create_mbd_conn(password, dbname):
    client = pymongo.MongoClient("mongodb+srv://Antony_Farag:{}@cluster0."
        "a9iur.mongodb.net/{}?retryWrites=true&w=majority"
        .format(PASSWORD, DBNAME)
    )
    return client


def create_sl_conn(extraction_db="/home/antony/Lambda/DS-Unit-3-Sprint-2-SQL"
                "-and-Databases/module1-introduction-to-sql/"
                "rpg_db.sqlite3"):
    sl_conn =sqlite3.connect(extraction_db)
    return sl_conn


def execute_query(curs, query):
    return curs.execute(query).fetchall()


def char_doc_creation(db, char_table):
    for char in char_table:
        char_doc = {
            "name": char[1],
            "level": char[2],
            "exp": char[3],
            "hp": char[4],
            "strength": char[5],
            "intelligence": char[6],
            "dexterity": char[7],
            "wisdom": char[8],
        }
        mongodb.insert_one(char_doc)

GET_CHAACTERS = "SELECT * FROM charactercreator_character"

if __name__ == "__main__":
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()
    client = create_mbd_conn(PASSWORD, DBNAME)
    db = client.test2