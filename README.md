# SimpleDjangoApplication

## Overview
This is a Django web application for browsing and managing a collection of quotes and their respective authors. The application allows users to view quotes, search for quotes by tags, and view detailed information about authors. Registered users can add new authors and quotes to the database.

## Features
- **User Authentication**: Users can register and log in to the application. Only authenticated users can add new authors and quotes.
- **Author Management**: Users can view a list of authors and detailed information about each author.
- **Quote Management**: Users can view a list of quotes, and these can be filtered by tags.
- **Add Quotes and Authors**: Registered users can add new quotes and authors to the database.
- **Tag-Based Search**: Users can search for quotes based on specific tags.
- **Pagination**: The quotes list is paginated to enhance user experience and performance.

## Technologies
- **Frontend**: HTML, CSS 
- **Backend**: Python, Django
- **Database**: PostgreSQL, MongoDB

## Setup and Installation
1. **Run Docker Engine via opening Docker Desktop.**

2. **Activate Virtual Environment:**
   ```
    poetry shell
   ```
3. **Fill the Database (MongoDB)**
    ```
    cd django_core
    python -m mongo.seeds
    ```
4. **Run Docker-Compose File (PostgreSQL DB Creation)**
    ```
    docker-compose -f docker-compose.yaml up --force-recreate
    ```

5. **Make the Tables in Database and fill Them**
   ```
   python manage.py makemigrations
   python manage.py migrate
   python -m mongo.migration
   ```

6. **Create an Admin User**
   ```
   python manage.py createsuperuser
   ```

7. **Run the Server**
   ```
   python manage.py runserver
   ```

## Usage
- Visit `http://localhost:8000` in your browser to access the application.
- Register a new user account to add new authors and quotes.
