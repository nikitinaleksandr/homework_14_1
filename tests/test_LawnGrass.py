import pytest

def test_LawnGrass(LawnGrass_1):
    assert LawnGrass_1.name == "Газонная трава"
    assert LawnGrass_1.description == "Элитная трава для газона"
    assert LawnGrass_1.price == 500.0
    assert LawnGrass_1.quantity == 20
    assert LawnGrass_1.country == "Россия"
    assert LawnGrass_1.germination_period == "7 дней"
    assert LawnGrass_1.color == "Зеленый"


def test_LawnGrass_add(LawnGrass_1, LawnGrass_2):
    assert LawnGrass_1 + LawnGrass_2 == 35


def test_LawnGrass_add_error(LawnGrass_1, LawnGrass_2):

    with pytest.raises(TypeError):
        result = LawnGrass_1 + 1