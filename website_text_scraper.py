from bs4 import BeautifulSoup
from kanji_dict import kanji_dict
import requests


N5 = 0
N4 = 0
N3 = 0
N2 = 0
N1 = 0

url = "https://www3.nhk.or.jp/nhkworld/ja/"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

for character in soup.text:
    if character in kanji_dict["JLPT N5"]:
        N5 += 1
    if character in kanji_dict["JLPT N4"]:
        N4 += 1
    if character in kanji_dict["JLPT N3"]:
        N3 += 1
    if character in kanji_dict["JLPT N2"]:
        N2 += 1
    if character in kanji_dict["JLPT N1"]:
        N1 += 1

print(f"Number of JLPT N5 Characters: {N5}")
print(f"Number of JLPT N4 Characters: {N4}")
print(f"Number of JLPT N3 Characters: {N3}")
print(f"Number of JLPT N2 Characters: {N2}")
print(f"Number of JLPT N1 Characters: {N1}")
