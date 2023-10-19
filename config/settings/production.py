from .base import *

DEBUG = False

# Celery
# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True

ALLOWED_HOSTS =['localhost', 'app.gthux.com']

#Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
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