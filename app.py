from flask import Flask, render_template, request, redirect, url_for
import json
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем значение переменной
url_api = os.getenv("SITE_URL_API")
categories_api = os.getenv("CATEGORIES_API")

@app.route('/cost_table', methods=['GET', 'POST'])
def cost_table():

    # Получаем текущего пользователя
    user = request.user

    from .modules.cost import main as costs

    # Получаем список цен на продукты
    data = costs.get_cost()

    # Получаем категории товаров
    sections = costs.get_sections()

    # Получаем выбранную категорию из параметра URL
    selected_category = request.GET.get('category')

    # Установка дефолтного значения, если selected_category равно None
    selected_category = selected_category or 'В панировке'

    # Ищем идентификатор категории по её имени в словаре sections
    selected_section_id = None
    for section_id, section_data in sections.items():
        if section_data.get('name') == selected_category:
            selected_section_id = section_id
            break

    offers_ids = costs.get_products_by_sections(selected_section_id)
    filtered_products = costs.filter_products_by_xml_id(data, offers_ids)

    if request.method == 'POST':
        put_products_costs = []

        # Обработка изменений в таблице
        for row in data:
            price = request.POST.get(f'price_{row["ID"]}')
            price_per_kg = request.POST.get(f'price_per_kg_{row["ID"]}')
            old_price = request.POST.get(f'old_price_{row["ID"]}')
            hidden_price = request.POST.get(f'hidden_price_{row["ID"]}')
            hidden_price_per_kg = request.POST.get(f'hidden_price_per_kg_{row["ID"]}')
            hidden_old_price = request.POST.get(f'hidden_old_price_{row["ID"]}')

            if hidden_price != price \
                    or hidden_price_per_kg != price_per_kg \
                    or hidden_old_price != old_price:
                put_products_costs.append({"ID": int(row["ID"]),
                                           'PRICE_PER_KG': price_per_kg,
                                           'OLD_PRICE': old_price,
                                           'PRICE': price})

        # Обновление внешнего API после сохранения данных в базе
        costs.put_cost(products=put_products_costs)

        # Переход на главную страницу
        return redirect('cost_table')

    context = {
        'data': filtered_products,
        'sections': sections,
        'selected_category': selected_category,
    }

    return render_template('cost_table.html', data=filtered_products, sections=sections, selected_category=selected_category)


if __name__ == '__main__':
    app.run(debug=True)