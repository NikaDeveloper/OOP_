from src.base_product import BaseProduct
from src.log_mixin import LogMixin


class Product(LogMixin, BaseProduct):

    def __init__(self, name, description, price, quantity):
        super().__init__()
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data, products_list=None):
        if products_list is None:
            products_list = []

        for existing_product in products_list:
            if existing_product.name == product_data["name"]:
                existing_product.quantity += product_data["quantity"]
                if product_data["price"] > existing_product.price:
                    existing_product.price = product_data["price"]
                return existing_product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if hasattr(self, "_Product__price") and new_price < self.__price:
            confirm = input(
                f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        return (
            f"Product('{self.name}', {self.price} руб., Остаток: {self.quantity} шт.)"
        )
