import json

from src.product import Product
from src.category import Category


def load_data_from_json(filename):
    """Загружает данные о категориях и товарах из JSON-файла
    и возвращает список объектов Category"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} содержит невалидный JSON")
        return []

    if not data or not isinstance(data, list):
        print("Ошибка: файл не содержит данных или имеет неверный формат")
        return []

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data['products']:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products.append(product)

        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )
        categories.append(category)

    return categories
