from src.category import Category
from src.product import Product
from src.utils import load_data_from_json


def main():
    # Загрузка данных из JSON
    categories = load_data_from_json("src/products.json")

    # Вывод информации о категориях и товарах
    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products)}")
        print(f"Средняя цена: {category.average_price():.2f} руб.")
        print("Товары:")
        for product in category.products:
            print(
                f"- {product.name}: {product.price} руб. (Остаток: {product.quantity})"
            )


if __name__ == "__main__":
    # Проверка создания продукта с нулевым количеством (должно прервать программу)
    product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)

    # Этот код не выполнится, если выше возникла ошибка
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    print(category1.average_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.average_price())

    main()
