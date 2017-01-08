from django.db import models

class tpo(models.Model):
	rollno = models.CharField(max_length = 10)
	name = models.CharFeild(max_length = 30)
	mail = models.CharFeild(max_length = 50)
	phonenumber = models.IntegerField()

	class Meta:
		db_table = "tpomodule"
