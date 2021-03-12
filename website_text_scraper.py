from bs4 import BeautifulSoup
from kanji_dict import kanji_dict
import requests


N5 = 0
N5_unique = set()
N4 = 0
N4_unique = set()
N3 = 0
N3_unique = set()
N2 = 0
N2_unique = set()
N1 = 0
N1_unique = set()

url = "https://www3.nhk.or.jp/nhkworld/ja/"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


def parse_text(soup):
    for character in soup.text:
        try:
            level = kanji_dict[character]
        except:
            continue

        if level == "JLPT N5":
            N5 += 1
            N5_unique.add(character)
        if level == "JLPT N4":
            N4 += 1
            N4_unique.add(character)
        if level == "JLPT N3":
            N3 += 1
            N3_unique.add(character)
        if level == "JLPT N2":
            N2 += 1
            N2_unique.add(character)
        if level == "JLPT N1":
            N1 += 1
            N1_unique.add(character)


print(f"Number of JLPT N5 Characters: {N5}")
print(f"Number of JLPT N4 Characters: {N4}")
print(f"Number of JLPT N3 Characters: {N3}")
print(f"Number of JLPT N2 Characters: {N2}")
print(f"Number of JLPT N1 Characters: {N1}")
