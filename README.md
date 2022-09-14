Docker environment for a Django 1.11 project
===========================================

# Project Details

# Django install project & name
docker-compose run django django-admin.py startproject seller_django .

# Django App name
docker-compose run django python manage.py startapp seller_math

# Start Project
docker-compose up -d

# Worke 
127.0.0.1:8000

# Django migrations:
Type `docker-compose exec` django bash in your bash to enter the python django bash.

Now run the migrations like so

`python manage.py makemigrations`

And

`python manage.py migrate`

Note: If it's the first time you're running the migrations and your app is not working in your browser, try docker-compose stop and docker-compose up -d again. This is due to Django trying to execute the app without the ddbb created yet. It should now work.

**Note:** If it's the first time you're running the migrations and your app is not working in your browser, try `docker-compose stop` and `docker-compose up -d` again. This is due to Django trying to execute the app without the ddbb created yet. It should now work.

**Note:**
`https://docs.docker.com/samples/django/`


