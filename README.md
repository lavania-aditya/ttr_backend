# Tiny Town Creations Backend

Production-ready Django REST API backend for Tiny Town Creations product catalogue.

## Tech Stack

- Django + Django REST Framework
- OpenAPI schema + Swagger UI (`drf-spectacular`)
- PostgreSQL (via `DATABASE_URL`)
- JWT auth (`djangorestframework-simplejwt`)
- Cloudinary image upload
- Render deployment (`gunicorn`, `whitenoise`)

## Project Overview

Tiny Town Creations Backend is a Django REST API for managing a product catalogue, categories, admin authentication, image uploads, and customer inquiries.

- `products`: public listing/detail APIs plus admin-managed create, update, and delete flows
- `categories`: public listing plus admin-managed create and delete flows
- `admins`: JWT login for admin users and authenticated image upload support
- `inquiries`: customer inquiry submission tied to products

## Project Structure

- `config/` Django project settings and root URLs
- `apps/products/` Product model and APIs
- `apps/categories/` Category model and APIs
- `apps/admins/` Custom admin user + login/upload APIs
- `apps/inquiries/` Inquiry model and create API
- `utils/cloudinary_upload.py` Cloudinary helper

## Environment Setup

1. Create a virtual environment and activate it.

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
4. Update `.env` values.

Required environment variables:

- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`
- `CORS_ALLOWED_ORIGINS`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

## Run Locally

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Documentation

After starting the server locally, Swagger UI is available at:

- [http://127.0.0.1:8000/api/docs/swagger/](http://127.0.0.1:8000/api/docs/swagger/)

Raw OpenAPI schema:

- [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

## API Endpoints

Public:

- `GET /api/products`
- `GET /api/products/{slug}`
- `GET /api/categories`

Admin-authenticated:

- `POST /api/admin/login`
- `POST /api/products`
- `PUT /api/products/{id}`
- `DELETE /api/products/{id}`
- `POST /api/categories`
- `DELETE /api/categories/{id}`
- `POST /api/upload-image`

Additional:

- `POST /api/inquiries`

## Auth

`POST /api/admin/login` accepts `email` and `password`, returns:

- `access` token
- `refresh` token
- admin profile payload

For protected endpoints, send:

```http
Authorization: Bearer <access_token>
```

Swagger UI supports bearer auth. Click `Authorize` and paste the JWT access token as `Bearer <access_token>`.

## Render Deployment Notes

- Set all environment variables from `.env.example` in Render.
- Use `web: gunicorn config.wsgi:application` (already in `Procfile`).
- Run migrations during deploy:
  ```bash
  python manage.py migrate
  ```
# ttr_backend
