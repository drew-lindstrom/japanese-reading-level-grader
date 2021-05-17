from util import *
import pytest


class TestUtil:
    @pytest.fixture
    def create_unique_kanji(self):
        """Creates dummy dictionary of unique kanji for tests."""
        unique_kanji = {}
        unique_kanji["N5"] = set()
        unique_kanji["N5"].add("a")
        unique_kanji["N5"].add("b")
        unique_kanji["N5"].add("c")

        unique_kanji["N4"] = set()
        unique_kanji["N4"].add("d")
        unique_kanji["N4"].add("e")
        unique_kanji["N4"].add("g")

        unique_kanji["N3"] = set()
        unique_kanji["N3"].add("s")
        unique_kanji["N3"].add("g")
        unique_kanji["N3"].add("e")
        unique_kanji["N3"].add("h")

        unique_kanji["N2"] = set()
        unique_kanji["N2"].add("p")
        unique_kanji["N2"].add("e")
        unique_kanji["N2"].add("l")

        unique_kanji["N1"] = set()
        unique_kanji["N1"].add("n")
        unique_kanji["N1"].add("m")
        unique_kanji["N1"].add("b")

        return unique_kanji

    def test_get_total(self):
        kanji_count = [3, 5, 6, 2, 4]
        assert get_total(kanji_count) == 20

    def test_get_unique_total(self, create_unique_kanji):
        unique_kanji = create_unique_kanji
        assert get_unique_total(unique_kanji) == 16

    def test_reset_unique_kanji(self, create_unique_kanji):
        unique_kanji = create_unique_kanji
        reset_unique_kanji(unique_kanji)
        assert len(unique_kanji["N5"]) == 0
        assert len(unique_kanji["N4"]) == 0
        assert len(unique_kanji["N3"]) == 0
        assert len(unique_kanji["N2"]) == 0
        assert len(unique_kanji["N1"]) == 0

    def test_reset_kanji_count(self):
        kanji_count = [3, 5, 6, 2, 4]
        reset_kanji_count(kanji_count)
        assert kanji_count[0] == 0
        assert kanji_count[1] == 0
        assert kanji_count[2] == 0
        assert kanji_count[3] == 0
        assert kanji_count[4] == 0