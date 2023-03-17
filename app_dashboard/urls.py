from django.conf.urls import url
from django.urls import include, path

from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('api/cart/', include('ingenialo.carts.api.urls')),
]