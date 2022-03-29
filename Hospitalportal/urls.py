from django.urls import path , include
from . import views

urlpatterns = [
    
    path('Login', views.Login.as_view(), name='Login'),
    path('Register', views.Register, name='Register'),
    path('Registercheck', views.Registercheck.as_view(), name='Registercheck'),
     path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]