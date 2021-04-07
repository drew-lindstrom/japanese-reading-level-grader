from bs4 import BeautifulSoup
import requests
import sqlite3


def get_kanji(url, kanji_count, unique_kanji):
    db = sqlite3.connect("kanji.db")
    db.text_factory = bytes
    mycursor = db.cursor()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    return parse_text(mycursor, soup, kanji_count, unique_kanji)


def parse_text(mycursor, soup, kanji_count, unique_kanji):
    for character in soup.text:
        try:
            mycursor.execute("SELECT * FROM kanji_table WHERE kanji=?", character)
            result = mycursor.fetchone()
            level = result[1].decode("utf-8")
        except:
            continue

        if level == "JLPT N5":
            kanji_count[0] += 1
            unique_kanji["N5"].add(character)
        if level == "JLPT N4":
            kanji_count[1] += 1
            unique_kanji["N4"].add(character)
        if level == "JLPT N3":
            kanji_count[2] += 1
            unique_kanji["N3"].add(character)
        if level == "JLPT N2":
            kanji_count[3] += 1
            unique_kanji["N2"].add(character)
        if level == "JLPT N1":
            kanji_count[4] += 1
            unique_kanji["N1"].add(character)