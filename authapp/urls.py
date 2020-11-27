from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]