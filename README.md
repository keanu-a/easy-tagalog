# EASY TAGALOG

## Backend

### Run Python Virtual Environment

Windows:
`venv\Scripts\activate`

Mac or Linux:
`source venv/bin/activate`

### Migrations

With Django REST framework you will need to run certain commands

If you make changes to your models (i.e. adding a new field to a model), you will need to:
`python manage.py makemigrations`

This command generates a migration file reglecting the changes you made.

To apply the migration to the database, you will need to run:
`python manage.py migrate`

If you want to create a new app, or object in the database, you should create a new app by running:
`python manage.py startapp <app-name>`

For example if you want to create an app to manage users, you could run:
`python manage.py startapp users`

**REMEMBER**: When you create an app, you need to register it in the projects `settings.py` under the `INSTALLED_APPS`