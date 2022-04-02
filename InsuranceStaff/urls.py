# @author - aishwarya
from django.urls import path, re_path
from . import views
app_name = 'InsuranceStaff'

urlpatterns = [
    path('', views.insuranceHome.as_view(), name='insuranceHome'),
    path('newPolicies/', views.newPolicies.as_view(), name='newPolicies'),
    path('viewPolicies/', views.viewPolicies.as_view(), name='viewPolicies'),
    re_path(r'^checkClaims/(?P<id>\d+)/$', views.checkClaims.as_view(), name='checkClaims'),
    path('viewClaimRequests/', views.viewClaimRequests.as_view(), name='viewClaimRequests'),

    
    
   ]