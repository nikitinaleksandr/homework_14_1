import pytest

def test_smartphone(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Высокотехнологичные смартфоны"
    assert category_smartphones.price == 10000
    assert category_smartphones.quantity == 7
    assert category_smartphones.efficiency == 2000
    assert category_smartphones.model == 'S800'
    assert category_smartphones.memory == 256
    assert category_smartphones.color == 'green'

def test_smartphone_add(category_smartphones, category_smartphones_2):
    assert category_smartphones + category_smartphones_2 == 16

def test_smartphone_add_error(category_smartphones, category_smartphones_2):
    # result = category_smartphones + 1
    with pytest.raises(TypeError):
        result = category_smartphones + 1