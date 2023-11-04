from .base import *

ALLOWED_HOSTS = ['host.docker.internal', 'localhost']

#Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}


# Statics
# LOCAL_CDN is a variable that is True for show statics from static_cdn folder
LOCAL_CDN = False 

# STATICFILES_DIRS = [
#     os.path.join("app-ui","dist")
# ]

# Celery
# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True

print("-----------dev ------------")

print('BASE_DIR', BASE_DIR)

print('STATIC_URL', STATIC_URL)
print('STATICFILES_DIRS', STATICFILES_DIRS)
print('STATIC_ROOT', STATIC_ROOT)

print('MEDIA_ROOT ', MEDIA_ROOT)
print('MEDIA_URL', MEDIA_URL)
# print('AWS_LOCATION', f'{AWS_LOCATION}/{STATIC_URL}ckeditor/ckeditor/')
print("-----------------------")