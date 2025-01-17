# EASY TAGALOG

# Backend

## Run Python Virtual Environment

Windows:
```bash
venv\Scripts\activate
```

Mac or Linux:
```bash
source venv/bin/activate
```

## Migrations

With Django REST framework you will need to run certain commands

If you make changes to your models (i.e. adding a new field to a model), you will need to:
```python
python manage.py makemigrations
```

This command generates a migration file reglecting the changes you made.

To apply the migration to the database, you will need to run:
```python
python manage.py migrate
```

**DO MIGRATION STEPS IN THIS ORDER**

## Creating apps

If you want to create a new app, or object in the database, you should create a new app by running:
```python
python manage.py startapp <app-name>
```

For example if you want to create an app to manage `users`, you could run:
```python
python manage.py startapp users
```

**REMEMBER**: When you create an app, you need to register it in the projects `settings.py` under the `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    # other default apps
    'users',
    'tests',
]
```

When you create an app, you will want to manage its objects in Django's admin interface.
So make sure you register your model in `admin.py`
```python
from django.contrib import admin
from .models import Test

admin.site.register(Test)
```

## Creating a superuser

You will want to create a superuser for accessing the admin panel, which can be done by running:
```python
python manage.py createsuperuser
```

## Running a server

Run a development server to test changes by running:
```python
python manage.py runserver
```

## Static files

Static files like CSS, JS, and images should go in a `static/` directory