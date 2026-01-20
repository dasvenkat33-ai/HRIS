from django.db import models

# Create your models here.
from django.db import models
from employees.models import Employee


class SalaryStructure(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    transport_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    other_allowances = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    effective_from = models.DateField()

    def __str__(self):
        return f"Salary Structure for {self.employee.employee_code}"
