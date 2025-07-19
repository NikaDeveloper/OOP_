import json

from src.category import Category
from src.product import Product


def load_data_from_json(filename):
    """Загружает данные о категориях и товарах из JSON-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Ошибка: файл {filename} содержит невалидный JSON: {e}")
                return []
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []

    if not isinstance(data, list):
        print("Ошибка: ожидался список категорий")
        return []

    categories = []
    for category_data in data:
        if not isinstance(category_data, dict):
            print("Ошибка: данные категории должны быть словарем")
            continue

        required_category_fields = ["name", "description", "products"]
        if not all(field in category_data for field in required_category_fields):
            print("Ошибка: неверная структура данных категории")
            continue

        if not isinstance(category_data["products"], list):
            print("Ошибка: products должен быть списком")
            continue

        products = []
        for product_data in category_data["products"]:
            if not isinstance(product_data, dict):
                print("Ошибка: данные товара должны быть словарем")
                continue

            required_product_fields = ["name", "description", "price", "quantity"]
            if not all(field in product_data for field in required_product_fields):
                print(
                    "Ошибка: неверная структура данных товара - отсутствуют обязательные поля"
                )
                continue

            try:
                product = Product(
                    name=str(product_data["name"]),
                    description=str(product_data["description"]),
                    price=float(product_data["price"]),
                    quantity=int(product_data["quantity"]),
                )
                products.append(product)
            except (ValueError, TypeError) as e:
                print(f"Ошибка преобразования данных товара: {e}")
                continue

        try:
            category = Category(
                name=str(category_data["name"]),
                description=str(category_data["description"]),
                products=products,
            )
            categories.append(category)
        except Exception as e:
            print(f"Ошибка при создании категории: {e}")
            continue

    return categories
