import pathlib
from pathlib import Path
import pytest
from mypy.types import names
from unicodedata import category

from tests.conftest import product

current_dir = Path(__file__).parent.parent.resolve()
cover_main = current_dir/'src'/'product.py'


from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 80000.0
    assert product.quantity == 5


def test_new_product():
    data = {
        'name': 'Товар',
        'price': '100',
        'description': 'Описание',
        'quantity': 10
    }
    product = Product.new_product(data)

    assert product.name == 'Товар'
    assert product.price == 100.0  # Проверяем, что цена преобразована в float
    assert product.description == 'Описание'
    assert product.quantity == 10


# Тест на изменение атрибутов

def test_change_product_attributes(product):
    #изменяем атрибуты
    product.name = "Новый товар"
    product.price = 150.0
    product.quantity = 5

    # Проверяем, что изменения прошли успешно
    assert product.name == "Новый товар"
    assert product.price == 150.0
    assert product.quantity == 5

def test_product_negativ_price(): #  "Цена должна быть больше нуля"
    # @price.setter
    # assert price(self, price=-1):
    #     print("Цена не должна быть нулевая или отрицательная")

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        Product(name="Товар", description="Описание", price=-10.0, quantity=5)
def test_product_zero_price(): #  "Цена должна быть больше нуля"
    # @price.setter
    # assert price(self, price=-1):
    #     print("Цена не должна быть нулевая или отрицательная")

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        Product(name="Товар", description="Описание", price=0, quantity=5)
def test_product_negativ_quantity(): #  "Цена должна быть больше нуля"
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Product(name="Товар", description="Описание", price=10.0, quantity=-5)


def test_price():
    "Правильность возврата цены с помощью геттера"
    product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    # product = Product(name="Товар", price=10)  # Создай экземпляр
    assert product.price == 180000.0  # Используй геттер
    # price = 10
    # assert self.__price == price


    # price(self) == self_price
def test_price_getter(product):
    assert product.price == 80000.0  # Проверяем, что геттер возвращает правильную цену
