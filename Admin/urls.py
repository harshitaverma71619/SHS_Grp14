from . import views
from django.urls import URLPattern, path, re_path
app_name = 'Admin'

urlpatterns = [
    path('', views.adminHome.as_view(), name='adminHome'),
    re_path('createEmployeeRecords', views.createEmployeeRecords.as_view(), name='createEmployeeRecords'),
    re_path('viewEmployeeRecords', views.viewEmployeeRecords.as_view(), name='viewEmployeeRecords'),
    re_path('editEmployeeRecords', views.editEmployeeRecords.as_view(), name='editEmployeeRecords'),
    re_path(r'^updateEmployeeDetails/(?P<id>\d+)/$', views.updateEmployeeDetails.as_view(), name='updateEmployeeDetails'),
    re_path(r'^updateEmployeeDetails/delete/(?P<id>\d+)/$', views.deleteEmployeeRecord.as_view(), name='deleteEmployeeRecord')
]