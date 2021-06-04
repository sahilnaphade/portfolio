from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class experience(models.Model):
    title = models.CharField(max_length=75)
    company = models.CharField(max_length=75)
    location = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    description = models.TextField()

    def add_experience(self):
        self.save()

    def __str__(self):
        return self.title + " at " +self.company

class education(models.Model):
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=20)
    specialization = models.CharField(max_length=50)
    grade = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    additional_desc = models.TextField(null=True, blank=True)

    def add_edu(self):
        self.save()

    def __str__(self):
        return self.degree + " at " + self.university