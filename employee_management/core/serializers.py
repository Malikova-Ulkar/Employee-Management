from rest_framework import serializers

from .models import Department, Position, Employee



class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Department

        fields = '__all__'



class PositionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Position

        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee

        fields = '__all__'