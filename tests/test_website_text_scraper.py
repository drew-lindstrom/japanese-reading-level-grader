from website_text_scraper import *
import pytest


class TestWebsiteTextScraper:
    @pytest.fixture
    def initialize_parse_text_test(self):
        db = sqlite3.connect("kanji.db")
        db.text_factory = bytes
        mycursor = db.cursor()
        text_string = "海外に住んでいる方、あるいは海外旅行中の方のために、ニュース・情報番組のほか、ドラマ、音楽番組、子ども番組などを放送しています。"
        unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}
        kanji_count = [0, 0, 0, 0, 0]
        known_kanji_count = [0, 0, 0, 0, 0]
        known_kanji = "海外旅行中"
        unknown_kanji = {
            "N5": set(),
            "N4": set(),
            "N3": set(),
            "N2": set(),
            "N1": set(),
        }

        return (
            mycursor,
            text_string,
            kanji_count,
            unique_kanji,
            known_kanji,
            known_kanji_count,
            unknown_kanji,
        )

    def test_parse_text(self, initialize_parse_text_test):
        (
            cursor,
            soup_text,
            kanji_count,
            unique_kanji,
            known_kanji,
            known_kanji_count,
            unknown_kanji,
        ) = initialize_parse_text_test

        parse_text(
            cursor,
            soup_text,
            kanji_count,
            unique_kanji,
            known_kanji,
            known_kanji_count,
            unknown_kanji,
        )

        assert kanji_count[0] == 5
        assert kanji_count[1] == 9
        assert kanji_count[2] == 9
        assert kanji_count[3] == 0
        assert kanji_count[4] == 0

        assert len(unique_kanji["N5"]) == 4
        assert len(unique_kanji["N4"]) == 7
        assert len(unique_kanji["N3"]) == 5
        assert len(unique_kanji["N2"]) == 0
        assert len(unique_kanji["N1"]) == 0

        assert known_kanji_count[0] == 4
        assert known_kanji_count[1] == 3
        assert known_kanji_count[2] == 0
        assert known_kanji_count[3] == 0
        assert known_kanji_count[4] == 0

        assert len(unknown_kanji["N5"]) == 1
        assert len(unknown_kanji["N4"]) == 5
        assert len(unknown_kanji["N3"]) == 5
        assert len(unknown_kanji["N2"]) == 0
        assert len(unknown_kanji["N1"]) == 0