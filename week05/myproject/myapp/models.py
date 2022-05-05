from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title=models.CharField(max_length=20, null=True, blank=True)
    description=models.CharField(max_length=100, null=True, blank=True)
    image=models.ImageField(upload_to='myimages')
    def __str__(self):
        return "pk:%s title:%s"%(self.pk, self.title)

class Board(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    owner = models.ForeignKey( User, on_delete=models.CASCADE)
    def __str__(self):
        return "title:%s"%(self.pk, self.title)

class Pin(models.Model):
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)