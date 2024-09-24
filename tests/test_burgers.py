from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurgers:
    def test_set_buns_to_burger(self, get_bun):
        burger = Burger()
        bun = get_bun
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredients_to_burger(self, get_list_ingredients):
        list_ingredients = get_list_ingredients
        burger = Burger()
        for i in list_ingredients:
            burger.add_ingredient(i)
        assert burger.ingredients == list_ingredients

    def test_delete_ingredients_from_burger(self, get_list_ingredients):
        list_ingredients = get_list_ingredients
        burger = Burger()
        for i in list_ingredients:
            burger.add_ingredient(i)
        del list_ingredients[1]
        burger.remove_ingredient(1)
        assert burger.ingredients == list_ingredients

    def test_move_ingredients_from_burger(self, get_list_ingredients):
        list_ingredients = get_list_ingredients
        burger = Burger()
        for i in list_ingredients:
            burger.add_ingredient(i)
        list_ingredients.insert(0, list_ingredients.pop(1))
        burger.move_ingredient(0, 1)
        assert burger.ingredients == list_ingredients

    def test_get_price_of_burger(self, get_list_ingredients, get_bun):
        list_ingredients = get_list_ingredients
        bun_data = Mock()
        bun_data.get_price.return_value = 100.67
        bun = bun_data
        buns_price = bun_data.get_price() * 2
        ingredients_price = 0
        burger = Burger()
        burger.set_buns(bun)
        for i in list_ingredients:
            burger.add_ingredient(i)
            ingredients_price += i.get_price()
        burger_price = buns_price + ingredients_price
        assert burger.get_price() == burger_price

    def test_get_receipt_of_burger(self, get_list_ingredients, get_bun, get_receipt_list):
        list_ingredients = get_list_ingredients
        bun = get_bun
        buns_price = bun.get_price() * 2
        ingredients_price = 0
        burger = Burger()
        burger.set_buns(bun)
        for i in list_ingredients:
            burger.add_ingredient(i)
            ingredients_price += i.get_price()
        burger_price = buns_price + ingredients_price
        burger_receipt = get_receipt_list
        burger_receipt.append(f'Price: {burger_price}')
        assert burger.get_receipt() == '\n'.join(burger_receipt)


