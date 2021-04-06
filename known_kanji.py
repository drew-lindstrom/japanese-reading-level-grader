import sqlite3


def get_known_kanji():
    known_kanji = set()
    f = open("Known_Kanji.txt", "r")

    db = sqlite3.connect("kanji.db")
    mycursor = db.cursor()

    for line in f:
        for char in line:
            mycursor.execute("SELECT * FROM kanji_table WHERE kanji=?", char)
            result = mycursor.fetchone()
            if result:
                known_kanji.add(result[0])

    f.close()

    return known_kanji
