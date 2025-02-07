from src.BaseProduct import BaseProduct
from src.print_mixin import ProductMixin


class Product(BaseProduct, ProductMixin):
    # Класс для создания продуктов с общими свойствами
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
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __add__(self, other):
        'Функция возвращающая произведение цены на количество у двух объектов'
        new_numerator = ((self.price * self.quantity) +
                         (other.price * other.quantity))

        return new_numerator

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if float(price) <= 0:
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

    def __str__(self):
        """
        Строковое значение класса Product
        'Название продукта, 80 руб. Остаток: 15 шт.'
        """
        return f"{self.name}, {self.price} руб., Остаток: {self.quantity} шт."
