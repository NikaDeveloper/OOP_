# Online Store Categories and Products

Простая программа для управления категориями и товарами интернет-магазина.

## Что делает

1. **Товары (Product)**
   - Хранит информацию о товарах: название, описание, цена и количество
   - Пример: "Телевизор", "4K QLED", 89990 руб., 10 шт.

2. **Категории (Category)**
   - Группирует товары по категориям
   - Автоматически считает:
     - Общее количество категорий
     - Общее количество товаров во всех категориях
   - Пример: "Электроника" → [Телевизор, Смартфон]

## Установка
Клонируйте репозиторий:

[git clone] (-> https://github.com/NikaDeveloper/OOP_<-)
### Перейдите в директорию проекта:
cd OOP_

### Установите зависимости с помощью Poetry:
poetry install

(Убедитесь, что у вас установлен Poetry)

### Запуск программы
Выполните в терминале: python3 main.py

### Тестирование
Для запуска тестов выполните: pytest
