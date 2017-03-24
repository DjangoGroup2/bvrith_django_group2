from django.db import models

# Create your models here.

class TPO_Venue(models.Model):
	tpo_venue  = models.CharField(max_length=200)
	tpo_date  = models.DateTimeField('tpo date')
	tpo_time = models.DateTimeField('tpo time')
	tpo_no_of_students = models.IntegerField(default=0)
	def __str__(self):
        	return self.tpo_venue

class TPO_Org(models.Model):
	tpo_org_name  = models.CharField(max_length=200)
	tpo_org_mode  = models.CharField(max_length=200)
	tpo_org_btech_pctg = models.IntegerField(default=0)
	tpo_venue = models.ForeignKey(TPO_Venue)
	def __str__(self):
        	return self.tpo_org_name

class Student(models.Model):
	student_roll_no = models.IntegerField(default=0)
	student_name  = models.CharField(max_length=200)
	student_percentage  = models.IntegerField(default=0)
	student_backlogs = models.IntegerField(default=0)
	def __str__(self):
        	return self.student_name


