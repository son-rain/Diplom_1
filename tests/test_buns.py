from praktikum.bun import Bun
import pytest


class TestBuns:
    @pytest.mark.parametrize('name, price',
                             [
                                 ['Ванильная булочка', '100.67'],
                                 ['Кунжутная булочка', '99.65'],
                                 ['Медовая булочка', '100']
                             ]
                             )
    def test_create_one_bun_and_check_name(self, name, price):
        float_price = float(price)
        bun = Bun(name, float_price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price',
                             [
                                 ['Ванильная булочка', '1'],
                                 ['Кунжутная булочка', '1000.065'],
                                 ['Медовая булочка', '100']
                             ]
                             )
    def test_create_one_bun_and_check_price(self, name, price):
        float_price = float(price)
        bun = Bun(name, float_price)
        assert bun.get_price() == float_price







