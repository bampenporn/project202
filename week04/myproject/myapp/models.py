from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return "Student id:%s, name:%s "\
        %(self.id,self.name)



