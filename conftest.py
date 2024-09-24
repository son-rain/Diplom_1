from typing import List

import pytest

from data import Data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture(scope='function')
def get_bun():
    bun = Bun(*Data.BUN_DATA.values())
    return bun


@pytest.fixture(scope='function')
def get_list_ingredients():
    ingredients_list = []
    for i in Data.INGREDIENTS_LIST:
        ingredient = Ingredient(*i)
        ingredients_list.append(ingredient)
    return ingredients_list


@pytest.fixture(scope='function')
def get_receipt_list():
    receipt: List[str] = [f'(==== {Data.BUN_DATA['name']} ====)']
    for i in Data.INGREDIENTS_LIST:
        receipt.append(f"= {i[0].lower()} {i[1]} =")
    receipt.append(f'(==== {Data.BUN_DATA['name']} ====)\n')
    return receipt
