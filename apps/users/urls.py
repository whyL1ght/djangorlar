# Django modules
from django.urls import path
# Project modules
from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
]
