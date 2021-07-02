import sqlite3


def get_known_kanji(text=None):
    """Parses a text document containing list of user's known kanji.
    Will only add characters found in kanji.db to known_kanji list."""
    known_kanji = set()

    if text == None:
        f = open("known_kanji.txt", "r")
    else:
        f = text

    db = sqlite3.connect("kanji.db")
    mycursor = db.cursor()

    for line in f:
        for char in line:
            mycursor.execute("SELECT * FROM kanji_table WHERE kanji=?", char)
            result = mycursor.fetchone()
            if result:
                known_kanji.add(result[0])

    if text == None:
        f.close()

    return known_kanji
