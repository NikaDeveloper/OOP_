import json

from src.category import Category
from src.product import Product
from src.utils import load_data_from_json


def test_load_valid_json(temp_json_file):
    categories = load_data_from_json(temp_json_file)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Тестовая категория"
    assert categories[0].product_count == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Тестовый товар"


def test_file_not_found():
    result = load_data_from_json("nonexistent_file.json")
    assert result == []


def test_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("{invalid json}")

    result = load_data_from_json(file_path)
    assert result == []


def test_empty_json(tmp_path):
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("")

    result = load_data_from_json(file_path)
    assert result == []


def test_not_list_json(tmp_path):
    file_path = tmp_path / "not_list.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"key": "value"}, f)

    result = load_data_from_json(file_path)
    assert result == []


def test_empty_list_json(tmp_path):
    file_path = tmp_path / "empty_list.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([], f)

    result = load_data_from_json(file_path)
    assert result == []


def test_category_counters(temp_json_file):
    Category.number_of_categories = 0
    Category.number_of_products = 0

    _ = load_data_from_json(temp_json_file)

    assert Category.number_of_categories == 1
    assert Category.number_of_products == 1


def test_skip_product_with_invalid_structure(tmp_path, capsys):
    file_path = tmp_path / "test_products.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Valid Product",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                },
                {"name": "Invalid Product"},
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Raw data: {data}")
    categories = load_data_from_json(file_path)
    print(f"Loaded categories: {categories}")
    if categories:
        print(
            f"Category details: {categories[0].name}, products: {categories[0].products}"
        )
    captured = capsys.readouterr()

    assert len(categories) == 1, f"Expected 1 category, got {len(categories)}"
    if categories:
        print(f"Category products: {categories[0].products}")
        assert len(categories[0].products) == 1
        assert categories[0].products[0].name == "Valid Product"
    assert "неверная структура данных товара" in captured.out


def test_skip_product_with_invalid_data_types(tmp_path, capsys):
    file_path = tmp_path / "invalid_data_types.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Valid Product",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                },
                {
                    "name": "Invalid Product",
                    "description": "Desc",
                    "price": "not_a_number",
                    "quantity": 5,
                },
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    assert file_path.exists()
    assert file_path.stat().st_size > 0

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 1, "Должна быть загружена 1 категория"
    assert len(categories[0].products) == 1, "Должен быть 1 валидный товар"
    assert categories[0].products[0].name == "Valid Product"
    assert "Ошибка преобразования данных товара" in captured.out


def test_skip_category_with_invalid_data(tmp_path, capsys):
    file_path = tmp_path / "invalid_category_data.json"
    data = [
        {"name": "Valid Category", "description": "Desc", "products": []},
        {"invalid": "data"},
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 1
    assert "неверная структура данных категории" in captured.out


def test_product_data_conversion_errors(tmp_path, capsys):
    file_path = tmp_path / "conversion_errors.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Invalid Price",
                    "description": "Desc",
                    "price": "not_a_number",
                    "quantity": 5,
                }
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 1
    assert len(categories[0].products) == 0
    assert "Ошибка преобразования данных товара" in captured.out


def test_invalid_products_type(tmp_path, capsys):
    file_path = tmp_path / "invalid_products_type.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": "not_a_list",  # Строка вместо списка
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 0
    assert "products должен быть списком" in captured.out


def test_category_creation_error(tmp_path, capsys, monkeypatch):
    file_path = tmp_path / "category_error.json"
    data = [{"name": "Test Category", "description": "Desc", "products": []}]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    def mock_init(self, name, description, products):
        raise ValueError("Искусственная ошибка создания категории")

    monkeypatch.setattr(Category, "__init__", mock_init)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 0
    assert (
        "Ошибка при создании категории: Искусственная ошибка создания категории"
        in captured.out
    )


def test_invalid_products_type_strict(tmp_path, capsys):
    file_path = tmp_path / "strict_invalid_products_type.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": {"invalid": "type"},  # Словарь вместо списка
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 0
    assert (
        "products должен быть списком" in captured.out
        or "неверная структура данных категории" in captured.out
    )


def test_product_creation_error(tmp_path, capsys, monkeypatch):
    file_path = tmp_path / "product_error.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Valid Product",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                }
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    original_product_init = Product.__init__

    def mock_product_init(self, name, description, price, quantity):
        raise ValueError("Искусственная ошибка создания продукта")

    monkeypatch.setattr(Product, "__init__", mock_product_init)

    try:
        categories = load_data_from_json(file_path)
        captured = capsys.readouterr()

        assert len(categories) == 1
        assert len(categories[0].products) == 0
        assert (
            "Ошибка преобразования данных товара: Искусственная ошибка создания продукта"
            in captured.out
        )
    finally:
        monkeypatch.setattr(Product, "__init__", original_product_init)


def test_non_list_products_type(tmp_path, capsys):
    """Тестирует обработку случая, когда products не является списком"""
    file_path = tmp_path / "non_list_products.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": {"not": "a_list"},  # Словарь вместо списка
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 0
    assert "products должен быть списком" in captured.out


