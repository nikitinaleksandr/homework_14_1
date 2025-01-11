import pathlib
from pathlib import Path
import pytest
from mypy.types import names
from unicodedata import category
current_dir = Path(__file__).parent.parent.resolve()
cover_main = current_dir/'src'/'main.py'


from src.main import Product, Category
# from tests.conftest import product, first_category1, second_category2, category_not_products


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 80000.0
    assert product.quantity == 5


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 80000.0
    assert product.quantity == 5

def test_category_init(first_category1, second_category2, category_not_products):
    assert first_category1.name == "Смартфоны"
    assert first_category1.description == ("Смартфоны, как средство не только коммуникации, но и получения "
                                           "дополнительных функций для удобства жизни")
    assert second_category2.name == "Смартфоны"
    assert second_category2.description == ("Смартфоны, как средство не только коммуникации, но и получения "
                                            "дополнительных функций для удобства жизни")
    assert category_not_products.name == "Смартфоны"
    assert category_not_products.description == ("Смартфоны, как средство не только коммуникации, но и получения "
                                                 "дополнительных функций для удобства жизни")

    assert first_category1.category_count == 3
    assert second_category2.category_count == 3
    assert category_not_products.category_count == 3

    assert first_category1.product_count == 5
    assert second_category2.product_count == 5
    assert category_not_products.product_count == 5


    assert len(second_category2.products) == 3
    assert len(first_category1.products) == 2
    assert len(category_not_products.products) == 0

def test_category_init_not_category():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни", 0)
    assert int(category.products) == 0

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

def test_change_category_attributes(first_category1):
    #изменяем атрибуты
    first_category1.name = "Новый товар"
    first_category1.description = "wool, black"
    first_category1.products = [Product(name='socks', description="wool, black", price=120.0, quantity=50)]

    # Проверяем, что изменения прошли успешно
    assert first_category1.name == "Новый товар"
    assert first_category1.description == 'wool, black'
    assert len(first_category1.products) == 1

def test_type_data_product(second_category2):
    assert isinstance(second_category2.name, str)
    assert isinstance(second_category2.description, str)
    assert isinstance(second_category2.products, list)


def test_product_negativ_price(): #  "Цена должна быть больше нуля"
    with pytest.raises(ValueError, match="Цена должна быть больше нуля"):
        Product(name="Товар", description="Описание", price=-10.0, quantity=5)

def test_product_negativ_quantity(): #  "Цена должна быть больше нуля"
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Product(name="Товар", description="Описание", price=10.0, quantity=-5)