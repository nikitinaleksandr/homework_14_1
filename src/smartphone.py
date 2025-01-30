from src.product import Product


# добавляет к классу Product новые свойства efficiency, model, memory, color
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency,
                 model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        # if type(other) is not type(self):
        #     return self.quantity + other.quantity
        # elif isinstance(other, int):
        #     return self.quantity + other
        else:
            raise TypeError
