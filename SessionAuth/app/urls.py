from django.urls import path,include
from .views import EmployeeAPI
from rest_framework import routers


routers=routers.DefaultRouter()

routers.register(r'EmployeeAPI',EmployeeAPI,basename='EmployeeAPI')

urlpatterns = [
    path('',include(routers.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
