from db_setup import *
import sqlite3
import pytest


class TestDbSetup:
    @pytest.fixture
    def connect_to_kanji_table(self):
        """Pytest fixture to connect to kanji database."""
        db = sqlite3.connect("kanji.db")
        return db

    def test_kanji_table_setup(self, connect_to_kanji_table):
        """Tests connection to kanji_table by asserting if the table contains 2220 rows."""
        cursor = connect_to_kanji_table
        assert len(list(cursor.execute("SELECT * FROM kanji_table"))) == 2220

    @pytest.mark.parametrize(
        "kanji,level",
        [
            ("万", "JLPT N5"),
            ("去", "JLPT N4"),
            ("受", "JLPT N3"),
            ("替", "JLPT N2"),
            ("就", "JLPT N1"),
        ],
    )
    def test_kanji_table_contents(self, connect_to_kanji_table, kanji, level):
        """Tests contents of kanji table by searching for five kanji of various levels
        asserting the table returns the correct levels."""
        cursor = connect_to_kanji_table
        assert (
            cursor.execute(
                "SELECT * FROM kanji_table WHERE kanji = (?)", kanji
            ).fetchone()[1]
            == level
        )
