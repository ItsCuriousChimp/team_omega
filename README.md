# Book My Show

Book My Show is a movie ticket booking API.

# Cloning Project from Github

```
git clone https://github.com/ItsCuriousChimp/team_omega.git
```

Have your own features added by creating a branch from it

```
git checkout -b branch-name
```

## Installation

First we need to set-up Virtual Environment to install all of our dependencies.

```bash
python -m venv venv
```

This will set-up a virtual environment in your Django project and create a folder named as venv, where all the required dependencies would be install.

To activate the VE we need to get in the directory where venv is located and run command as

```python
.\venv\Scripts\activate
```

Now we can start with our project

## Install All Dependencies

### create a file named requirements with '.txt' extension and write all the required dependencies in it(with specified version).

```text
django==4.0.5
djangorestframework==3.13.0
pyyaml==6.0
requests==2.28.1
django-cors-headers==3.13.0
pylint==2.14.4
pre-commit==2.19.0
black==22.6.0
django-configurations==2.3.2
python-dotenv==0.20.0
django-safedelete==1.2.2

```

## Install requirements.txt

```
pip install -r requirements.txt
```

This will install all the required dependencies.

Now we can start with our Django project configuration

# .env file

There are times in Django where you have to provide sensitive information in the backend. Like providing DJANGO_CONFIGURATION, user_id, passwords etc.

# Main Components of a Django App

- Views
- Models
- Services
- Repositories
- Dtos

## manage.py file

manage.py in Django is a command-line utility that works similar to the django-admin command. The difference is that it points towards the project's settings.py file. This manage.py utility provides various commands that you must have while working with Django

Here now we are all set to start with creating different API.

To run the project we run the command as

```
python manage.py runserver
```

now it will run the API on local server
with base endpoint as

# http://127.0.0.1:8000/

you can create different endpoint in the projects starting with this as base URL.
