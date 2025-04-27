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
