# @author - aishwarya
from django.urls import path, re_path
from . import views
app_name = 'patient'

urlpatterns = [
    path('', views.patientHome.as_view(), name='patientHome'),
    path('bookAppointment', views.bookAppointment.as_view(), name='bookAppointment'),
    re_path(r'^updateAppointment/(?P<id>\d+)/$', views.updateAppointment.as_view(), name='updateAppointment'),
    re_path(r'^nextAppointment/(?P<id>\d+)/$', views.nextAppointment.as_view(), name='nextAppointment'),
    path('insuranceClaimRequest', views.insuranceClaimRequest.as_view(), name='insuranceClaimRequest'),
    re_path(r'^updateInsuranceClaimRequest/(?P<id>\d+)/$', views.updateInsuranceClaimRequest.as_view(), name='updateInsuranceClaimRequest')
    re_path(r'^updateInsuranceClaimRequest/(?P<id>\d+)/$', views.updateInsuranceClaimRequest.as_view(), name='updateInsuranceClaimRequest'),
    re_path(r'^logout/(?P<id>\d+)/$', views.logout_user),
    re_path(r'^home/(?P<id>\d+)/$', views.patientHome.as_view(), name='patientHome'),
]