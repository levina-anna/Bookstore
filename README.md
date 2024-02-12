# Bookstore Management System

The Bookstore Management System is a web application designed to help bookstore owners efficiently manage their
inventory and improve customer experience. This system provides features for adding, updating, and categorizing books,
making it easier to keep track of available titles and offer a seamless shopping experience to customers.

![Screenshot](https://github.com/levina-anna/levina-anna.github.io/raw/main/images/Bookstore.png)

## API Integration

- **Product and Category Data**: The application fetches and displays products and categories from the API.

## Features

- **Category Filtering**: Allow customers to filter books by categories, making it effortless for them to find their
  preferred genre or author.

## Installation and Launch

```bash
git clone <repository-url>
cd <project-directory-name>
# Install dependencies
pip install -r requirements.txt
# Apply database migrations
python manage.py migrate
# Run the application
python manage.py runserver
```

## Technologies Used

- Bootstrap5
- Django 4.2.5
- Jinja2 3.1.2
- Python 3.11
- HTML
- CSS