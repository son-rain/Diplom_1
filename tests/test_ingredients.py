from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredients:
    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_FILLING, 'Куриное мясо', '70'],
                                 [INGREDIENT_TYPE_SAUCE, 'Горчичный соус', '44']
                             ]
                             )
    def test_create_ingredient_and_check_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_FILLING, 'Куриное мясо', '70'],
                                 [INGREDIENT_TYPE_SAUCE, 'Горчичный соус', '44']
                             ]
                             )
    def test_create_ingredient_and_check_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_FILLING, 'Куриное мясо', '70'],
                                 [INGREDIENT_TYPE_SAUCE, 'Горчичный соус', '44']
                             ]
                             )
    def test_create_ingredient_and_check_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
