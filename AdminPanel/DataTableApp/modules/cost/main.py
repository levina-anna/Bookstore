import requests


class APIClient:
    """
    Handles interactions with the external API.
    """

    @staticmethod
    def get_cost(api_url) -> list:
        """
        Fetches product data from the given API URL.

        Args:
            api_url: The API endpoint URL.

        Returns:
            A list of product data if the request is successful, otherwise an empty list.
        """
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error getting data from API: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"An error occurred while connecting to the API: {e}")
            return []

    @staticmethod
    def get_categories(api_url) -> list:
        """
        Fetches unique category data from the given API URL.

        Args:
            api_url: The API endpoint URL.

        Returns:
            A list of unique categories with their IDs and names if the request is successful,
            otherwise an empty list.
        """
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                categories = {
                    item['category_id']: item['category_name']
                    for item in data
                }
                return [{'category_id': k, 'category_name': v} for k, v in categories.items()]
            else:
                print(f"Error getting data from API: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"An error occurred while connecting to the API: {e}")
            return []
