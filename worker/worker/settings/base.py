from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-l=z$v=v#_!qz^-i*1-q37mw1rv&9^hzo5r@ilw5yj^vc1&3*a#"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# custom user 'app_label.model_name'
AUTH_USER_MODEL = "api.User"


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

FIRST_PARTY_APPS = [
    "api",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
]

INSTALLED_APPS += FIRST_PARTY_APPS + THIRD_PARTY_APPS


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "api.authentications.BaseJSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DATETIME_FORMAT": "%s",
}

JWT_AUTH = {
    "JWT_AUTH_HEADER_PREFIX": "jwt",
    "JWT_AUTH_COOKIE": "token",
    "JWT_EXPIRATION_DELTA": timedelta(minutes=30),
    "JWT_ALLOW_REFRESH": True,
    "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_payload_handler",
    "JWT_PAYLOAD_GET_USER_ID_HANDLER": "rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_response_payload_handler",
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
    "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
    "JWT_SECRET_KEY": SECRET_KEY,
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

THIRD_PARTY_MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

CORS_ALLOW_ALL_ORIGINS = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

ROOT_URLCONF = "worker.urls"


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


WSGI_APPLICATION = "worker.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
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

AUTHENTICATION_BACKENDS = [
    # Custom django backend
    "api.backends.CustomBackend",
    # Default django backend
    "django.contrib.auth.backends.ModelBackend",
]

# PAYPAL PAYMENT GATEWAY SETTINGS
PAYPAL_ENVIRONMENT = "sandbox"
PAYPAL_CLIENT_ID = (
    "AaUxPPiAzJeUA3uijnHdAyNZ8h5R6iPQ0KhIJIFhNlwGPZJHuFtqpZDY6rGQZT0Hej4arrYFEXVKbuhC"
)
PAYPAL_CLIENT_SECRET = (
    "EO2mBilH4t-ENG_EGT7Do2h435_5S6scSzJOQTe9rbacQFnPIjXa14mTngU-N6kJ4t8T27hY7BbDeIuB"
)

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

MEDIA_URL = "media/"

BASE_MEDIA_URL = "http://localhost:8000/media/"

MEDIA_ROOT = BASE_DIR / "media"

IMAGE_MODE = "RGB"
IMAGE_SIZE = (224, 224)
MAX_PIXEL_VALUE = 255.0

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
