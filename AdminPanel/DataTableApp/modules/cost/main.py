import requests


def get_cost(api_url) -> list:
    # Send a GET request to the API
    response = requests.get(api_url)
    try:
        # Check that the request was successful
        if response.status_code == 200:
            # Convert the API response to JSON
            data = response.json()
            # Return data
            return data
        else:
            # Handle possible errors
            print(f"Error getting data from API: {response.status_code}")
            return []
    except requests.RequestException as e:
        # Log an exception if it was not possible to connect to the API
        print(f"An error occurred while connecting to the API: {e}")
        return []


def get_categories(api_url) -> list:
    # Send a GET request to the API
    response = requests.get(api_url)
    try:
        # Check that the request was successful
        if response.status_code == 200:
            # Convert the API response to JSON
            data = response.json()

            # Create a dictionary to track unique categories
            categories = {}
            for item in data:
                # Add a category to the dictionary if it is not there yet
                cat_id = item['category_id']
                categories[cat_id] = item['category_name']

            # Return a list of unique categories
            unique_categories = [{'category_id': k, 'category_name': v} for k, v in categories.items()]
            return unique_categories
        else:
            # In case of error, return an empty list
            print(f"Error getting data from API: {response.status_code}")
            return []
    except requests.RequestException as e:
        # Log an exception if it was not possible to connect to the API
        print(f"An error occurred while connecting to the API: {e}")
        return []
