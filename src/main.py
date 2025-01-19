class Product:  # Класс для создания продуктов с общими свойствами
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Количество

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description

        if float(price) > 0:
            self.__price = price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Количество не может быть отрицательным")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if float(price) < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, dict_product):
        name = dict_product['name']
        price = float(dict_product['price'])
        description = dict_product['description']
        quantity = dict_product['quantity']
        return cls(name, description, price, quantity)


class Category:  # Класс для создания категорий с общими свойствами
    name: str  # Название
    description: str  # Описание
    products: list  # Список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):  # Инициализация класса
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    # Метод в который нужно передавать объект класса Product
    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
          return self.__products

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

