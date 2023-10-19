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
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
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