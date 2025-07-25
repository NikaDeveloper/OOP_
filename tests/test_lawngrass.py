import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_lawngrass_creation():
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.price == 500.0
    assert grass.country == "Россия"
    assert isinstance(grass, Product)


def test_lawngrass_str():
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
    expected_str = "Газонная трава, 500.0 руб. Остаток: 20 шт."
    assert str(grass) == expected_str


def test_add_lawngrass():
    grass1 = LawnGrass(
        name="Grass 1",
        description="Premium",
        price=500,
        quantity=10,
        country="Russia",
        germination_period="7 days",
        color="Green",
    )
    grass2 = LawnGrass(
        name="Grass 2",
        description="Standard",
        price=400,
        quantity=15,
        country="USA",
        germination_period="5 days",
        color="Dark Green",
    )
    total = grass1 + grass2
    assert total == (500 * 10) + (400 * 15)


def test_add_different_classes_raises_error():
    smartphone = Smartphone(
        name="iPhone",
        description="",
        price=1000,
        quantity=1,
        efficiency=0,
        model="",
        memory=0,
        color="",
    )
    grass = LawnGrass(
        name="Grass",
        description="",
        price=100,
        quantity=1,
        country="",
        germination_period="",
        color="",
    )
    with pytest.raises(TypeError):
        smartphone + grass
