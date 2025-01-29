def test_smartphone(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Высокотехнологичные смартфоны"
    assert category_smartphones.price == 10000
    assert category_smartphones.quantity == 7
    assert category_smartphones.efficiency == 2000
    assert category_smartphones.model == 'S800'
    assert category_smartphones.memory == 256
    assert category_smartphones.color == 'green'
