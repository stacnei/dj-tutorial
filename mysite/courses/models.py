import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Courses(models.Model):
    index_number = models.AutoField(primary_key=True)
    #index_str = models.CharField(max_length=10 , default=(index_number), editable=False)
    #index_str = models.CharField(max_length=10 , editable=False)
    #index_str = models.CharField(max_length=10)
    course = models.CharField(max_length=30)
    distance = models.IntegerField()
    all_tur = models.CharField(max_length=30,default = 't',choices=(('a','a'),('t','t')))
    inn_out = models.CharField(max_length=30,default = '-',choices=(('o','o'),('i','i'),('-','-')))
    str_rnd = models.CharField(max_length=30,default = 'r',choices=(('s','s'),('r','r')))
    friendly_course = models.CharField(max_length=30)
    friendly_distance = models.CharField(max_length=30)
    c_d_attr = models.IntegerField()
    c_d_offs = models.IntegerField()
    m = models.FloatField()
    c = models.FloatField()
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        string = str(self.friendly_course) + ' ' + str(self.friendly_distance)
        return string

    class Meta:
        ordering = ['course','distance']
        verbose_name = 'Course'
