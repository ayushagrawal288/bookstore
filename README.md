Book Store
===========

Problem Statement
-----------------
An online bookstore API. Following are the steps -
- Develop endpoints to create, read, update, delete and search (generic search) books in the store.
- Design an endpoint to upload books from CSV/excel file one by one or in bulk

## Heroku link -> https://bookstore288.herokuapp.com/


Getting Started
---------------

- Change directory into your newly created project.

    cd bookstore/

- Create a Python virtual environment.

    virtualenv -p python3 venv
    source venv/bin/activate

- Upgrade packaging tools.

    pip install -r requirements.txt

- Run your project.

    python manage.py runserver

Endpoints
---------
Book:   
- List(get):
    /book/list/ 
    /book/list/?search= 
  
- Create(post):  
    /book/create/ 
    body = { 
        "title": "",  
        "isbn": "",  
        "price": 0.0,  
        "author": ["", ""],  
        "publisher": "",  
        "edition": "",  
        "date_published": "2000-01-15" 
    }
  
- Get Book(get):  
    /book/{id}/ 
  
- Update(put):  
    /book/{id}/edit/ 
    Must contain attr = title 
  
- Delete(delete):  
    /book/<id>/delete 
  
- Upload Csv(post):  
    /book/upload-csv/ 
    Must contain attr = title, author, publisher 
