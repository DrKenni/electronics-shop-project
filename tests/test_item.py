"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class Test_Item:

    def test___repr__(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"

    def test___str__(self):
        item1 = Item("Смартфон", 10000, 20)
        assert str(item1) == 'Смартфон'

    def test_calculate_total_price(self):
        example = Item("Apple", 15, 67)
        assert example.calculate_total_price() == 1005

    def test_apply_discount(self):
        example = Item("Book", 100, 14)
        example.pay_rate = 0.9
        example.apply_discount()
        assert example.price == 90

    def test_name(self):
        item = Item('Телефон', 10000, 5)
        assert item.name == 'Телефон'
        item.name = 'Смартфон'
        assert item.name == 'Смартфон'
        item.name = 'СуперСмартфон'
        assert item.name == 'Смартфон'

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv()
        assert len(Item.all) == 5
        item1 = Item.all[0]
        assert item1.name == 'Смартфон'

    def test_string_to_number(self):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5
