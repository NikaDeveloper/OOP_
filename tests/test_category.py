from src.category import Category
from src.product import Product


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Смартфоны с разными характеристиками"
    assert len(sample_category.products) == 3
    assert sample_category.products == sample_products


def test_empty_category(empty_category, empty_products):
    assert empty_category.name == "Телевизоры"
    assert empty_category.description == "Телевизоры с OLED и QLED"
    assert len(empty_category.products) == 0
    assert empty_category.products == empty_products


def test_category_count_increases(sample_category, empty_category):
    assert (
        Category.number_of_categories == 2
    )  # создали 2 категории (sample_category и empty_category)


def test_product_count_increases(sample_category, empty_category):
    # sample_category содержит 3 продукта, empty_category — 0
    assert Category.number_of_products == 3


def test_category_products_are_product_instances(sample_category):
    for product in sample_category.products:
        assert isinstance(product, Product)


def test_category_str_representation(sample_category):
    assert (
        str(sample_category)
        == f"{sample_category.name}, количество продуктов: {len(sample_category.products)}"
    )
