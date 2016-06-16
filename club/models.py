from django.db import models
from datetime import date

class Training(models.Model):
    STATE = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
       
    training_name = models.CharField(max_length = 50)
    training_desc = models.ForeignKey('TrnDesc')
    instructor = models.ForeignKey('Instructor')
    start_time = models.TimeField(blank = True)
    end_time = models.TimeField(default = '00:00:00')
    availability = models.IntegerField(default = 15)
    state = models.CharField(max_length = 1,choices = STATE, default = 'A')
    date = models.DateField(default = date.today)
    
    def __str__(self):
        return self.training_name


class Instructor(models.Model):
    instructor_name = models.CharField(max_length=30)

    def __str__(self):
        return self.instructor_name
    

class TrnDesc(models.Model):
    tr_name = models.CharField(max_length = 50)
    tr_desc = models.CharField(max_length = 200)

    def __str__(self):
        return self.tr_desc

   



    

    




        
