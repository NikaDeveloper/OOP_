from abc import ABC, abstractmethod


class BaseOrder(ABC):
    @abstractmethod
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    @abstractmethod
    def total_cost(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Order(BaseOrder):
    def __init__(self, product, quantity):
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.product = product
        self.quantity = quantity

    @property
    def total_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, количество: {self.quantity}, общая стоимость: {self.total_cost}"
