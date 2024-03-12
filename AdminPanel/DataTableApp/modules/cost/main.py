import requests
from config import api_domain


def get_cost() -> list:
    # URL API, с которого мы хотим получать данные
    api_url = f"{api_domain}/products_and_categories"

    # Отправляем GET-запрос к API
    response = requests.get(api_url)

    # Проверяем, что запрос прошёл успешно
    if response.status_code == 200:
        # Преобразуем ответ API в JSON
        data = response.json()
        # Возвращаем данные
        return data
    else:
        # Обрабатываем возможные ошибки
        print(f"Ошибка при получении данных из API: {response.status_code}")
        return []


def get_categories() -> list:
    # URL API, с которого получаем данные
    api_url = "http://127.0.0.1:8002/products_and_categories"

    try:
        # Отправляем GET-запрос к API
        response = requests.get(api_url)

        # Проверяем, что запрос прошёл успешно
        if response.status_code == 200:
            # Преобразуем ответ API в JSON
            data = response.json()

            # Создаем словарь для отслеживания уникальных категорий
            categories = {}
            for item in data:
                # Добавляем категорию в словарь, если ее там еще нет
                cat_id = item['category_id']
                categories[cat_id] = item['category_name']

            # Возвращаем список уникальных категорий
            unique_categories = [{'category_id': k, 'category_name': v} for k, v in categories.items()]
            return unique_categories
        else:
            # В случае ошибки возвращаем пустой список
            print(f"Ошибка при получении данных из API: {response.status_code}")
            return []
    except requests.RequestException as e:
        # Логируем исключение, если что-то пошло не так
        print(f"Произошла ошибка при подключении к API: {e}")
        return []
