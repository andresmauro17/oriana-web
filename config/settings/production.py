from .base import *

DEBUG = False

# Celery
# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True

ALLOWED_HOSTS =['localhost', 'app.gthux.com']
CSRF_TRUSTED_ORIGINS = ['https://app.gthux.com', 'http://app.gthux.com']

#Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        # Handler for request logs
        "requests_file": {
            "level": "INFO",  # Captures all HTTP requests (change to DEBUG for more details)
            "class": "logging.FileHandler",
            "filename": "/var/log/django_requests.log",
            "formatter": "requests",
        },
        # Handler for error logs
        "errors_file": {
            "level": "ERROR",  # Captures only errors (HTTP 4xx/5xx, exceptions, etc.)
            "class": "logging.FileHandler",
            "filename": "/var/log/django_errors.log",
            "formatter": "errors",
        },
    },
    "loggers": {
        # Logger for HTTP requests
        "django.server": {
            "handlers": ["requests_file"],
            "level": "INFO",
            "propagate": False,
        },
        # Logger for errors
        "django.request": {
            "handlers": ["errors_file"],
            "level": "ERROR",
            "propagate": False,
        },
    },
    "formatters": {
        # Formatter for request logs
        "requests": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        # Formatter for error logs
        "errors": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}

print("-----------prod ------------")

# print('BASE_DIR', BASE_DIR)
print('STATIC_URL', STATIC_URL)
print('STATICFILES_DIRS', STATICFILES_DIRS)
print('STATIC_ROOT', STATIC_ROOT)

print('MEDIA_ROOT ', MEDIA_ROOT)
print('MEDIA_URL', MEDIA_URL)
# print('AWS_LOCATION', f'{AWS_LOCATION}/{STATIC_URL}ckeditor/ckeditor/')
print("-----------------------")