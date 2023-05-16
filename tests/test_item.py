"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class Test_Item:

    def test_calculate_total_price(self):
        example = Item("Apple", 15, 67)
        assert example.calculate_total_price() == 1005

    def test_apply_discount(self):
        example = Item("Book", 100, 14)
        example.pay_rate = 0.9
        example.apply_discount()
        assert example.price == 90
