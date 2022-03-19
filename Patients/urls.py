# @author - aishwarya
from django.urls import path, re_path
from . import views
app_name = 'Patients'

urlpatterns = [
    path('', views.patientHome.as_view(), name='patientHome'),
    path('bookAppointment', views.bookAppointment.as_view(), name='bookAppointment'),
    re_path(r'^updateAppointment/(?P<id>\d+)/$', views.updateAppointment.as_view(), name='updateAppointment')
]