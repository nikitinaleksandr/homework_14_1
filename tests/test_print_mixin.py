from src.product import Product
from src.BaseProduct import BaseProduct


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra","256GB, Серый цвет, 200MP камера",180000.0, 18)
    message = capsys.readouterr()
    # print(message)
    assert message.out.strip() == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера ,180000.0, 18)'