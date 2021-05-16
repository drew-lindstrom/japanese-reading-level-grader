from prev_search import *
import sqlite3
import pytest


class TestPrevSearch:
    @pytest.fixture
    def connect_to_temp_prev_search_table(self):
        db = sqlite3.connect("kanji.db")
        return db

    @pytest.fixture
    def create_temp_prev_search_table(self, connect_to_temp_prev_search_table):
        cursor = connect_to_temp_prev_search_table
        while True:
            try:
                cursor.execute(
                    "CREATE TABLE temp_prev_search (url text UNIQUE, JLPT_5 int, JLPT_4 int, JLPT_3 int, JLPT_2 int, JLPT_1 int)"
                )
                return cursor
            except:
                # delete_temp_prev_search_table
                return cursor

    # @pytest.fixture
    # def delete_temp_prev_search_table(self, connect_to_temp_prev_search_table):
    #     cursor = connect_to_temp_prev_search_table
    #     cursor.execute("DROP TABLE temp_prev_search")

    @pytest.mark.parametrize(
        "url,level,result",
        [
            ("testURL", 1, 5),
            ("testURL", 2, 5),
            ("testURL", 3, 5),
            ("testURL", 4, 5),
            ("testURL", 5, 5),
        ],
    )
    def test_update_prev_search_table(
        connect_to_temp_prev_search_table,
        create_temp_prev_search_table,
        url,
        level,
        result,
    ):
        cursor = create_temp_prev_search_table
        update_prev_search_table("testURL", [5, 5, 5, 5, 5], "temp_prev_search")
        update_prev_search_table("testURL", [5, 5, 5, 5, 5], "temp_prev_search")
        assert (
            cursor.execute(
                "SELECT * FROM temp_prev_search WHERE url = (?)", url
            ).fetchone()[level]
            == result
        )
