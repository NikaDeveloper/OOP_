def test_product_attributes(sample_product1):
    assert sample_product1.name == "Samsung Galaxy S23 Ultra"
    assert sample_product1.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product1.price == 180000.0
    assert sample_product1.quantity == 5


def test_empty_product(empty_product):
    assert empty_product.name == ""
    assert empty_product.description == ""
    assert empty_product.price == 0.0
    assert empty_product.quantity == 0


def test_product_price_type(sample_product2):
    assert isinstance(sample_product2.price, float)


def test_product_quantity_type(sample_product3):
    assert isinstance(sample_product3.quantity, int)
