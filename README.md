
# Multilingual CMS


This is a multilingual content management system (CMS) built with Django and Django REST Framework (DRF). It supports CRUD operations for managing content on the Home Page and exposes an API for retrieving content in multiple languages.


Table of Contents

    1. Setup Instructions

    2. API Endpoints Documentation

    3. Steps to Test the Application

Setup Instructions

1. Clone the Repository

        git clone https://github.com/Arman170616/Project_1BT/
        cd multilingual-cms

2. Install Dependencies

        pip install -r requirements.txt

3. Set Up the Database
Run migrations to create the database schema:

    python manage.py migrate


4. Create a Superuser
Create an admin account to access the admin panel and generate tokens:

    python manage.py createsuperuser


5. Run the Development Server
Start the Django development server:

    python manage.py runserver

The application will be available at http://localhost:8000/.

API Endpoints Documentation
1. Token Generation
URL: /api/token/

Method: POST

Description: Generate access and refresh tokens for authentication.

Request Body:

    {
        "username": "admin123",
        "password": "admin123"
    }

Response:

    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODc3MjE1MSwiaWF0IjoxNzM4Njg1NzUxLCJqdGkiOiJiOTk5NWMwNGVhOTY0Mzc0OTAzZTFhNzYxYTI5ZTNlZCIsInVzZXJfaWQiOjJ9.mjx-JXkBvJfX1gtUua0zar-ZWmQqn7dhe6aBUUTsAEE",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4Njg5MzUxLCJpYXQiOjE3Mzg2ODU3NTEsImp0aSI6IjA1MGQwZGIzYTc3NTRmZWU5OGFkMDFlMmFlZmI5Y2E5IiwidXNlcl9pZCI6Mn0.bS3zR0_7oH_Fzpb1JIuxfH-82CAa9PsV2bNNYil5CI4"
    }



2. List and Create Home Page Content
URL: api/home/

Method: GET (List) or POST (Create)

Query Parameters:

page_name: Filter by page name (e.g., home).

language: Filter by language (e.g., en or fr).

Example Request (List):

    curl -X GET "http://localhost:8000/api/home/?page_name=home&language=en" -H "Authorization: Bearer <access_token>"

Example Request (Create):

    curl -X POST "http://localhost:8000/api/home/" \
        -H "Authorization: Bearer <access_token>" \
        -H "Content-Type: application/json" \
        -d '{
            "page_name": "home",
            "title_en": "Welcome to Our Website",
            "title_fr": "Bienvenue sur notre site web",
            "description_en": "This is the home page description in English.",
            "description_fr": "Ceci est la description de la page d'accueil en français."
            }'


3. Retrieve, Update, and Delete Home Page Content
URL: /api/home/<id>/

Method: GET (Retrieve), PUT (Update), or DELETE (Delete)

Example Request (Retrieve):

    curl -X GET "http://localhost:8000/api/home/1/" -H "Authorization: Bearer <access_token>"

Example Request (Update):

    curl -X PUT "http://localhost:8000/api/home/1/" \
        -H "Authorization: Bearer <access_token>" \
        -H "Content-Type: application/json" \
        -d '{
            "page_name": "home",
            "title_en": "Updated Welcome Message",
            "title_fr": "Message de bienvenue mis à jour",
            "description_en": "Updated description in English.",
            "description_fr": "Description mise à jour en français."
            }'

Example Request (Delete):

    curl -X DELETE "http://localhost:8000/api/home/1/" -H "Authorization: Bearer <access_token>"

Support
For any issues or questions, please whatsapp me: +8801811302984
