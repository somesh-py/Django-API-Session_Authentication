from django.shortcuts import render
from .serilizers import EmployeeSerilizers
from .models import Employee
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly,DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.


class EmployeeAPI(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizers
    authentication_classes = [SessionAuthentication]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # parser_classes=[DjangoModelPermissionsOrAnonReadOnly]
