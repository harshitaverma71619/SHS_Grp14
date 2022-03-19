"""SHS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include

urlpatterns = [
    path('', include('Hospitalportal.urls')),
    path('home/', include('homepage.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('patient/',include('Patients.urls',namespace='patient')),
=======
    path('labStaff/', include('LabStaff.urls'))
>>>>>>> 43b08a4b2c6cac0e38c02e002d5c6c999c8ba9de
]
