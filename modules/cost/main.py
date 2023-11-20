import json
import requests
import os
from dotenv import load_dotenv


# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем значение переменной
url_api = os.getenv("SITE_URL_API")
categories_api = os.getenv("CATEGORIES_API")


# Получаем товары с ценами
def get_cost() -> list:

    config = {
        "SITE": {
            "url_api": url_api
        }
    }

    url = config["SITE"]["url_api"] + "catalog/product/priceList.php"
    payload = json.dumps({"token": "jhsjdfgby7324hbjsdfhyg3478hd6t3"})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ZGV2OjEyMzQ1Ng==',
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    return response["list"]


# Меняем цены у товаров
def put_cost(products) -> dict:

    config = {
        "SITE": {
            "url_api": url_api
        }
    }

    url_put_date = config["SITE"]["url_api"] + "catalog/product/priceUpdate.php"

    payload = json.dumps({
        "token": "jhsjdfgby7324hbjsdfhyg3478hd6t3",
        "products": products})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ZGV2OjEyMzQ1Ng==',
    }

    response = requests.post(url_put_date, headers=headers, data=payload, auth=("dev", 123456)).json()

    if response.get("success"):
        print("Данные успешно обновлены во внешнем API.")
    else:
        print(f"Не удалось обновить данные во внешнем API. Ответ: {response}")

    return response


# Получаем категории для отображения в "Фильтр по разделам"
def get_sections() -> dict:
    url = categories_api
    response = requests.get(url).json()
    return response.get("sections", {})


# Получаем продукты по категории
def get_products_by_sections(selected_section_id: str) -> list:
    url = categories_api
    response = requests.get(url).json()

    # Преобразуем selected_section_id в строку, чтобы сравнение прошло успешно
    selected_section_id = str(selected_section_id)

    # Получаем все товары из "products" с указанным section_id
    products_ids = [product_id for product_id, product_info in response.get("products", {}).items()
                    if str(product_info.get("section_id")) == selected_section_id]

    # Получаем все товары из "offers" с указанным section_id
    offers_ids = [offer_id for offer_id, offer_info in response.get("offers", {}).items()
                  if str(offer_info.get("parent_id")) in products_ids]

    return offers_ids


# Получаем товары по XML_ID
def filter_products_by_xml_id(products, xml_ids):
    filtered_products = [product for product in products if str(product['XML_ID']) in xml_ids]
    return filtered_products
