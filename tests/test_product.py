from src.product import Product


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


def test_new_product_method():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 5


def test_duplicate_product_merge():
    products = [Product("Test Product", "Desc", 100.0, 5)]
    product_data = {
        "name": "Test Product",
        "description": "New Desc",
        "price": 150.0,
        "quantity": 3,
    }
    product = Product.new_product(product_data, products)
    assert product.quantity == 8
    assert product.price == 150.0
    assert len(products) == 1


def test_price_setter_validation():
    product = Product("Test", "Desc", 100.0, 5)

    product.price = -50
    assert product.price == 100.0

    product.price = 0
    assert product.price == 100.0

    product.price = 200.0
    assert product.price == 200.0
