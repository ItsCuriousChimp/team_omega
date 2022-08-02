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

# Authentication
Authentication is the mechanism of associating an incoming request with a set of identifying credentials, such as the user the request came from, or the token that it was signed with. The permission and throttling policies can then use those credentials to determine if the request should be permitted.

## Token Authentication:
### Setting the authentication scheme :
First we need to add authentication framework class in the ``` settings.py ``` file.
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```
Add TokenAuthentication in installed app :
```
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```
# Generating Token:
If you want every user to have an automatically generated Token, you can simply catch the User's post_save signal.

```
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```
Token is return in reposnse when we register a user.

# Getting the Token :
In oreder to get the token corresponds to particular Username and Password, TokenAuthentication provides inbuilt API in which we need to provide the username and password which in response returns the Token for that particular User.

For that we need to add path in ```urls.py``` as 

```
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
```
Then our endpoint would look like
```
http://localhost:8000/api-token-auth/
```
in which we pass username and password as parameters and in response we get Token for that particular user.
# Authenticating the Token

For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
We also need to add authentication classes in the views where authentication is necessary to access the API. Like given bellow for 
``` booking_view.py ``` which is an view of API to book ticket for a show.
```
from rest_framework.views import APIView
# Need to be imported to check authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BookingView(APIView):
   authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(
        self,
        booking_service: IBookingService = Provide[ServiceContainer.booking_service],
    ) -> None:
       # Implemented in the '''booking_view.py'''

```