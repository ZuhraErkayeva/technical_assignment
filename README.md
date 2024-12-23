
---

# Blog Project with JWT Authentication

This is a blog platform built using Django and Django Rest Framework with JWT (JSON Web Tokens) authentication. The platform allows users to register, log in, create blog posts, view posts based on their permissions, and perform other operations with role-based access control.

## Features

- **User Registration**: Allows users to sign up with a username, email, and password.
- **User Authentication**: Login and logout functionality using JWT tokens.
- **Blog Posts**: Create, view, and manage blog posts with various permissions.
- **Role-based Permissions**: Admins have full control over posts, while regular users can only create their own posts and view published ones.
- **Filtering and Sorting**: Blog posts can be filtered by published status and sorted by creation or update date.
- **Search Functionality**: Blog posts can be searched by title or content.

## Technologies Used

- **Backend**: Django 5.1.4, Django Rest Framework
- **Database**: PostgreSQL (recommended, but other options are supported)
- **Authentication**: JWT (JSON Web Tokens)
- **Frontend**: (Optional, not included in this project)
- **Libraries**: `rest_framework_simplejwt`, `django-allauth`, `dj_rest_auth`

## Requirements

- Python 3.10+
- Django 5.1.4
- Django Rest Framework 3.14+
- PostgreSQL (or other database backends)
- `pip install -r requirements.txt`

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/blog-project.git
cd blog-project
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Make sure PostgreSQL is installed and create a database:

```bash
psql -U postgres
CREATE DATABASE blog_db;
```

Update the `DATABASES` setting in `settings.py` to reflect your database configuration.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional, for Admin Access)

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Now you can visit the application at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication

1. **Register a User**
   - **POST** `/api/auth/register/`
   - Request Body:
     ```json
     {
       "username": "string",
       "email": "string",
       "password": "string"
     }
     ```
   - Response:
     ```json
     {
       "message": "User registered successfully",
       "user_id": "string"
     }
     ```

2. **Login**
   - **POST** `/api/auth/login/`
   - Request Body:
     ```json
     {
       "email": "string",
       "password": "string"
     }
     ```
   - Response:
     ```json
     {
       "access": "string (JWT)",
       "refresh": "string (JWT)",
       "user": {
         "id": "string",
         "username": "string",
         "email": "string",
         "role": "string"
       }
     }
     ```

3. **Logout**
   - **POST** `/api/auth/logout/`
   - Headers: `Authorization: Bearer <token>`
   - Response:
     ```json
     {
       "message": "Successfully logged out"
     }
     ```

### Blog Posts

1. **Create a Blog Post**
   - **POST** `/api/posts/`
   - Headers: `Authorization: Bearer <token>`
   - Request Body:
     ```json
     {
       "title": "string",
       "content": "string",
       "is_published": "boolean"
     }
     ```
   - Response:
     ```json
     {
       "id": "string",
       "title": "string",
       "content": "string",
       "author": "string (User id)",
       "created_at": "Date",
       "updated_at": "Date",
       "is_published": "boolean"
     }
     ```

2. **List All Blog Posts**
   - **GET** `/api/posts/`
   - Headers: `Authorization: Bearer <token>` (optional, for unpublished posts)
   - Query Parameters:
     - `page`: page number (default: 1)
     - `page_size`: number of posts per page (default: 10)
   - Response:
     ```json
     {
       "count": "number",
       "next": "string (URL)",
       "previous": "string (URL)",
       "results": [
         {
           "id": "string",
           "title": "string",
           "content": "string",
           "author": {
             "id": "string",
             "username": "string"
           },
           "created_at": "Date",
           "updated_at": "Date",
           "is_published": "boolean"
         }
       ]
     }
     ```

3. **Get a Single Blog Post**
   - **GET** `/api/posts/{id}/`
   - Headers: `Authorization: Bearer <token>` (optional, for unpublished posts)
   - Response:
     ```json
     {
       "id": "string",
       "title": "string",
       "content": "string",
       "author": {
         "id": "string",
         "username": "string"
       },
       "created_at": "Date",
       "updated_at": "Date",
       "is_published": "boolean"
     }
     ```

## Additional Features

- **Search**: You can search blog posts by title or content using the `search` query parameter on the `/api/posts/` endpoint.
  - Example: `/api/posts/?search=django`

- **Sorting**: You can sort blog posts by `created_at` or `updated_at` using the `ordering` query parameter.
  - Example: `/api/posts/?ordering=created_at`

- **Filtering**: Blog posts can be filtered by `is_published` status.
  - Example: `/api/posts/?is_published=true`

## Permissions

1. **Unauthenticated users** can only view published blog posts.
2. **Authenticated users** can create their own posts and view published posts.
3. **Authors** can edit or delete their own posts.
4. **Admins** can manage all posts, including editing, deleting, and changing publish status.

## JWT Implementation

- JWT tokens are used for authentication. The payload includes the user's ID and role.
- Tokens are valid for 24 hours, after which they need to be refreshed using the refresh token.
- Token refresh functionality is supported.

## Running Tests

Run the test suite to check the functionality of the API:

```bash
python manage.py test
```

---
