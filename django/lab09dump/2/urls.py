from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_work, name='add_work'),
    path('search/', views.search_company, name='search_company'),
]