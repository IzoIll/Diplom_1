import pytest
import pytest_cov
from ..praktikum.burger import Burger

class TestBurger:

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_sauce(self, ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce)
        assert ingredient_sauce in burger.ingredients

    def test_add_ingredient_fill(self, ingredient_fill):
        burger = Burger()
        burger.add_ingredient(ingredient_fill)
        assert ingredient_fill in burger.ingredients

    def test_remove_ingredient(self, ingredient_sauce, ingredient_fill):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_fill)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_fill]

    def test_move_ingredient(self, ingredient_sauce, ingredient_fill):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_fill)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_fill, ingredient_sauce]

    def test_get_price_with_ingredients(self, bun, ingredient_sauce):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        assert burger.get_price() == bun.get_price.return_value * 2 + ingredient_sauce.get_price.return_value

    def test_get_price_without_ingredients(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.get_price() == bun.get_price.return_value * 2

    def test_get_receipt(self, bun, ingredient_sauce, ingredient_fill):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_fill)
        receipt = burger.get_receipt()
        new_receipt = (
            '(==== Bulochka ====)\n'
             '= sauce Mayonez =\n'
             '= filling Kotletka =\n'
             '(==== Bulochka ====)\n'
             '\n'
             'Price: 50.0')
        assert receipt == new_receipt

    def test_get_receipt_without_ingredients(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        new_receipt = (
            '(==== Bulochka ====)\n'
            '(==== Bulochka ====)\n'
            '\n'
            'Price: 10.0')
        assert receipt == new_receipt