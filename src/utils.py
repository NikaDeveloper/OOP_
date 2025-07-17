import json

from src.category import Category
from src.product import Product


def load_data_from_json(filename):
    """Загружает данные о категориях и товарах из JSON-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} содержит невалидный JSON")
        return []

    if not isinstance(data, list):
        print("Ошибка: ожидался список категорий")
        return []

    categories = []
    for category_data in data:
        if not all(key in category_data for key in ["name", "description", "products"]):
            print("Ошибка: неверная структура данных категории")
            continue

        products = []
        for product_data in category_data["products"]:
            if not all(
                key in product_data
                for key in ["name", "description", "price", "quantity"]
            ):
                print("Ошибка: неверная структура данных товара")
                continue

            try:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=float(product_data["price"]),
                    quantity=int(product_data["quantity"]),
                )
                products.append(product)
            except (ValueError, TypeError):
                print("Ошибка: неверные данные товара")
                continue

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
