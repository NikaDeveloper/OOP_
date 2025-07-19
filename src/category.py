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

    def add_product(self, product):
        self.__products.append(product)
        Category.number_of_products += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self):
        return len(self.__products)

    @property
    def products_list(self):
        return self.__products
