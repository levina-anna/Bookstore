import json


def get_cost() -> list:
    # Путь к файлу api.json
    file_path = r'D:\my_scripts\Bookstore\AdminPanel\DataTableApp\modules\cost\api.json'

    # Открываем файл и загружаем данные
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Возвращаем список книг из данных
    return data


def get_categories() -> dict:
    # Загружаем данные из categories.json
    with open(r'D:\my_scripts\Bookstore\AdminPanel\DataTableApp\modules\cost\categories.json', 'r', encoding='utf-8') as file:
        categories_data = json.load(file)

    return categories_data
