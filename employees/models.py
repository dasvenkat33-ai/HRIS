from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    VISA_TYPE_CHOICES = [
        ("Employment", "Employment"),
        ("Visit", "Visit"),
        ("Golden", "Golden"),
        ("Investor", "Investor"),
        ("Dependent", "Dependent"),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Terminated", "Terminated"),
    ]

    employee_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    passport_number = models.CharField(max_length=50, null=True, blank=True)
    passport_expiry_date = models.DateField(null=True, blank=True)

    emirates_id_number = models.CharField(max_length=50, null=True, blank=True)
    emirates_id_expiry_date = models.DateField(null=True, blank=True)

    visa_type = models.CharField(max_length=20, choices=VISA_TYPE_CHOICES)
    visa_expiry_date = models.DateField(null=True, blank=True)

    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField(null=True, blank=True)
    employment_status = models.CharField(
        max_length=20, choices=EMPLOYMENT_STATUS_CHOICES, default="Active"
    )
    work_location = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_code} - {self.first_name} {self.last_name}"
