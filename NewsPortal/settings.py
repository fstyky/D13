

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^!t2#n&#z7120^q-((y++q3dc8jwubpqn1%f_hb#%v$e8fns=h'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'main_app.apps.MainAppConfig',
    'sign',
    'django_filters',
    # 'django_apscheduler',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

EMAIL_HOST_USER = "fstyky@gmail.com.com"
EMAIL_HOST_PASSWORD = "xxx"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]


ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_FORMS = {'signup': 'sign.forms.BasicSignupForm'}


WSGI_APPLICATION = 'NewsPortal.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True





STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = 'static/'





STATIC_MY_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = f'{STATIC_MY_DIR} / static'





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False



ADMINS = [
    ('Admin', 'a.erastov@gmail.com')
]

def debug_info_filter(message):
    return message.levelname == 'DEBUG' or message.levelname == 'INFO'


def warning_filter(message):
    return message.levelname == 'WARNING'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console_debug_info': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'console_warning': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'console_error_critical': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'file_general_log': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'file_errors_log': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'file_security_log': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'mail_errors_log': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'debug_info_filter': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': debug_info_filter,
        },
        'warning_filter': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': warning_filter,
        },
    },
    'handlers': {
        'console_debug_info': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_info_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug_info'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true', 'warning_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning'
        },
        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error_critical'
        },
        'file_general_log': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'Logging/general.log',
            'formatter': 'file_general_log'
        },
        'file_errors_log': {
            'class': 'logging.FileHandler',
            'filename': 'Logging/errors.log',
            'formatter': 'file_errors_log'
        },
        'file_security_log': {
            'class': 'logging.FileHandler',
            'filename': 'Logging/security.log',
            'formatter': 'file_security_log'
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'mail_errors_log'
        }
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console_debug_info', 'console_warning', 'console_error_critical', 'file_general_log'],
            'propagate': True
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['file_errors_log', 'mail_admins'],
        },
        'django.server': {
            'level': 'ERROR',
            'handlers': ['file_errors_log', 'mail_admins'],
        },
        'django.template': {
            'level': 'ERROR',
            'handlers': ['file_errors_log'],
        },
        'django.db_backends': {
            'level': 'ERROR',
            'handlers': ['file_errors_log'],
        },
        'django.security': {
            'level': 'DEBUG',
            'handlers': ['file_security_log'],
        },
    }
}


