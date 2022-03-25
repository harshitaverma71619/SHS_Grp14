from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.labStaffHome.as_view(), name='labStaffHome'),
    path('viewRequests', views.viewRequests.as_view(), name='viewRequests')
]