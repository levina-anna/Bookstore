from django.shortcuts import render


def index(request):
    return render(request, 'DataTableApp/index.html')


def cost_table(request):
    from .modules.cost import main as costs

    # Получаем данные о товарах и категориях
    products = costs.get_cost()
    categories_data = costs.get_categories()

    # Проверяем, есть ли параметр "category" в URL
    selected_category_id = request.GET.get('category')

    # Фильтруем товары по выбранной категории
    if selected_category_id:
        filtered_products = [product for product in products if any(product['id'] in p['products'] for p in categories_data['categories'] if p['category_id'] == int(selected_category_id))]
    else:
        filtered_products = products

    # Передаем данные в шаблон
    context = {
        'products': filtered_products,
        'categories': categories_data['categories'],
        'selected_category': int(selected_category_id) if selected_category_id else None,
    }

    return render(request, 'DataTableApp/cost_table.html', context)