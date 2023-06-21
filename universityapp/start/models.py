from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Prestige(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prestige = models.ForeignKey(Prestige, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
