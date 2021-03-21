from bs4 import BeautifulSoup
from kanji_dict import kanji_dict
import requests
import sqlite3


def parse_text(soup, kanji_count, unique_kanji):
    for character in soup.text:
        try:
            # Need to fix parameter input.
            mycursor.execute("SELECT * FROM kanji_list WHERE kanji=?", character)
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


def print_count(kanji_count):
    print(f"Number of JLPT N5 Characters: {kanji_count[0]}")
    print(f"Number of JLPT N4 Characters: {kanji_count[1]}")
    print(f"Number of JLPT N3 Characters: {kanji_count[2]}")
    print(f"Number of JLPT N2 Characters: {kanji_count[3]}")
    print(f"Number of JLPT N1 Characters: {kanji_count[4]}")
    print()


def print_count_unique(unique_kanji):
    print(f"Number of Unique JLPT N5 Characters: {len(unique_kanji['N5'])}")
    print(f"Number of Unique JLPT N4 Characters: {len(unique_kanji['N4'])}")
    print(f"Number of Unique JLPT N3 Characters: {len(unique_kanji['N3'])}")
    print(f"Number of Unique JLPT N2 Characters: {len(unique_kanji['N2'])}")
    print(f"Number of Unique JLPT N1 Characters: {len(unique_kanji['N1'])}")
    print()


db = sqlite3.connect("kanji.db")
db.text_factory = bytes
mycursor = db.cursor()

unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}
kanji_count = [0, 0, 0, 0, 0]

print("Enter URL: ")
url = input()

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

parse_text(soup, kanji_count, unique_kanji)
print_count(kanji_count)
print_count_unique(unique_kanji)