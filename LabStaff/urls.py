from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.labStaffHome.as_view(), name='labStaffHome'),
    path('viewRequests', views.viewRequests.as_view(), name='viewRequests'),
    path('addLabRecord', views.addLabRecord.as_view(), name='addLabRecord'),
    path('updateLabRecord', views.updateLabRecord.as_view(), name='updateLabRecord'),
    path('viewLabRecord', views.viewLabRecord.as_view(), name='viewLabRecord')
]