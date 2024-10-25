from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Worker(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define id as primary key and auto-increment
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    salary_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100)
    doj = models.DateField()  # Date of joining
    is_active = models.BooleanField(default=True)
    mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
