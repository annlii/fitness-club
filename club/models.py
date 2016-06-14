from django.db import models

# Create your models here.

class Training(models.Model):
    STATE = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wnd', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    training_name = models.CharField(max_length = 50)
    training_description = models.CharField(max_length = 200)
    instructor = models.ForeignKey('Instructor')
    start_time = models.TimeField(blank = True)
    end_time = models.TimeField(default = '00:00:00')
    availability = models.IntegerField(default = 15)
    state = models.CharField(max_length = 1, choices = STATE, default = 'A')
    day_of_week = models.CharField(max_length = 3, choices = DAYS, default = 'Mon')
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.training_name


class Instructor(models.Model):
    instructor_name = models.CharField(max_length=30)

    def publish(self):
        self.save()

    def __str__(self):
        return self.instructor_name

    def __unicode__(self):
        return self.instructor_name
