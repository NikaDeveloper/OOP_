from src.category import Category
from src.product import Product


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Смартфоны с разными характеристиками"

    products_str = sample_category.products

    assert "Samsung Galaxy S23 Ultra" in products_str
    assert "Iphone 15" in products_str
    assert "Xiaomi Redmi Note 11" in products_str
    assert sample_category.product_count == 3


def test_empty_category(empty_category, empty_products):
    assert empty_category.name == "Телевизоры"
    assert empty_category.description == "Телевизоры с OLED и QLED"
    assert empty_category.products == ""
    assert empty_category.product_count == 0


def test_category_count_increases(sample_category, empty_category):
    assert Category.number_of_categories == 2


def test_product_count_increases(sample_category, empty_category):
    assert Category.number_of_products == 3


def test_category_products_are_product_instances(sample_category):
    for product in sample_category.products_list:
        assert isinstance(product, Product)


def test_category_str_representation(sample_category):
    total_quantity = sum(product.quantity for product in sample_category.products_list)
    expected_str = f"{sample_category.name}, количество продуктов: {total_quantity} шт."
    assert str(sample_category) == expected_str


def test_add_product_to_category(sample_category, sample_product1):
    initial_count = sample_category.product_count
    sample_category.add_product(sample_product1)
    assert sample_category.product_count == initial_count + 1


def test_products_list_property(sample_category):
    products = sample_category.products_list
    assert len(products) == 3
    assert all(isinstance(p, Product) for p in products)


def test_product_property(sample_category):
    products_str = sample_category.products
    assert "Samsung Galaxy S23 Ultra" in products_str
    assert "Iphone 15" in products_str
    assert "Xiaomi Redmi Note 11" in products_str


def test_product_count_property(sample_category):
    assert sample_category.product_count == 3
