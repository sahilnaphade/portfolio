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
    passingYear = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100)
    additional_desc = models.TextField(null=True, blank=True)

    def add_edu(self):
        self.save()

    def __str__(self):
        return self.degree + " at " + self.university

class publication(models.Model):
    title = models.CharField(max_length=100)
    journalName = models.CharField(max_length=100)
    dateOfPub = models.DateField(null=True)
    DOI = models.CharField(max_length=100)
    link = models.CharField(max_length=150)
    indexing = models.CharField(max_length=50, null=True)
    ISSN = models.CharField(max_length=20, null=True)
    beginPage = models.IntegerField(default=0)
    endPage = models.IntegerField(default=0)

    def add_pub(self):
        self.save()
    
    def __str__(self):
        return self.title + " in " + self.journalName

class extracurricular(models.Model):
    org = models.CharField(max_length=100)
    title = models.CharField(max_length=75)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    description = models.TextField()

    def add_ec(self):
        self.save()

    def __str__(self):
        return self.title + " at " + self.org 
