from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_works),
    path('search/', views.search_company),
]