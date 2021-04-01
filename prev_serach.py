import sqlite3

# TODO: Duplicate urls?


def update_prev_search_db(url, kanji_count):
    db = sqlite3.connect("kanji.db")
    mycursor = db.cursor()

    i = (
        url,
        kanji_count[0],
        kanji_count[1],
        kanji_count[2],
        kanji_count[3],
        kanji_count[4],
    )

    mycursor.execute("INSERT INTO prev_search VALUES (?, ?, ?, ?, ?, ?)", i)
    db.commit()