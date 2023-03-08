import os
from decouple import config as env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = env('DEBUG', cast=bool)

ALLOWED_HOSTS: list[str] = []

# Application definition

DJANGO_APPS: list[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS: list[str] = [
    'rest_framework',
]

LOCAL_APPS: list[str] = [
    'pets',
    'users'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE: list[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF: str = 'django_app.urls'

TEMPLATES: list[dict] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION: str = 'django_app.wsgi.application'

DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS: list[dict] = [
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

LANGUAGE_CODE: str = 'en-us'

TIME_ZONE: str = 'UTC'

USE_I18N: bool = True

USE_L10N: bool = True

USE_TZ: bool = True

STATIC_URL: str = '/static/'

AUTH_USER_MODEL: str = 'users.User'

DEFAULT_FILE_STORAGE: str = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_REGION_NAME: str = env('AWS_S3_REGION_NAME')
AWS_ACCESS_KEY_ID: str = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME: str = env('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY: bool = env('AWS_S3_VERIFY', cast=bool)
AWS_QUERYSTRING_AUTH: bool = env('AWS_QUERYSTRING_AUTH', cast=bool)
AWS_S3_SIGNATURE_VERSION: str = env('AWS_S3_SIGNATURE_VERSION')
AWS_QUERYSTRING_EXPIRE: int = env('AWS_QUERYSTRING_EXPIRE', cast=int)

EXTERNAL_URLS: dict = {
    'DOG_BREEDS_URL': env('DOG_BREEDS_URL')
}
