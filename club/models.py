"""This is a module to create tables for fitness club"""
from datetime import date
from django.db import models

class Training(models.Model):
    """Class for plan training"""
    STATE = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    name = models.ForeignKey('TrnDesc')
    instructor = models.ForeignKey('Instructor')
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(default='00:00:00')
    availability = models.IntegerField(default=15)
    state = models.CharField(max_length=1, choices=STATE, default='A')
    training_date = models.DateField(default=date.today)
    def __str__(self):
        return self.name.name

class Instructor(models.Model):
    """Class for dictionary with instructors"""
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class TrnDesc(models.Model):
    """Class for dictionary with names of trainings along with descriptions"""
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Participant(models.Model):
    """Data of people which book fitness classes"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    training = models.ForeignKey('Training')
    def __str__(self):
        return self.training.name.name
