import pathlib
from pathlib import Path
import pytest
from mypy.types import names
from unicodedata import category

from tests.conftest import product

# from tests.conftest import product

current_dir = Path(__file__).parent.parent.resolve()
cover_main = current_dir/'src'/'category.py'


from src.category import Category
from src.product import Product


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

    assert first_category1.product_count == 6
    assert second_category2.product_count == 6
    assert category_not_products.product_count == 6


    assert second_category2.products == 'Iphone 15, 210000.0 руб., Остаток: 8 шт.; Samsung Galaxy S23 Ultra, 31000.0 руб., Остаток: 5 шт.; Xiaomi Redmi Note 11, 80000.0 руб., Остаток: 14 шт.'
    assert first_category1.products == 'Iphone 15, 210000.0 руб., Остаток: 8 шт.; Samsung Galaxy S23 Ultra, 80000.0 руб., Остаток: 5 шт.'
    assert category_not_products.products == ''

def test_category_init_not_products():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни", [])
    assert category.products == ''

# Тест на изменение атрибутов



def test_change_category_attributes(first_category1):
    #изменяем атрибуты
    first_category1.name = "Новый товар"
    first_category1.description = "wool, black"
    first_category1.add_product = [Product(name='socks', description="wool, black", price=120.0, quantity=50)]
    # first_category1.add_product(...)
    # Проверяем, что изменения прошли успешно
    assert first_category1.name == "Новый товар"
    assert first_category1.description == 'wool, black'
    assert len(first_category1.products) == 96

def test_type_data_product(second_category2):
    assert isinstance(second_category2.name, str)
    assert isinstance(second_category2.description, str)
    assert isinstance(second_category2.products, str)

def test_str(first_category1):
    assert str(first_category1) == 'Смартфоны, количество продуктов: 13 шт.'

def test_middle_price(first_category1, category_not_products):
    assert first_category1.middle_price() == 145000.0
    assert category_not_products.middle_price() == 0


def test_add_product(first_category1):
    assert first_category1.product_count == 3


def test_add_non_product_raises_type_error(first_category1, non_product_object):
    with pytest.raises(TypeError, match="Объект должен быть экземпляром класса Product"):
        first_category1.add_product(non_product_object)
