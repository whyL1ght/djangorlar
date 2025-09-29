from django.urls import path
from . import views

urlpatterns = [
    path('', views.cnt_view, name='cnt_view'),
    path('increment/', views.increment, name='increment'),
    path('reset/', views.reset, name='reset'),
]
