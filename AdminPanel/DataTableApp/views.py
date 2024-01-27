from django.shortcuts import render


def index(request):
    # Передаем данные в шаблон
    context = {
        'title': "Main",
    }
    return render(request, 'DataTableApp/index.html', context)


def cost_table(request):
    from .modules.cost import main as costs

    # Получаем данные о товарах и категориях
    products = costs.get_cost()
    # print(f"products: {products}")
    categories_data = costs.get_categories()
    # print(f"categories_data: {categories_data}")

    # Проверяем, есть ли параметр "category" в URL
    selected_category_id = request.GET.get('category')

    # Фильтруем товары по выбранной категории
    if selected_category_id:
        filtered_products = [
            product for product in products
            if any(
                product['id'] == prod['id']
                for cat in categories_data['categories']
                if cat['category_id'] == int(selected_category_id)
                for prod in cat['products']
            )
        ]
    else:
        filtered_products = products

    # Передаем данные в шаблон
    context = {
        'title': "Bookstore",
        'products': filtered_products,
        'categories': categories_data['categories'],
        'selected_category': int(selected_category_id) if selected_category_id else None,
    }

    return render(request, 'DataTableApp/cost_table.html', context)
