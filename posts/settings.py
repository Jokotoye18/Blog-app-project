"""
Django settings for posts project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from decouple import config, Csv
import os
import django_heroku
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '#p16i(40bnb$-z8d@6%tcnczczuo%jkibfe2swvmo)pby*bjx+'
SECRET_KEY = config('SECRET_KEY')

ENVIRONMENT = config('ENVIRONMENT', default='production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())


sentry_sdk.init(
    dsn=config('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    send_default_pii=True
)

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    
    

    #django_comments app
    'django_comments_xtd',
    'django_comments',
    'django_markdown2',

    #third party app
    #API
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'drf_yasg',
    'taggit_serializer',
    'django_filters',


    #others
    'debug_toolbar',
    'crispy_forms',
    "taggit",
    'martor',
    'django_bleach',
    'storages',
 
     #local app
    'articles.apps.ArticlesConfig',
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#whitenoise
    # 'django.middleware.cache.UpdateCacheMiddleware',#cache
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware', #cache
    # 'csp.middleware.CSPMiddleware',#django-csp
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',#debug_toolbar
    "django.middleware.common.BrokenLinkEmailsMiddleware", #Manager
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'posts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'posts.wsgi.application'

#site_app
SITE_ID = 1

#django-taggit
TAGGIT_CASE_INSENSITIVE = True



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': config('DB_ENGINE'),
    #    'NAME': config('DB_NAME'),
    #    'USER': config('DB_USER'),
    #    'HOST': config('DB_HOST'),
    #    'PASSWORD': config('DB_PASSWORD'),
    #    'PORT': 5432
    #},
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

DATABASE_URL = config('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

INTERNAL_IPS = [
    '127.0.0.1',
]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#static config
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = 'articles:article_lists'
LOGOUT_REDIRECT_URL = 'pages:home'

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# crispy_form
CRISPY_TEMPLATE_PACK = 'bootstrap4'


#comments_app
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 4
COMMENTS_XTD_COMFIRM_EMAIL = True
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. " b"Aequam memento rebus in arduis servare mentem.")
COMMENTS_XTD_SEND_HTML_EMAIL = True 
COMMENTS_XTD_MARKUP_FALLBACK_FILTER = 'markdown'
COMMENTS_XTD_APP_MODEL_OPTIONS = {
     'articles.article': {
        'allow_flagging': True, 
        'allow_feedback': True, 
        'show_feedback': True,
     } 
}




#email_settings
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST') 
EMAIL_HOST_USER = config('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') 
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
DEFAULT_FROM_EMAIL = 'Jokotoye18 Blog <jokotoyeademola995@gmail.com>'

ADMIN = (
    ('Jokotoye Ademola', 'jokotoyeademola95@gmail.com'),
)

SERVER_EMAIL = DEFAULT_FROM_EMAIL

MANAGERS = ADMIN

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
          


# AWS config
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH=False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'media'
AWS_S3_REGION_NAME = 'us-east-2' #change to your region
AWS_S3_SIGNATURE_VERSION = 's3v4'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:				
    from.local_settings	import * 
except ImportError:
    pass


#Martor
CSRF_COOKIE_HTTPONLY = False
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',        # to enable/disable emoji icons.
    'imgur': 'true',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

# To setup the martor editor with label or not (default is False)
MARTOR_ENABLE_LABEL = True

# Imgur API Keys
# MARTOR_IMGUR_CLIENT_ID = 'e2be1ac381249b7'
# MARTOR_IMGUR_API_KEY   = 'ff5d8d9e226198ae46672a0f778a5341ec59117e'
import time
MARTOR_UPLOAD_PATH = 'images/uploads/'
MARTOR_UPLOAD_URL = '/api/uploader/'  # change to local uploader

# Maximum Upload Image
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_IMAGE_UPLOAD_SIZE = 5242880  # 5MB


CACHE = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', 
            'LOCATION': '127.0.0.1:11211',
            'OPTIONS': {
                'server_max_value_length': 1024 * 1024 * 2,
            }

        }
    }

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600   
CACHE_MIDDLEWARE_KEY_PREFIX = '' 



if ENVIRONMENT == 'production':
    
    #HTTP Strict Transport Security (HSTS)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_PRELOAD = True

    #Cross-Site Request Forgery (CSRF)
    CSRF_COOKIE_SECURE = True  # cookie will only be sent over an HTTPS connection
    CSRF_COOKIE_HTTPONLY = False  # only accessible through http(s) request, JS not allowed to access csrf cookies

    
    # SECURE_REFERRER_POLICY = 'same-origin'
    
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    #Cross-Site Scripting (XSS)
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_HTTPONLY = True
    #django-csp(Details at official docs)

django_heroku.settings(locals())


REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASSES': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}