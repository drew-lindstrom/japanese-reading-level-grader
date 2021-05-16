from db_setup import *
import sqlite3
import pytest


class Test_Db_Setup:
    @pytest.fixture
    def connect_to_kanji_table(self):
        db = sqlite3.connect("kanji.db")
        return db

    def test_kanji_table_setup(self, connect_to_kanji_table):
        cursor = connect_to_kanji_table
        assert len(list(cursor.execute("SELECT * FROM kanji_table"))) == 4440
