from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    # Add more fields as needed

    def __str__(self):
        return self.name