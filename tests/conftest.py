import json

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def sample_product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def sample_product2():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def sample_product3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def empty_product():
    return Product(name="", description="", price=0.0, quantity=0)


@pytest.fixture
def sample_products():
    return [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def empty_products():
    return []


@pytest.fixture
def sample_category(sample_products):
    return Category(
        name="Смартфоны",
        description="Смартфоны с разными характеристиками",
        products=sample_products,
    )


@pytest.fixture
def empty_category(empty_products):
    return Category(
        name="Телевизоры",
        description="Телевизоры с OLED и QLED",
        products=empty_products,
    )


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.number_of_categories = 0
    Category.number_of_products = 0
    yield


@pytest.fixture
def temp_json_file(tmp_path):
    data = [
        {
            "name": "Тестовая категория",
            "description": "Описание тестовой категории",
            "products": [
                {
                    "name": "Тестовый товар",
                    "description": "Описание тестового товара",
                    "price": 1000.0,
                    "quantity": 10,
                }
            ],
        }
    ]
    file_path = tmp_path / "test_products.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        name="Test Phone",
        description="Test",
        price=1000,
        quantity=1,
        efficiency=90.0,
        model="X",
        memory=128,
        color="Black",
    )


@pytest.fixture
def sample_lawngrass():
    return LawnGrass(
        name="Test Grass",
        description="Test",
        price=100,
        quantity=1,
        country="Russia",
        germination_period="7 days",
        color="Green",
    )
