from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField(null=True, blank=True)
    def __str__(self):
        return "%s"%(self.name)
