from pathlib import Path
from configurations import Configuration
from book_my_show.common.enums.app_environment import AppEnvironment
import os
import logging
import boto3

# from boto3.session import Session


class Settings(Configuration):

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME")
<<<<<<< HEAD
    AWS_LOG_GROUP = "MyLogGroup"  # your log group
    AWS_LOG_STREAM = "Mystream"  # your stream
    AWS_LOGGER_NAME = "watchtower-logger"  # your logger
    boto3_session = Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME,
    )
=======
    AWS_LOG_GROUP = "BMKLogGroup"
    AWS_LOG_STREAM = "BMKstream"
    AWS_LOGGER_NAME = "bmk-watchtower-logger"

    boto3_logs_client = boto3.client("logs", region_name=AWS_REGION_NAME)
>>>>>>> d3f2900500d5d07a3eb3ff893d891e5702113f4c

    BASE_DIR = Path(__file__).resolve().parent.parent
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")

    SECRET_KEY = os.environ.get("SECRET_KEY")

    DEBUG = False

    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "book_my_show.heartbeat",
        "book_my_show.authenticate",
        "book_my_show.coreapis",
        "rest_framework.authtoken",
        "safedelete",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "book_my_show.middlewares.exception_handler_middleware.ExceptionHandlerMiddleware",
    ]

    ROOT_URLCONF = "book_my_show.urls"
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "watchtower": {
                "level": "DEBUG",
                "class": "watchtower.CloudWatchLogHandler",
                "boto3_client": boto3_logs_client,
                "log_group": AWS_LOG_GROUP,
                "stream_name": AWS_LOG_STREAM,
<<<<<<< HEAD
            },
=======
            }
>>>>>>> d3f2900500d5d07a3eb3ff893d891e5702113f4c
        },
        "loggers": {
            AWS_LOGGER_NAME: {
                "level": "DEBUG",
                "handlers": ["watchtower"],
                "propagate": False,
            }
        },
    }

    WSGI_APPLICATION = "book_my_show.wsgi.application"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = "static/"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    APP_ENVIRONMENT: AppEnvironment = None
    AUTH_USER_MODEL = "authenticate.UserModel"
