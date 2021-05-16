from prev_search import *
import sqlite3
import pytest


class TestPrevSearch:
    @pytest.fixture
    def connect_to_temp_prev_search_table(self):
        """Pytest fixture to connect to database."""
        db = sqlite3.connect("kanji.db")
        return db

    @pytest.fixture
    def create_temp_prev_search_table(self, connect_to_temp_prev_search_table):
        """Pytest fixture to create a temporary prev_search table."""
        cursor = connect_to_temp_prev_search_table
        try:
            self.delete_temp_prev_search_table(cursor)
        except:
            pass
        cursor.execute(
            "CREATE TABLE temp_prev_search (url text UNIQUE, JLPT_5 int, JLPT_4 int, JLPT_3 int, JLPT_2 int, JLPT_1 int)"
        )
        return cursor

    def delete_temp_prev_search_table(self, cursor):
        """Deletes temp_prev_search table."""
        cursor.execute("DROP TABLE temp_prev_search")

    def test_update_prev_search_table(
        self,
        connect_to_temp_prev_search_table,
        create_temp_prev_search_table,
    ):
        """Tests that update_prev_search_table operates correctly and checks that duplicates aren't present."""
        cursor = connect_to_temp_prev_search_table
        update_prev_search_table("testURL", [5, 5, 5, 5, 5], "temp_prev_search")
        update_prev_search_table("testURL", [5, 5, 5, 5, 5], "temp_prev_search")
        assert cursor.execute(
            "SELECT * FROM temp_prev_search WHERE url = (?)", ("testURL",)
        ).fetchone() == ("testURL", 5, 5, 5, 5, 5)
        assert len(list(cursor.execute("SELECT * FROM temp_prev_search"))) == 1
        self.delete_temp_prev_search_table(cursor)