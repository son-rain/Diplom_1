from typing import List

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_in_database(self):
        database: Database = Database()
        buns: List[Bun] = database.available_buns()
        assert database.buns == buns

    def test_available_ingredients_in_database(self):
        database: Database = Database()
        ingredients: List[Ingredient] = database.available_ingredients()
        assert database.ingredients == ingredients