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
    print(f"products: {products}")
    categories_data = costs.get_categories()
    print(f"categories_data: {categories_data}")

    # Проверяем, есть ли параметр "category" в URL
    selected_category_id = request.GET.get('category')

    # Если выбрана категория, фильтруем товары по этой категории
    if selected_category_id:
        try:
            selected_category_id = int(selected_category_id)
            filtered_products = [
                product for product in products
                if product['category_id'] == selected_category_id
            ]
        except ValueError:
            # Если selected_category_id не может быть преобразован в int, выводим все продукты
            filtered_products = products
    else:
        # Если категория не выбрана, выводим все продукты
        filtered_products = products

    # Передаем данные в шаблон
    context = {
        'title': "Bookstore",
        'products': filtered_products,
        'categories': categories_data,
        'selected_category': int(selected_category_id) if selected_category_id else None,
    }

    return render(request, 'DataTableApp/cost_table.html', context)
