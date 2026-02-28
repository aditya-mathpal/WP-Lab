"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('groceryform/', include('groceryform.urls')),
    path('studentform/', include('studentform.urls')),
    path('carform/', include('carform.urls')),
    path('formex/', include('formex.urls')),
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
    path('formapp/',include('formapp.urls')),
    path('ex1app/', include('ex1app.urls')),
    path('ex2app/', include('ex2app.urls')),
    path('homeex1app/', include('homeex1app.urls')),
    path('basic_calc/', include('basic_calc.urls')),
    path('magazine/', include('magazine.urls')),
    path('book/', include('book.urls')),
    path('label/', include('label.urls')),
]