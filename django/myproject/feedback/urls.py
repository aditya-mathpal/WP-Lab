from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_page, name='feedback'),
]