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
    expected_str = (
        f"{sample_category.name}, количество продуктов: {sample_category.product_count}"
    )
    assert str(sample_category) == expected_str
