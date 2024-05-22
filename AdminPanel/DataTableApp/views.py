from django.shortcuts import render
from config import api_domain


def index(request):
    # Pass data to template
    context = {
        'title': "Main",
    }
    return render(request, 'DataTableApp/index.html', context)


def cost_table(request):
    from .modules.cost import main as costs

    # API URL from which we want to receive data
    api_url = f"{api_domain}/products_and_categories"

    # Receive data about products and categories
    products = costs.get_cost(api_url)
    # print(f"products: {products}")
    categories_data = costs.get_categories(api_url)
    # print(f"categories_data: {categories_data}")

    # Check if there is a "category" parameter in the URL
    selected_category_id = request.GET.get('category')
    print(f"selected_category_id: {selected_category_id}")

    # If a category is selected, filter products by this category
    if selected_category_id:
        try:
            selected_category_id = int(selected_category_id)
            filtered_products = [
                product for product in products
                if product['category_id'] == selected_category_id
            ]
        except ValueError:
            # If selected_category_id cannot be converted to int, print all products
            filtered_products = products
    else:
        # If the category is not selected, display all products
        filtered_products = products

    # Pass data to template
    context = {
        'title': "Bookstore",
        'products': filtered_products,
        'categories': categories_data,
        'selected_category': int(selected_category_id) if selected_category_id else None,
    }

    return render(request, 'DataTableApp/cost_table.html', context)
