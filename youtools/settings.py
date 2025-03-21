import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
from data.database import DATABASES, CACHES # imported database # pylint: disable=unused-import

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", 0)))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")



# Application definition

INSTALLED_APPS = [
    'django_daisy',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
]

ADDED_APPS = [
    "accounts",
    "api_gateway_microservices",
    "images",
    "sentiment_analysis",
    "BaseID",
    "products",
    "others"
]

THIRDPARTY_APPS = [
    "rest_framework",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    "rest_framework.authtoken",
    "corsheaders",
    # "django_admin_logs",

    # Social Authentication

    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google"

]

# Added Own created apps
INSTALLED_APPS += ADDED_APPS

# Added 3rd party apps/library
INSTALLED_APPS += THIRDPARTY_APPS

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        "APP": {
            "client_id": os.getenv("GOOGLE_SOCIAL_LOGIN_CLIENT_ID"),
            "secret": os.getenv("GOOGLE_SOCIAL_LOGIN_SECRET_KEY"),
            "key": ""
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

AUTH_USER_MODEL = 'accounts.User'

DJANGO_ADMIN_LOGS_DELETABLE = False
DJANGO_ADMIN_LOGS_ENABLED = True
DJANGO_ADMIN_LOGS_IGNORE_UNCHANGED = True


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "api_gateway_microservices.middleware.MoveJWTRefreshCookieIntoTheBody",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:80",
    "http://localhost:8000",
    "http://localhost:8080",
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "withcredentials",
)

# Email configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_USE_TLS = True




ROOT_URLCONF = "youtools.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = "youtools.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

SITE_ID = 1
REST_USE_JWT = True #  For Using Json Web Token

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = '/media/'

STATIC_ROOT = "/vol/web/static"
MEDIA_ROOT = "/vol/web/media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    'ALGORITHM': 'HS256',
    "SIGNING_KEY": os.environ.get('DJANGO_SIGNING_KEY'),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
    'JTI_CLAIM': 'jti',
}



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    )
    
}


SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"


REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY':True,
    'JWT_AUTH_COOKIE': 'access_token',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_SECURE': True,
    'JWT_AUTH_SAMESITE': 'Lax',
    'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.LoginSerializer',
    'REGISTER_SERIALIZER': 'dj_rest_auth.registration.serializers.RegisterSerializer'
} 

SOCIALACCOUNT_ADAPTER = 'accounts.adapters.SocialAccountAdapter'


ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

LOGIN_URL = 'http://localhost:8080/login'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Django sessions are stored in Redis
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


DAISY_SETTINGS = {
    'SITE_TITLE': 'Youtools AI',  # The title of the site 
    'SITE_HEADER': 'Youtools AI Admin Control Panel',  # Header text displayed in the admin panel
    'INDEX_TITLE': 'Hi, welcome to your dashboard',  # The title for the index page of dashboard
    'SITE_LOGO': '/static/logo/youtools.png',  # Path to the logo image displayed in the sidebar
    'EXTRA_STYLES': ['/static/logo/image.css'],  # List of extra stylesheets to be loaded in base.html (optional)
    'EXTRA_SCRIPTS': [],  # List of extra script URLs to be loaded in base.html (optional)
    'LOAD_FULL_STYLES': True,  # If True, loads full DaisyUI components in the admin (useful if you have custom template overrides)
    'SHOW_CHANGELIST_FILTER': True,  # If True, the filter sidebar will open by default on changelist views
    'DONT_SUPPORT_ME': True, # Hide github link in sidebar footer
    'SIDEBAR_FOOTNOTE': '', # add footnote to sidebar
    'APPS_REORDER': {
        # Custom configurations for third-party apps that can't be modified directly in their `apps.py`
        'auth': {
            'icon': 'fa-solid fa-person-military-pointing',  # FontAwesome icon for the 'auth' app
            'name': 'Authentication',  # Custom name for the 'auth' app
            'hide': False,  # Whether to hide the 'auth' app from the sidebar (set to True to hide)
            'divider_title': "Auth",  # Divider title for the 'auth' section
        },
        'social_django': {
            'icon': 'fa-solid fa-users-gear',  # Custom FontAwesome icon for the 'social_django' app
        },
    },
}