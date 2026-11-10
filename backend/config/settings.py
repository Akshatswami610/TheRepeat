import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================
# CORE SETTINGS
# =====================================

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "therepeat.live",
    "www.therepeat.live",
    "therepeat.pages.dev",
    "therepeat-backend.onrender.com",
    "localhost",
    "127.0.0.1",
]

CORS_ALLOWED_ORIGINS = [
    "https://therepeat.pages.dev",
    "https://therepeat.live",
    "https://www.therepeat.live",
]

# =====================================
# APPLICATIONS
# =====================================

INSTALLED_APPS = [
    # Django Unfold
    "unfold",

    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "corsheaders",

    # Local apps
    "categories",
    "feedback",
]


# =====================================
# DJANGO UNFOLD
# =====================================

UNFOLD = {
    "SITE_TITLE": "TheRepeat Admin",
    "SITE_HEADER": "TheRepeat",
    "SITE_SUBHEADER": "Music website",
    "SITE_SYMBOL": "home",

    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,

    "DASHBOARD_CALLBACK": None,
}


# =====================================
# MIDDLEWARE
# =====================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =====================================
# URL CONFIGURATION
# =====================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# =====================================
# TEMPLATES
# =====================================

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


# =====================================
# DATABASE - SUPABASE POSTGRESQL
# =====================================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=0,
        ssl_require=True,
    )
}


# =====================================
# PASSWORD VALIDATION
# =====================================

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


# =====================================
# INTERNATIONALIZATION
# =====================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =====================================
# STATIC FILES - WHITENOISE
# =====================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "config.storage_backends.SupabaseMediaStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# =====================================
# SUPABASE STORAGE
# =====================================

SUPABASE_URL = config("SUPABASE_URL")

SUPABASE_S3_ENDPOINT = config("SUPABASE_S3_ENDPOINT")

SUPABASE_S3_REGION = config("SUPABASE_S3_REGION")

SUPABASE_S3_ACCESS_KEY = config("SUPABASE_S3_ACCESS_KEY")

SUPABASE_S3_SECRET_KEY = config("SUPABASE_S3_SECRET_KEY")

SUPABASE_MEDIA_BUCKET = config(
    "SUPABASE_MEDIA_BUCKET",
    default="therepeat-media",
)


# =====================================
# SECURITY
# =====================================

if not DEBUG:
    SECURE_SSL_REDIRECT = config(
        "SECURE_SSL_REDIRECT",
        default=True,
        cast=bool,
    )

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )


# =====================================
# DEFAULT PRIMARY KEY
# =====================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
