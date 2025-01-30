from src.product import Product

class LawnGrass(Product): # добавляет к классу Product новые свойства efficiency, model, memory, color
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        # elif isinstance(other, int):
        #     return self.quantity + other
        else:
            raise TypeError

