from django.urls import path, re_path
from . import views
app_name = 'Doctors'

urlpatterns = [
    path('', views.doctorHome.as_view(), name='doctorHome'),
    path('patientRecords/', views.patientRecords.as_view(), name='patientRecords'),
    path('viewLabReports/', views.viewLabReports.as_view(), name='viewLabReports'),
    re_path(r'^patientRecords/search/(?P<id>\d+)/$', views.updatePatientDetails.as_view(), name='updatePatientDetails'),
    re_path(r'^diagnosis/searchDiagnosis/(?P<id>\d+)/$', views.updatePatientDiagnosis.as_view(), name='updatePatientDiagnosis'),
    path('patientRecords/search/', views.searchBar, name='search'),
    path('viewLabReports/search1/', views.searchLabReports, name='search1'),
    path('diagnosis/', views.patientDiagnosis.as_view(), name='diagnosis'),
    path('diagnosis/searchDiagnosis/', views.searchDiagnosis, name='searchDiagnosis'),
    path('searchAppointments',views.searchAppointments, name='searchAppointments'),
    re_path(r'addDiagnosis/(?P<id>\d+)/$',views.addDiagnosis.as_view(), name = 'addDiagnosis'),
    re_path(r'addPrescription/(?P<id>\d+)/$',views.addPrescription.as_view(), name = 'addPrescription')
]