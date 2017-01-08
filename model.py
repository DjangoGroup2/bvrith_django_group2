from django.db import models
class faculty(models.Model):
        fid = models.CharField(max_length=9, primary_key=True)
        fname = models.CharField(max_length=40)

        def __unicode__(self):
               return u'%s, %s' % (self.fid, self.fname)


class course(models.Model):
        cnum = models.CharField(max_length=9, primary_key=True)
        cname = models.CharField(max_length=40)
        credits = models.IntegerField()


        def __unicode__(self):
               return u'%s, %s, %s' %(self.cnum, self.cname, self.credits)
class section(models.Model):
        snum = models.CharField(max_length=9, primary_key=True)
        cnum = models.ForeignKey(course, db_column='cnum')
        fid = models.ForeignKey(faculty, db_column='fid')
        semester = model
        s.CharField(max_length=6)
        year = models.IntegerField()
        enrollment = models.IntegerField()
        capacity = models.IntegerField()
        
        def __unicode__(self):
               return u'%s, %s' % (self.snum, self.enrollment) 


//settings.py//related to database

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'sis'
DATABASE_USER = 'micsuser'
DATABASE_PASSWORD = 'micspass' 
