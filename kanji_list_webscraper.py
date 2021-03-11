import requests
import pprint
from bs4 import BeautifulSoup


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


kanji_dict = {}
get_kanji_dict(kanji_dict)
new_dict = swap_key_and_value(kanji_dict)
