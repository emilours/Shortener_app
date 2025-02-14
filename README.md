
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
    git clone git@github.com:emilours/Shortener_app.git Shortener_app_project
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
  This is the default interactive API documentation interface provided by FastAPI. You can access it by visiting the following URL in your browser:


Swagger UI allows you to explore and test all available endpoints directly from the browser. It provides an intuitive, user-friendly interface to interact with the API.

2. **ReDoc UI: http://127.0.0.1:8000/redoc**  
ReDoc is another interface for API documentation, which provides a more structured and detailed view of the API. You can access it at:


ReDoc focuses on presenting the API documentation in a clean and organized format, making it easier to read through the details of each endpoint.

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
