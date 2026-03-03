from django.urls import path
from . import views

urlpatterns = [
    path('billing/', views.billing_page, name='billing'),
    path('billing/result/', views.bill_result, name='bill_result'),
]