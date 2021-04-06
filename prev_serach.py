import sqlite3


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
    try:
        mycursor.execute("INSERT INTO prev_search VALUES (?, ?, ?, ?, ?, ?)", i)
    except Exception:
        mycursor.execute(
            "UPDATE prev_search SET JLPT_5 = (?), JLPT_4 = (?), JLPT_3 = (?), JLPT_2 = (?), JLPT_1 = (?) WHERE url = (?)",
            i,
        )
    db.commit()