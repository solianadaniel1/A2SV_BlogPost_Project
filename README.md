# Blog Platform API

This is a blog platform API built with Django and Django Rest Framework. The API allows users to create, read, update, and delete blog posts. Only the owner of a blog post can update or delete it, while all users (authenticated and unauthenticated) can view the blog posts.

## Technologies Used
- **Python:** Backend programming language.
- **Django:** Framework for rapid development.
- **Django Rest Framework:** Toolkit for building APIs.
- **SQLite:** Default database for local development (can be replaced with other databases).
- **JWT Authentication:** For secure user authentication.

## Features

- **User Authentication**: Users must be authenticated to create, update, or delete blog posts.
- **Blog Posts**: Users can create blog posts, which are associated with their user account.
- **Permissions**:
  - **Read**: All users (authenticated and unauthenticated) can view blog posts.
  - **Write**: Only authenticated users can create, update, or delete their own blog posts.
- **Custom Permissions**: Custom permissions restrict access to blog modification based on ownership.

## Technologies Used

- **Django**: Web framework for rapid development.
- **Django Rest Framework**: Toolkit for building Web APIs.
- **SQLite**: Default database for storing blog data (can be replaced with other databases like PostgreSQL, MySQL, etc.).
- **Python**: Programming language used for the backend logic.


## Setup Instructions

Follow these steps to set up the development environment:

1. **Create a virtual environment**:
   In your project folder, run the following command to create a virtual environment:
   ```bash
   python -m venv env
   venv\Scripts\activate

2. **Install the Django Rest Framework**:
   In your project folder, run the following command to install DRF:
   ```bash
   pip install djangorestframework 

3. **Clone the Repository**:
   ```bash
    git clone https://github.com/yourusername/blog-platform.git
    cd blog-platform

4. **Package for filtering**: 
   #### * Filtering of Querysets
   In your project folder, run the following command to install to allows users to filter querysets:
   ```bash
   pip install django-filter

5. **Package for Mysql**: 
   #### * Database Connector for MySQL
   In your project folder, run the following command used in Python database 
   connector to MySQL:
   ```bash
   pip install mysqlclient


6. **Create a new Django project**:
   Create a django project
   ```bash
   django-admin startproject product_api

7. **To Generate the requirement.txt file**:
   ```bash
  pip freeze > requirements.txt

7. **Run Database Migrations**:
   ```bash
    python manage.py migrate

8. **Run Server**:
   ```bash
    python manage.py runserver


