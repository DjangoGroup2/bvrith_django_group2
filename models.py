from django.db import models
class personalInfo(models.Model):
    rollNo = models.TextField(max_length = 20, primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    address = models.TextField(max_length = 80)
    email = models.EmailField(max_length = 80)
    phone_no = models.IntegerField(max_length = 10)
class academicInfo(models.Model):
    student_Id = models.ForeignKey(personalInfo, on_delete = models.CASCADE)
    yearOfJoining = models.IntegerField(max_length = 4)
    aggregate = models.IntegerField(max_length = 10)
    upperSecondaryInst = models.CharField(max_length = 10)
    upperSecondaryBoard = models.CharField(max_length = 10)
    upperSecondaryPercentage = models.IntegerField(max_length = 10)
    SecondaryInst = models.CharField(max_length = 10)
    SecondaryBoard = models.CharField(max_length = 10)
    SecondaryPercentage = models.IntegerField(max_length = 10)
class additionalInfo(models.Model):
    studentId = models.ForeignKey(personalInfo, on_delete = models.CASCADE)
    coAcademicActivities = models.CharField(max_length = 30)
    details = models.TextField(max_length = 30)
    coCurriculars = models.CharField(max_length = 30)
    hobbies = models.CharField(max_length = 20)
class Notifications(models.Model):
    studentId = models.ForeignKey(personalInfo, on_delete = models.CASCADE)
    date = models.TextField()
    notification = models.CharField(max_length = 50)
	hvhvjh
		
		
		
		
		
		
