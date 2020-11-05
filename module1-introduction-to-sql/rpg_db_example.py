import sqlite3 as sq3

def connect_db(db_name="/home/antony/Lambda/DS-Unit-3-Sprint-2-SQL"
                "-and-Databases/module1-introduction-to-sql/"
                "rpg_db.sqlite3"):
    return sq3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS_TOTALS = """
    SELECT COUNT(*)
    FROM charactercreator_character;
"""


GET_SUBCLASS_TOTALS_CLERIC = """
    SELECT COUNT(*)
    FROM charactercreator_cleric;
"""


GET_SUBCLASS_TOTALS_FIGHTER = """
    SELECT COUNT(*)
    FROM charactercreator_fighter;
"""


GET_SUBCLASS_TOTALS_MAGE = """
    SELECT COUNT(*)
    FROM charactercreator_mage;
"""


GET_SUBCLASS_TOTALS_NECROMANCER = """
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
"""


GET_SUBCLASS_TOTALS_THIEF = """
    SELECT COUNT(*)
    FROM charactercreator_thief;
"""


GET_ITEM_TOTALS = """
    SELECT COUNT(*)
    FROM armory_item;
"""


GET_WEAPONS = """
    SELECT COUNT(item_id)
    FROM armory_item as ai
    INNER JOIN armory_weapon as aw
    ON aw.item_ptr_id = ai.item_id;
"""

GET_NONWEAPONS = """
    SELECT(SELECT COUNT(item_id)
    FROM armory_item)-
    (SELECT COUNT(item_ptr_id)
    FROM armory_weapon);
"""

GET_CHAR_ITEMS = """
    SELECT cc.character_id, cc.name, ci.item_count
    FROM charactercreator_character as cc
    LEFT JOIN(SELECT character_id, COUNT(*) as item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id) as ci
    ON ci.character_id = cc.character_id
    LIMIT 20;
"""

GET_CHAR_WEAPONS ="""
    SELECT cc.character_id, cc.name, ci.weapons
    FROM charactercreator_character as cc
    LEFT JOIN(SELECT character_id, COUNT(*) as weapons
    FROM (SELECT ci.character_id, ci.item_id, aw.item_ptr_id
    FROM charactercreator_character_inventory as ci
    INNER JOIN armory_weapon as aw
    ON aw.item_ptr_id = ci.item_id)
    GROUP BY character_id) as ci
    ON ci.character_id = cc.character_id
    LIMIT 20;
"""

GET_ITEM_AVERAGE = """
    SELECT AVG(item_count)
    FROM(SELECT cc.character_id, cc.name, ci.item_count
    FROM charactercreator_character as cc
    LEFT JOIN(SELECT character_id, COUNT(*) as item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id) as ci
    ON ci.character_id = cc.character_id);
"""

GET_WEAPONS_AVERAGE = """
    SELECT AVG(weapons)
    FROM(SELECT cc.character_id, cc.name, ci.weapons
    FROM charactercreator_character as cc
    LEFT JOIN(SELECT character_id, COUNT(*) as weapons
    FROM (SELECT ci.character_id, ci.item_id, aw.item_ptr_id
    FROM charactercreator_character_inventory as ci
    INNER JOIN armory_weapon as aw
    ON aw.item_ptr_id = ci.item_id)
    GROUP BY character_id) as ci
    ON ci.character_id = cc.character_id);
"""

if __name__ == "__main__":
    conn = connect_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS_TOTALS)
    print("Number of chars ", results[0])
    results_typs_cl = execute_query(curs, GET_SUBCLASS_TOTALS_CLERIC)
    print("Number of clerics ", results_typs_cl[0])
    results_typs_fight = execute_query(curs, GET_SUBCLASS_TOTALS_FIGHTER)
    print("Number of fighters ", results_typs_fight[0])
    results_typs_mage = execute_query(curs, GET_SUBCLASS_TOTALS_MAGE)
    print("Number of mages ", results_typs_mage[0])
    results_typs_necro = execute_query(curs, GET_SUBCLASS_TOTALS_NECROMANCER)
    print("Number of necromancers ", results_typs_necro[0])
    results_typs_thief = execute_query(curs, GET_SUBCLASS_TOTALS_THIEF)
    print("Number of thiefs ", results_typs_thief[0])
    results_items = execute_query(curs, GET_ITEM_TOTALS)
    print("Number of items ", results_items[0])
    results_weapons = execute_query(curs, GET_WEAPONS)
    print("Number of weapon items ", results_weapons[0])
    results_nonweapons = execute_query(curs, GET_NONWEAPONS)
    print("Number of non-weapon items ", results_nonweapons[0])
    results_char_items = execute_query(curs, GET_CHAR_ITEMS)
    print("Number of items each character has", results_char_items[0:])
    results_char_weapons = execute_query(curs, GET_CHAR_WEAPONS)
    print("Number of weapons each character has", results_char_weapons[0:])
    results_items_avg = execute_query(curs, GET_ITEM_AVERAGE)
    print("Average number of items ", results_items_avg[0])
    results_weapons_avg = execute_query(curs, GET_WEAPONS_AVERAGE)
    print("Average number of weapon items ", results_weapons_avg[0])
