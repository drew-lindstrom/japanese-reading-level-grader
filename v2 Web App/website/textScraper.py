from bs4 import BeautifulSoup
import requests
import sqlite3
from kanjiDictionary import kanjiDict


class UrlDataObject:
    def __init__(self):
        self.knownKanji = set()
        self.unknownKanji = set()
        self.totalKanjiCount = {"N5": 0, "N4": 0, "N3": 0, "N2": 0, "N1": 0}
        self.knownKanjiCount = {"N5": 0, "N4": 0, "N3": 0, "N2": 0, "N1": 0}
        self.readPercent = 0


def getUrlData(url):
    data = getUrlDataSetUp()
    parseTextSetUp(url, data)
    calculateReadPercentage(data)
    return data


def getUrlDataSetUp():
    data = UrlDataObject()
    initializeKnownKanji(data)
    return data


def initializeKnownKanji(data):
    pass


def parseTextSetUp(url, data):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    return parseText(soup.text, data)


def parseText(soup_text, data):
    for character in soup_text:
        try:
            level = kanjiDict[character]
        except:
            continue

        if level:
            data.totalKanjiCount[level] += 1
            if character in data.knownKanji:
                data.knownKanjiCount[level] += 1
            else:
                data.unknownKanji.add(character)


def calculateReadPercentage(data):
    totalKanjiTotal = 0
    knownKanjiTotal = 0
    for value in data.totalKanjiCount.values():
        totalKanjiTotal += value

    for value in data.knownKanjiCount.values():
        knownKanjiTotal += value

    return knownKanjiTotal / totalKanjiTotal
