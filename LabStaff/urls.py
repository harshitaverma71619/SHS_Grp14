from django.urls import URLPattern, path
from . import views
app_name = "LabStaff"

urlpatterns = [
    path('', views.labStaffHome.as_view(), name='labStaffHome'),
    path('viewRequests', views.viewRequests.as_view(), name='viewRequests')
]

# app_name = 'Patients'

# urlpatterns = [
#     path('', views.patientHome.as_view(), name='patientHome'),
#     path('bookAppointment', views.bookAppointment.as_view(), name='bookAppointment'),
# ]