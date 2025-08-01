import pytest

from src.category import Category
from src.exceptions import ZeroQuantityError
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Смартфоны с разными характеристиками"
    assert len(sample_category.products) == 3
    assert sample_category.product_count == 3


def test_empty_category(empty_category, empty_products):
    assert empty_category.name == "Телевизоры"
    assert empty_category.description == "Телевизоры с OLED и QLED"
    assert len(empty_category.products) == 0
    assert empty_category.product_count == 0


def test_category_count_increases(sample_category, empty_category):
    assert Category.number_of_categories == 2


def test_product_count_increases(sample_category, empty_category):
    assert Category.number_of_products == 3


def test_category_products_are_product_instances(sample_category):
    for product in sample_category.products:
        assert isinstance(product, Product)


def test_category_str_representation(sample_category):
    total_quantity = sum(product.quantity for product in sample_category.products)
    expected_str = f"{sample_category.name}, количество продуктов: {total_quantity} шт."
    assert str(sample_category) == expected_str


def test_add_product_to_category(sample_category, sample_product1):
    """Тест добавления обычного продукта в категорию"""
    initial_count = sample_category.product_count
    sample_category.add_product(sample_product1)
    assert sample_category.product_count == initial_count + 1
    assert sample_product1 in sample_category.products


def test_products_list_property(sample_category):
    products = sample_category.products
    assert len(products) == 3
    assert all(isinstance(p, Product) for p in products)


def test_product_property(sample_category):
    products = sample_category.products
    product_names = [product.name for product in products]
    assert "Samsung Galaxy S23 Ultra" in product_names


def test_product_count_property(sample_category):
    assert sample_category.product_count == 3


def test_add_smartphone_to_category(sample_category):
    """Тест добавления смартфона в категорию"""
    smartphone = Smartphone(
        name="New Phone",
        description="",
        price=1000,
        quantity=1,
        efficiency=0,
        model="",
        memory=0,
        color="",
    )
    initial_count = sample_category.product_count
    sample_category.add_product(smartphone)
    assert sample_category.product_count == initial_count + 1
    assert smartphone in sample_category.products


def test_add_lawngrass_to_category(sample_category):
    """Тест добавления газонной травы в категорию"""
    grass = LawnGrass(
        name="New Grass",
        description="",
        price=100,
        quantity=1,
        country="",
        germination_period="",
        color="",
    )
    initial_count = sample_category.product_count
    sample_category.add_product(grass)
    assert sample_category.product_count == initial_count + 1
    assert grass in sample_category.products


def test_add_invalid_product_raises_error(sample_category):
    """Тест попытки добавления не-продукта в категорию"""
    with pytest.raises(TypeError):
        sample_category.add_product("Not a product")

    with pytest.raises(TypeError):
        sample_category.add_product(123)

    with pytest.raises(TypeError):
        sample_category.add_product({"name": "Dict", "price": 100})


def test_average_price_with_products(sample_category):
    assert sample_category.average_price() == pytest.approx(140333.33, abs=0.01)


def test_average_price_empty_category(empty_category):
    assert empty_category.average_price() == 0


def test_average_price_single_product():
    product = Product("Test", "Desc", 100.0, 1)
    category = Category("Test Cat", "Desc", [product])
    assert category.average_price() == 100.0


def test_average_price_zero_price_products():
    products = [
        Product("Product1", "Desc", 0.0, 1),
        Product("Product2", "Desc", 0.0, 1),
    ]
    category = Category("Test Cat", "Desc", products)
    assert category.average_price() == 0.0


def test_average_price_after_adding_product(sample_category):
    initial_avg = sample_category.average_price()
    new_product = Product("New Product", "Desc", 300000.0, 1)
    sample_category.add_product(new_product)

    new_avg = sample_category.average_price()
    assert new_avg == pytest.approx(180250.0, abs=0.01)
    assert new_avg > initial_avg


def test_average_price_after_removing_product(sample_category):
    initial_avg = sample_category.average_price()

    product_to_remove = sample_category.products[0]
    sample_category.products.remove(product_to_remove)

    new_avg = sample_category.average_price()
    assert new_avg != initial_avg
    assert len(sample_category.products) == 2


def test_original_tests_still_work(sample_category, empty_category):
    assert str(sample_category) == "Смартфоны, количество продуктов: 27 шт."
    assert str(empty_category) == "Телевизоры, количество продуктов: 0 шт."

    initial_count = sample_category.product_count
    new_product = Product("New", "Desc", 100.0, 1)
    sample_category.add_product(new_product)
    assert sample_category.product_count == initial_count + 1

    assert sample_category.category_count > 0
    assert sample_category.get_product_count() == sample_category.product_count


def test_add_product_with_zero_quantity(sample_category):
    """Тест добавления продукта с нулевым количеством в категорию"""
    with pytest.raises(ZeroQuantityError):
        zero_product = Product("Zero Product", "Desc", 100.0, 0)
        sample_category.add_product(zero_product)


def test_add_product_success_message(capsys, sample_category):
    """Тест сообщения об успешном добавлении товара"""
    product = Product("Test", "Desc", 100.0, 1)
    sample_category.add_product(product)
    captured = capsys.readouterr()
    assert "Товар Test успешно добавлен" in captured.out
    assert "обработка добавления товара завершена" in captured.out.lower()
