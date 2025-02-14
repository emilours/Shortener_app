
# URL Shortener with FastAPI

This project demonstrates how to build a simple URL shortener using **FastAPI**, **SQLAlchemy**, and **SQLite**. The primary goal is to create a REST API that allows users to shorten URLs and retrieve the original URL through a unique key. One data point of the response body is how often your shortened URL was clicked.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation and Setup](#installation-and-setup)
3. [Running the Application](#running-the-application)
4. [API Endpoints](#api-endpoints)
5. [Database Setup](#database-setup)
6. [Testing the Application](#testing-the-application)
7. [Additional Information](#additional-information)

---


## Prerequisites
Make sure you have the following installed on your system:
- **Python 3.7+**
- **pip** (Python's package installer)
- **Git** (for version control)

---
## Installation

1. **Prepare Your Environment**  

   Clone the project repository from GitHub:

   ```bash
    git clone git@github.com:emilours/Shortener_app.git
    ```

    Create a virtual environment and activate it:

   ```bash
    python -m venv venv
    source venv/bin/activate 
    # On Windows, use `venv\Scripts\activate`

    ```

    Install Dependencies:

   ```bash
    pip install -r requirements.txt
    # to check installed dependences: python -m pip freeze 
    ```

    Create .env and  define file:

   ```bash
    touch .env
    #file to be filled with values:
    # Environment name: Development, Production, etc.
    ENV_NAME="Development"

    # Base URL for the application (used in the API and redirects)
    BASE_URL="http://127.0.0.1:8000"

    # Database connection URL
    # Example for SQLite (local database)
    DB_URL="sqlite:///./shortener.db"

    # Example for PostgreSQL (production setup)
    # DB_URL="postgresql://user:password@localhost/shortener_db"

    ```

    This will start the development server at http://127.0.0.1:8000.

    ```bash
    uvicorn shortener_app.main:app --reload
    ```

## Access the API Documentation

FastAPI automatically generates interactive API documentation for your application, which you can access through two different UI options:

1. **Swagger UI : http://127.0.0.1:8000/docs**
  This is the default interactive API documentation interface provided by FastAPI.

Swagger UI allows you to explore and test all available endpoints directly from the browser.

2. **ReDoc UI: http://127.0.0.1:8000/redoc**  
ReDoc is another interface for API documentation, which provides a more structured and detailed view of the API.

These interfaces are generated dynamically and can be accessed once your application is running locally.

## Project Structure

The project is organized as follows:


- **`.env`**: Stores environment variables such as database credentials, application mode (Development/Production), and base URL.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`venv/`**: Contains the virtual environment. This folder should not be pushed to version control (it is in `.gitignore`).
- **`shortener_app/`**: The folder containing the source code for the FastAPI application.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`main.py`**: The entry point for the FastAPI application, where routing and request handling occurs.
  - **`database.py`**: Manages the database setup and connection configuration.
  - **`models.py`**: Defines the SQLAlchemy models for the database, representing the structure of the tables.
  - **`schemas.py`**: Defines the Pydantic models for request validation and response serialization.
  - **`crud.py`**: Contains the functions for creating, reading, updating, and deleting (CRUD) records in the database.
  - **`keygen.py`**: Includes utility functions for generating secure keys for the shortened URLs.
  - **`config.py`**: Contains configuration settings for the application, typically loaded from `.env`.

## FastAPI Documentation

FastAPI automatically generates an interactive documentation interface for the API to explore the endpoints. Below are descriptions of the different sections available in the FastAPI documentation UI, along with screenshots of each.

### 1. General Documentation Page

The **general documentation page** provides an overview of all the available API endpoints. You can find the list of routes with their HTTP methods, descriptions, and any required request parameters.

**URL:**  
`http://127.0.0.1:8000/docs`

![General Documentation](assets/DocsView.png)

---

### 2. POST `/url` Endpoint

The **POST `/url`** endpoint allows users to shorten a given URL. On the documentation page, you can see the required request body (target URL) and execute the endpoint directly from the UI.

**Description:**  
This endpoint takes a URL in the request body and returns a shortened URL with additional information like the unique key and secret key.

**URL:**  
`http://127.0.0.1:8000/docs#/default/create_url_url_post`

![POST URL Endpoint](assets/POST.png)

---

### 3. GET `/admin/{secret_key}` - Admin Info (Check Clicks)

The **GET `/admin/{secret_key}`** endpoint provides administrative information about a shortened URL, including the number of times it has been clicked.

**Description:**  
By entering the secret key of the shortened URL, you can view stats such as the target URL and the total number of clicks.

**URL:**  
`http://127.0.0.1:8000/docs#/default/get_url_info_admin_secret_key_get`

![Admin Info](assets/ClickInfo.png)

---

### 4. DELETE `/admin/{secret_key}` - Delete URL

The **DELETE `/admin/{secret_key}`** endpoint allows you to deactivate a shortened URL.

**Description:**  
This endpoint requires the secret key of the shortened URL. Once entered, it will remove the URL from the database.

**URL:**  
`http://127.0.0.1:8000/docs#/default/delete_url_admin_secret_key_delete`

![Delete URL](assets/DeactivateURL.png)


## Documentation

[Documentation](https://linktodocumentation)

## Sources

The following resources were used to build and understand the implementation of this project:

1. **Real Python - Build a Python URL Shortener with FastAPI**  
   A detailed tutorial on building a URL shortener using FastAPI.  
   [Read the tutorial here](https://realpython.com/build-a-python-url-shortener-with-fastapi/)

2. **FastAPI Documentation**  
   The official FastAPI documentation  
   [Explore the documentation here](https://fastapi.tiangolo.com/)

3. **Pydantic Documentation**  
   The official documentation for Pydantic  
   [Read the documentation here](https://docs.pydantic.dev/)

4. **SQLAlchemy Documentation**  
   The official SQLAlchemy documentation  
   [Check out the documentation here](https://www.sqlalchemy.org/)
