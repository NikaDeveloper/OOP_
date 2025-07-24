from src.product import Product


class LawnGrass(Product):

    def __init__(self, country, germination_period, color, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color