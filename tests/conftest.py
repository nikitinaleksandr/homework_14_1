import pytest
from src.category import Category
from src.product import Product
from src.LawnGrass import LawnGrass
from src.smartphone import Smartphone



@pytest.fixture
def first_category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни",
        products=[Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
                  Product(name="Samsung Galaxy S23 Ultra", description = "256GB, Серый цвет, 200MP камера",
                          price = 80000.0, quantity = 5)]
    )

@pytest.fixture
def second_category2():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни",
        products=[Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
                  Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера",
                          price=31000.0, quantity=5),
                  Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий",
                          price=80000.0, quantity=14)
                  ]
    )

@pytest.fixture
def category_not_products():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни",
        products=[]
    )

@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=80000.0,
        quantity=5)

# @pytest.fixture
# def product():
#     return Product(name="Товар", price=100, quantity=10)

@pytest.fixture
def product_a():
    return Product(name="Product A", description="Description A", price=10, quantity=10)

@pytest.fixture
def product_b():
    return Product(name="Product b", description="Description b", price=20, quantity=10)

@pytest.fixture
def category_4():
    return Category(name="Product b", quantity=10)


@pytest.fixture
def category_smartphones():
    return  Smartphone("Смартфоны", "Высокотехнологичные смартфоны", 10000, 7, 2000, 'S800',256, 'green')
#     category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

