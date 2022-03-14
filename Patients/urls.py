# @author - aishwarya
from django.urls import path , include
from . import views
app_name = 'Patients'

urlpatterns = [
    path('', views.patientHome.as_view(), name='patientHome'),
    path('bookAppointment', views.bookAppointment.as_view(), name='bookAppointment'),
]