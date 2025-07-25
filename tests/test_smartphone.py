from src.product import Product
from src.smartphone import Smartphone


def test_smartphone_creation():
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    assert smartphone.name == "iPhone 15"
    assert smartphone.price == 210000.0
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert isinstance(smartphone, Product)


def test_smartphone_str():
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    expected_str = "iPhone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(smartphone) == expected_str


def test_add_smartphones():
    smartphone1 = Smartphone(
        name="iPhone 15",
        description="512GB",
        price=210000,
        quantity=2,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray",
    )
    smartphone2 = Smartphone(
        name="Samsung S23",
        description="256GB",
        price=180000,
        quantity=3,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Black",
    )
    total = smartphone1 + smartphone2
    assert total == (210000 * 2) + (180000 * 3)
