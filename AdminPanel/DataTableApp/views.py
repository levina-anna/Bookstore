from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from config import api_domain
from .modules.cost.main import APIClient


class IndexView(View):
    """
    Handles rendering of the main page.
    """
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handles GET requests for the main page.

        Args:
            request: The HTTP request object.

        Returns:
            Rendered template for the main page.
        """
        context = {
            'title': "Main",
        }
        return render(request, 'DataTableApp/index.html', context)


class CostTableView(View):
    """
    Handles rendering of the cost table page with product and category data.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handles GET requests for the cost table page.

        Args:
            request: The HTTP request object.

        Returns:
            Rendered template for the cost table page.
        """
        api_url = f"{api_domain}/products_and_categories"

        # Fetch products and categories
        products = APIClient.get_cost(api_url)
        categories_data = APIClient.get_categories(api_url)

        # Get selected category ID from request
        selected_category_id = request.GET.get('category')

        if selected_category_id:
            try:
                selected_category_id = int(selected_category_id)
                filtered_products = [
                    product for product in products
                    if product['category_id'] == selected_category_id
                ]
            except ValueError:
                filtered_products = products
        else:
            filtered_products = products

        context = {
            'title': "Bookstore",
            'products': filtered_products,
            'categories': categories_data,
            'selected_category': int(selected_category_id) if selected_category_id else None,
        }

        return render(request, 'DataTableApp/cost_table.html', context)
