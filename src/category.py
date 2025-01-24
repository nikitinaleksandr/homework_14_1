from itertools import product


class Category:  # Класс для создания категорий с общими свойствами
    name: str  # Название
    description: str  # Описание
    products: list  # Список товаров категории
    category_count = 0
    product_count = 0



    def __init__(self, name, description, products=[]):  # Инициализация класса
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
        # self._product_count = 0


        # Метод в который нужно передавать объект класса Product
    def add_product(self, product):
        # if self.__products == []:
        #     self.__products.append([])
        # else:
        self.__products.append(product)
    product_count += 1





    # @property
    # def products(self):
    #     list_products = ""
    #     for prod in self.__products:
    #         list_products +=f'Название {prod.name}, описание {prod.description}, цена {prod.price}, количество {prod.quantity}'
    #         return list_products
    #     # return self.__products

    def __str__(self):
        sum_quantity = 0
        for prod in self.__products:
            sum_quantity += int(prod.quantity)

        return f"{self.name}, количество продуктов: {sum_quantity} шт."


    @property
    def products(self):
        return "; ".join(str(product) for product in self.__products)

