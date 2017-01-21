from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.full_name

class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
	flat_number = models.CharField(max_length=25)
    person = models.OneToOneField(Person, null=True)
     def __unicode__(self):
        return self.street
class TechnicalSkills(models.Model):
    technology_name = models.CharField(max_length=200)
	 description = models.TextField(blank=True)
	
class Education(models.Model):
    School = models.CharField(max_length=100)
	Intermediate=models.CharField(max_length=100)
	Degree=models.CharField(max_length=100)
	start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
class Projects(models.Model): 
    name = models.CharField(maxlength=100)
	description = models.CharField(max_length=200)
	startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
	link = models.URLField(blank=True, null=True)
	
	
	
		
		
		
		
		
		
