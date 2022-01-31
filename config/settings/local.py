from .base import *

# Statics
# LOCAL_CDN is a variable that is True for show statics from static_cdn folder
LOCAL_CDN = False 

STATICFILES_DIRS = [
    os.path.join("app-ui","dist")
]

# Celery
# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True