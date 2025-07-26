import pytest

from src.order import Order
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 5)


@pytest.fixture
def sample_order(sample_product):
    return Order(sample_product, 3)


def test_order_initialization(sample_order, sample_product):
    assert sample_order.product == sample_product
    assert sample_order.quantity == 3


def test_order_total_cost(sample_order):
    assert sample_order.total_cost == 300.0  # 100 * 3


def test_order_str_representation(sample_order):
    expected_str = "Заказ: Test Product, количество: 3, общая стоимость: 300.0"
    assert str(sample_order) == expected_str


def test_order_with_zero_quantity(sample_product):
    order = Order(sample_product, 0)
    assert order.total_cost == 0.0


def test_order_with_negative_quantity(sample_product):
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Order(sample_product, -1)
