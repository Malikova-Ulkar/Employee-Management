from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import Department, Position, Employee

from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer



class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer

    permission_classes = [permissions.IsAuthenticated]



class PositionViewSet(viewsets.ModelViewSet):

    queryset = Position.objects.all()

    serializer_class = PositionSerializer

    permission_classes = [permissions.IsAuthenticated]



class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    permission_classes = [permissions.IsAuthenticated]

