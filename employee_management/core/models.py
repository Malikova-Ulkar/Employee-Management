from django.db import models

from django.db import models

from django.contrib.auth.models import AbstractUser



class Department(models.Model):

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



class Position(models.Model):

    name = models.CharField(max_length=255)

    salary = models.DecimalField(max_digits=10, decimal_places=2)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



class Employee(models.Model):

    name = models.CharField(max_length=255)

    surname = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
