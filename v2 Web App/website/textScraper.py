from bs4 import BeautifulSoup
import requests
import sqlite3
from .kanjiDictionary import kanjiDict
from .models import Url


class UrlDataObject:
    def __init__(self):
        self.knownKanji = set()
        self.unknownKanji = set()
        self.totalKanjiCount = {
            "JLPT N5": 0,
            "JLPT N4": 0,
            "JLPT N3": 0,
            "JLPT N2": 0,
            "JLPT N1": 0,
        }
        self.knownKanjiCount = {
            "JLPT N5": 0,
            "JLPT N4": 0,
            "JLPT N3": 0,
            "JLPT N2": 0,
            "JLPT N1": 0,
        }
        self.readPercent = 0


def getUrlData(url, knownKanjiString):
    data = getUrlDataSetUp()
    initializeKnownKanjiDictionary(data, knownKanjiString)
    parseTextSetUp(url, data)
    calculateReadPercentage(data)
    urlModel = createNewUrlModel(data, url)
    return urlModel


def getUrlDataSetUp():
    data = UrlDataObject()
    return data


def initializeKnownKanjiDictionary(data, knownKanjiString):
    for character in knownKanjiString:
        if character in kanjiDict:
            data.knownKanji.add(character)


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

    data.readPercent = knownKanjiTotal / totalKanjiTotal


def createNewUrlModel(data, url):
    model = Url()
    model.url = str(url)
    model.totalN5 = int(data.totalKanjiCount["JLPT N5"])
    model.totalN4 = int(data.totalKanjiCount["JLPT N4"])
    model.totalN3 = data.totalKanjiCount["JLPT N3"]
    model.totalN2 = data.totalKanjiCount["JLPT N2"]
    model.totalN1 = data.totalKanjiCount["JLPT N1"]
    model.knownN5 = data.knownKanjiCount["JLPT N5"]
    model.knownN4 = data.knownKanjiCount["JLPT N4"]
    model.knownN3 = data.knownKanjiCount["JLPT N3"]
    model.knownN2 = data.knownKanjiCount["JLPT N2"]
    model.knownN1 = data.knownKanjiCount["JLPT N1"]
    model.unknownKanji = str(data.unknownKanji)
    model.readPercentage = data.readPercent
    return model