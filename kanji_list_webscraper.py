import requests
import pprint
from bs4 import BeautifulSoup
import mysql.connector


def get_kanji_dict(kanji_dict):
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
    new_dict = {}
    for key in kanji_dict.keys():
        for character in kanji_dict[key]:
            new_dict[character] = key

    return new_dict


def create_table():
    mycursor.execute("CREATE DATABASE kanji_database")
    mycursor.execute(
        "CREATE TABLE Kanji (kanji CHAR, level STRING, kanjiID int PRIMARY KEY AUTO_INCREMENT)"
    )


kanji_dict = {}
get_kanji_dict(kanji_dict)
new_dict = swap_key_and_value(kanji_dict)

db = mysql.connector.connect(
    host="localhost",
    user="",
    passwd="",
    database="kanji_database",
    auth_plugin="mysql_native_password",
)

mycursor = db.cursor