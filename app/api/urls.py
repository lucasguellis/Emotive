from django.urls import path

from . import views

urlpatterns = [
    path('get', views.get, name='weather'),
    path('search', views.search, name='weather'),
]
