import pytest
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item1) == 'Смартфон'


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()

    assert item1.price == 8000.0


def test_name_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара равна 10 символов
    item.name = '0123456789'
    assert item.name == '0123456789'


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[0].name == "Смартфон"


def test_add():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10



