import os
from pathlib import Path
from workers import env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.DJANGO_SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = [
    "therepeat.live",
    "www.therepeat.live",
]

CSRF_TRUSTED_ORIGINS = [
    "https://therepeat.live",
    "https://www.therepeat.live",
]

# Application definition

INSTALLED_APPS = [
    # Django Unfold - must be before django.contrib.admin
    'unfold',

    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',

    # Local apps
    'categories',
    'feedback',
]


# Django Unfold Configuration

UNFOLD = {
    "SITE_TITLE": "TheRepeat Admin",
    "SITE_HEADER": "TheRepeat",
    "SITE_SUBHEADER": "Music website",
    "SITE_SYMBOL": "home",

    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,

    "DASHBOARD_CALLBACK": None,
}


# Middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL Configuration

ROOT_URLCONF = 'config.urls'


# Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.parent / "frontend"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database Configuration
DATABASES = {
    "default": {
        "ENGINE": "django_cf.db.backends.d1",
        "CLOUDFLARE_BINDING": "DB",
    }
}


# Password Validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static Files

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'categories' / 'media'

# Default Primary Key

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'