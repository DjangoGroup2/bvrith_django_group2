from django.db import models

class faculty(models.Model):
fid = models.CharField(max_length=9, primary_key=True)


class student(models.model):
student_Id = models.ForeignKey(personalInfo, on_delete = models.CASCADE)

class Suggestion(models.model):
suggestion = models.CharField(max_length = 100)

class Notification(models.Model):
company_name = models.CharField(max_length=500)
date = models.TextField()
notification = models.CharField(max_length = 100)


