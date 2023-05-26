from src.phone import Phone
from src.item import Item
import pytest

"""Тесты класса Phone"""

phone = Phone("iPhone 14", 120_000, 5, 2)


def test_magic_methods():
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test___add__():
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone == 25
    assert phone + phone == 10
    with pytest.raises(ValueError):
        phone + Phone


def test_sim_setter():
    assert phone.number_of_sim == 2
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
