from django.db import models

# Create your models here.
class wadu(models.Model):

    Title = models.CharField(max_length=100)
    Titleinarabic = models.CharField(max_length=5000)

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=5000)
    descriptioninarabic = models.CharField(max_length=5000)
