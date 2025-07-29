from src.exceptions import ZeroQuantityError
from src.product import Product


class Category:
    name: str
    description: str
    __products: list

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self):
        return f"Category(name='{self.name}', products={self.__products})"

    def add_product(self, product):
        try:
            if not isinstance(product, Product):
                raise TypeError(
                    "Можно добавлять только объекты Product или его наследников"
                )
            if product.quantity == 0:
                raise ZeroQuantityError()

            self.__products.append(product)
            Category.number_of_products += 1
            print(f"Товар {product.name} успешно добавлен")
            return True

        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
            return False
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise
        finally:
            print("обработка добавления товара завершена")

    @property
    def products(self):
        return self.__products

    @property
    def product_count(self):
        return len(self.__products)

    @property
    def category_count(self):
        return Category.number_of_categories

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    # Методы для main.py
    def get_category_count(self):
        return self.category_count

    def get_product_count(self):
        return self.product_count
