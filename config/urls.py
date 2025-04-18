"""oriana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from app_sensors.views import vue_test
from app_sensors.views import test_celery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vue-test/', vue_test),
    path('celery-test/', test_celery),
    path('',include(('app_users.urls', 'users'), namespace='users')),
    path('',include(('app_organizations.urls', 'organizations'), namespace='organizations')),
    path('',include(('app_sensors.urls', 'sensors'), namespace='sensors')),
    path('', include(('app_dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('', include(('app_amarey.urls', 'legacy'), namespace='legacy')),
]

if settings.DEBUG:
    # import debug_toolbar
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # urlpatterns = [
    #     # For django versions before 2.0:
    #     url(r'^__debug__/', include(debug_toolbar.urls)),

    # ] + urlpatterns


# print("--------------------------")
# print("LOCAL_CDN:",settings.LOCAL_CDN)
# print("STATIC_URL:",settings.STATIC_URL)
# print("STATIC_ROOT:",settings.STATIC_ROOT)
# print("MEDIA_URL:",settings.MEDIA_URL)
# print("MEDIA_ROOT:",settings.MEDIA_ROOT)
# print("STATICFILES_DIRS:",settings.STATICFILES_DIRS)
