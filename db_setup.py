import requests
import pprint
from bs4 import BeautifulSoup
import sqlite3


def get_kanji_dict(kanji_dict):
    """Parses website that lists kanji by JLPT level (Japanese Language Proficiency Test).
    Results are placed in a temporary dictionary."""
    url = "https://www.nihongo-pro.com/kanji-pal/list/jlpt"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    outputLists = soup.find("div", class_="outputLists")

    for outputList in outputLists:
        try:
            name = outputList.find("div", class_="outputListName").a.text
        except:
            continue

        kanji_list = []

        kanjiList = outputList.find("div", class_="kanjiList")

        for kanji in kanjiList:
            try:
                kanji_list.append(kanji.text)
            except:
                continue

        kanji_dict[name] = kanji_list


def swap_key_and_value(kanji_dict):
    """Utility function to swap kanji and JLPT level in temporary dictionary."""
    new_dict = {}
    for key in kanji_dict.keys():
        for character in kanji_dict[key]:
            new_dict[character] = key
    return new_dict


def create_kanji_list(new_dict, kanji_list):
    # TODO: This function probably isn't needed/can be simplified with previous two functions.
    """Utility function to change dictionary contain kanji into a list."""
    for key in new_dict:
        kanji_list.append((key, new_dict[key]))


def create_prev_search_table():
    """Creates mysql database table for results of previous URL searches.
    Each entry saves URL and the number of kanji in each JLPT level.
    Does not keep track of unique kanji. URL entrys are unique."""
    mycursor.execute(
        "CREATE TABLE prev_search (url text UNIQUE, JLPT_5 int, JLPT_4 int, JLPT_3 int, JLPT_2 int, JLPT_1 int)"
    )


def create_kanji_table():
    """Creates mysql database table for each kanji with its corresponding JLPT level."""
    mycursor.execute("CREATE TABLE kanji_table (kanji text, level text)")


def update_kanji_table(kanji_list):
    """Updates kanji_table database with kanji and JLPT level pairs from kanji_list."""
    mycursor.executemany("INSERT INTO kanji_table VALUES (?, ?)", kanji_list)
    db.commit()


kanji_dict = {}
kanji_list = []

db = sqlite3.connect("kanji.db")
mycursor = db.cursor()


# get_kanji_dict(kanji_dict)
# new_dict = swap_key_and_value(kanji_dict)
# create_kanji_list(new_dict, kanji_list)

# create_prev_search_table()
# create_kanji_table()
update_kanji_table(kanji_list)