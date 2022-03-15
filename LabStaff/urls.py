from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.labStaff, name='labStaff'),
]