# MyLibrary

**MyLibrary** is a Django-based personal book-tracking web application.

---

## Design Decisions

- **User Authentication**: Used Django’s built-in `User` model and authentication views for login, logout, and registration.
- **User-Scoped Data**: Books are tied to the user who added them. Other users cannot see or modify those books.
- **Class-Based Views**: Used Django's generic class-based views for clean and maintainable CRUD functionality.
- **Template Inheritance**: Implemented consistent layout via `base.html`.

---

### Setting up the Project

`git clone https://github.com/your-username/MyLibrary.git
cd MyLibrary`

`python3 -m venv venv
source venv/bin/activate`  

`pip install django`

`python3 manage.py makemigrations
python3 manage.py migrate`

### Run the Development Server

`python manage.py runserver`

###  Authentication Pages

- **Register**: `/register/`
- **Login**: `/login/`
- **Logout (confirmation)**: `/logout/confirm/`

---

###  Book Management Features

- `/` – View your books
- `/add/` – Add a new book
- `/<book_id>/` – View book details
- `/<book_id>/edit/` – Edit an existing book
- `/<book_id>/delete/` – Delete a book

> Each user can only see and manage the books they’ve added.
