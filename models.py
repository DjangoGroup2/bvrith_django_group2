from django.db import models

class Notification(models.Model):
    student = models.ForeignKey(student,max_length=50)
    company_name = models.CharField(max_length=500)

class Drive(models.Model):
    company_name = models.CharField(max_length=500)
    release_date = models.DateField()
    num_stars = models.IntegerField()