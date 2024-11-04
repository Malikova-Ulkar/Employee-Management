from celery import shared_task

from .models import Employee

from django.utils import timezone

from datetime import timedelta



@shared_task

def notify_inactive_employees():

    two_days_ago = timezone.now() - timedelta(days=2)

    inactive_employees = Employee.objects.filter(created_at__lt=two_days_ago, status=True)

    for employee in inactive_employees:

        # Send notification logic here

        print(f"Notification sent to {employee.email}")