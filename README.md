# book_management_system
System for library management


## Purpose of this project
* Develop a complete REST API with the connection using token authorization
* Write some unit tests to test the source code

## Table of Content

* [Requirements](#requirements)
* [Schema](#schema)
* [API](#api)

## Local setup

1. Must have Python 3 installed and running
1. Clone the repo and cd into repo
1. Create a virtual environment: `python -m venv venv`
1. Go into your virtual environment: `venv/Script/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`
1. Run the app: `python manage.py runserver`
1. View the API at `localhost:8000` and the admin interface at `localhost:8000/admin`

## Requirements

* Develop REST API endpoints which allows to create, modify and delete authors.
* Develop REST API endpoints which allows to create, modify and delete books.
* Develop REST API endpoints which allows to manage the book in stock and out of stock.
* Create an endpoint to retrieve 1book
* Managing authentication (Token Authentication)

## Schema
<img width="557" alt="image" src="https://user-images.githubusercontent.com/77486898/208766738-476c702c-7100-4880-8f1b-d1bad1131b27.png">

## API

**/books/list/**

* get 
* post

**books/<int:pk>**

* get
* put
* delete

**/authors/list/**

* get
* post

**authors/<int:pk>**

* get
* put
* delete


**borrowed_books/list/**

* get


**borrowed_books/<int:pk>**
* get
* put
* delete


*example response:*

```json
[
    {
        "isbn": 1,
        "title": "Building Microservices: Designing Fine-Grained Systems",
        "keywords": "microservices",
        "status": "B",
        "author": 5,
        "categorie": 6
    },
    {
        "isbn": 2,
        "title": "Microeconomics: Policy and Practice",
        "keywords": "Macro, economics",
        "status": "B",
        "author": 4,
        "categorie": 2
    },
    {
        "isbn": 3,
        "title": "Macroeconomics: Policy and Practice",
        "keywords": "Macro, economics",
        "status": "A",
        "author": 4,
        "categorie": 2
    },
    {
        "isbn": 4,
        "title": "Principle of Marketing",
        "keywords": "marketing",
        "status": "A",
        "author": 1,
        "categorie": 2
    },
    {
        "isbn": 5,
        "title": "Notre Dame de Paris",
        "keywords": "story",
        "status": "A",
        "author": 3,
        "categorie": 7
    },
    {
        "isbn": 6,
        "title": "Connan",
        "keywords": "detective",
        "status": "A",
        "author": 8,
        "categorie": 5
    }
]
```
