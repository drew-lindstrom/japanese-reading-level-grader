from known_kanji import *
import pytest


class TestKnownKanji:
    def test_get_known_kanji(self):
        string = "afd 234 s旅行中 行中"
        known_kanji = get_known_kanji(string)
        assert ("旅" in known_kanji) == True
        assert ("中" in known_kanji) == True
        assert ("行" in known_kanji) == True
        assert ("a" in known_kanji) == False
        assert ("2" in known_kanji) == False
