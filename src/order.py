from abc import ABC, abstractmethod

from src.exceptions import ZeroQuantityError


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
        try:
            if quantity < 0:
                raise ValueError("Количество не может быть отрицательным")
            if quantity == 0:
                raise ZeroQuantityError()

            self.product = product
            self.quantity = quantity
            print(f"Товар {product.name} добавлен в заказ")
        except (ValueError, ZeroQuantityError) as e:
            print(f"Ошибка: {e}")
            raise
        finally:
            print("Обработка создания заказа завершена")

    @property
    def total_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, количество: {self.quantity}, общая стоимость: {self.total_cost}"
