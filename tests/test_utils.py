import json
from src.utils import load_data_from_json
from src.product import Product
from src.category import Category


def test_load_valid_json(temp_json_file):
    categories = load_data_from_json(temp_json_file)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Тестовая категория"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Тестовый товар"


def test_file_not_found():
    result = load_data_from_json("nonexistent_file.json")
    assert result == []


def test_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("{invalid json}")

    result = load_data_from_json(file_path)
    assert result == []


def test_empty_json(tmp_path):
    file_path = tmp_path / "empty.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("")

    result = load_data_from_json(file_path)
    assert result == []


def test_not_list_json(tmp_path):
    file_path = tmp_path / "not_list.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"key": "value"}, f)

    result = load_data_from_json(file_path)
    assert result == []


def test_empty_list_json(tmp_path):
    file_path = tmp_path / "empty_list.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([], f)

    result = load_data_from_json(file_path)
    assert result == []


def test_category_counters(temp_json_file):
    Category.number_of_categories = 0
    Category.number_of_products = 0

    categories = load_data_from_json(temp_json_file)

    assert Category.number_of_categories == 1
    assert Category.number_of_products == 1