def test_category_creation_exception(tmp_path, capsys, monkeypatch):
    """Тестирует обработку исключения при создании категории"""
    file_path = tmp_path / "category_exception.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                }
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    original_init = Category.__init__

    def mock_init(self, name, description, products):
        raise RuntimeError("Искусственная ошибка создания категории")

    monkeypatch.setattr(Category, "__init__", mock_init)

    try:
        categories = load_data_from_json(file_path)
        captured = capsys.readouterr()

        assert len(categories) == 0
        assert (
            "Ошибка при создании категории: Искусственная ошибка создания категории"
            in captured.out
        )
    finally:
        monkeypatch.setattr(Category, "__init__", original_init)


def test_products_as_string_instead_of_list(tmp_path, capsys):
    """Тестирует случай, когда products является строкой вместо списка"""
    file_path = tmp_path / "products_string.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": "invalid_products_value",  # Строка вместо списка
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 0
    assert "products должен быть списком" in captured.out


def test_products_as_number_instead_of_list(tmp_path, capsys):
    """Тестирует случай, когда products является числом вместо списка"""
    file_path = tmp_path / "products_number.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": 123,  # Число вместо списка
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    categories = load_data_from_json(file_path)
    captured = capsys.readouterr()

    assert len(categories) == 0
    assert "products должен быть списком" in captured.out


def test_category_creation_with_invalid_data(tmp_path, capsys, monkeypatch):
    """Тестирует обработку исключения при создании категории с невалидными данными"""
    file_path = tmp_path / "category_invalid_data.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Valid Product",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                }
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    original_init = Category.__init__

    def mock_init(self, name, description, products):
        if "Invalid" in name:
            raise ValueError("Invalid category name")
        original_init(self, name, description, products)

    monkeypatch.setattr(Category, "__init__", mock_init)

    try:
        categories = load_data_from_json(file_path)
        assert len(categories) == 1

        invalid_data = [
            {"name": "Invalid Category", "description": "Desc", "products": []}
        ]

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(invalid_data, f)

        categories = load_data_from_json(file_path)
        captured = capsys.readouterr()

        assert len(categories) == 0
        assert "Ошибка при создании категории" in captured.out
    finally:
        monkeypatch.setattr(Category, "__init__", original_init)


def test_products_type_coverage(tmp_path, capsys):
    """Тест специально для покрытия всех веток проверки типа products"""
    test_cases = [
        ("string", "invalid_products"),
        ("number", 123),
        ("dict", {"key": "value"}),
        ("none", None),
        ("bool", True),
    ]

    for case_type, case_value in test_cases:
        file_path = tmp_path / f"products_{case_type}.json"
        data = [
            {
                "name": f"Test Category {case_type}",
                "description": "Desc",
                "products": case_value,
            }
        ]

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        categories = load_data_from_json(file_path)
        captured = capsys.readouterr()

        print(f"\nTest case {case_type}:")
        print(f"Input: {data}")
        print(f"Output: {categories}")
        print(f"Captured: {captured.out}")

        assert len(categories) == 0
        assert "products должен быть списком" in captured.out


def test_category_creation_failure(tmp_path, capsys, monkeypatch):
    """Тестирует полный сценарий с ошибкой создания категории"""
    file_path = tmp_path / "category_fail.json"
    data = [
        {
            "name": "Test Category",
            "description": "Desc",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                }
            ],
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    original_init = Category.__init__

    def mock_init(self, name, description, products):
        raise RuntimeError("Категория не может быть создана")

    monkeypatch.setattr(Category, "__init__", mock_init)

    try:
        categories = load_data_from_json(file_path)
        captured = capsys.readouterr()

        assert len(categories) == 0
        assert (
            "Ошибка при создании категории: Категория не может быть создана"
            in captured.out
        )
    finally:
        monkeypatch.setattr(Category, "__init__", original_init)


def test_full_error_handling(tmp_path, capsys, monkeypatch):
    """Комплексный тест обработки ошибок"""
    file_path = tmp_path / "full_test.json"
    data = [
        {
            "name": "Category 1",
            "description": "Desc",
            "products": "not_a_list",
        },
        {
            "name": "Category 2",
            "description": "Desc",
            "products": [
                {
                    "name": "Product 1",
                    "description": "Desc",
                    "price": 100,
                    "quantity": 5,
                }
            ],
        },
        {
            "name": "Category 3",
            "description": "Desc",
            "products": [],
        },
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    original_init = Category.__init__

    call_count = 0

    def mock_init(self, name, description, products):
        nonlocal call_count
        call_count += 1
        if name == "Category 3":
            raise ValueError("Специальная ошибка для теста")
        original_init(self, name, description, products)

    monkeypatch.setattr(Category, "__init__", mock_init)

    try:
        categories = load_data_from_json(file_path)
        captured = capsys.readouterr()

        assert len(categories) == 1
        assert categories[0].name == "Category 2"

        output = captured.out
        assert "products должен быть списком" in output
        assert "Специальная ошибка для теста" in output
        assert call_count == 2
    finally:
        monkeypatch.setattr(Category, "__init__", original_init)
