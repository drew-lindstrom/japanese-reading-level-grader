import sqlite3


def update_prev_search_table(url, kanji_count, table="prev_search"):
    """Updates database containing past searches. Searches are oraganized by URL
    and total count for each kanji level is recorded. Unique kanji is not recorded.
    Duplicate URLs can not exist and will update already existing identical URLs.
    Websites with no kanji are not tracked."""
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


def get_all_time_total():
    """Returns a list containing total count of kanji for each JLPT level for every
    unique URL in the previous search database."""
    db = sqlite3.connect("kanji.db")
    mycursor = db.cursor()
    mycursor.execute(
        "SELECT SUM(JLPT_5), SUM(JLPT_4), SUM(JLPT_3), SUM(JLPT_2), SUM(JLPT_1) FROM prev_search"
    )
    return list(mycursor)