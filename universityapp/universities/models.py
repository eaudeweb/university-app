from django.db import models

class University(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    details = models.CharField(max_length=1000)
    duration = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    image = models.ImageField(upload_to="universities/")

    def __str__(self):
        return self.name