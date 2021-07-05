from bs4 import BeautifulSoup
import requests
import sqlite3
from kanjiDictionary import kanjiDict
from models import Url


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


def getUrlData(url):
    data = getUrlDataSetUp()
    parseTextSetUp(url, data)
    calculateReadPercentage(data)
    dataModel = createNewDataModel(data, url)
    return dataModel


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


def createNewDataModel(data, url):
    model = Url()
    model.url = url
    totalN5 = data.totalKanjiCount["JLPT N5"]
    totalN4 = data.totalKanjiCount["JLPT N4"]
    totalN3 = data.totalKanjiCount["JLPT N3"]
    totalN2 = data.totalKanjiCount["JLPT N2"]
    totalN1 = data.totalKanjiCount["JLPT N1"]
    knownN5 = data.knownKanjiCount["JLPT N5"]
    knownN4 = data.knownKanjiCount["JLPT N4"]
    knownN3 = data.knownKanjiCount["JLPT N3"]
    knownN2 = data.knownKanjiCount["JLPT N2"]
    knownN1 = data.knownKanjiCount["JLPT N1"]
    unknownKanji = str(data.unknownKanji)
    readPercentage = data.readPercent
    return model