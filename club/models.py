from django.db import models

# Create your models here.

class Training(models.Model):
    training_name = models.CharField(max_length=50)
    training_description = models.CharField(max_length=200)
    instructor = models.CharField(max_length=30)
    time = models.TimeField(blank=True)
    availability = models.IntegerField(default=15)

    def publish(self):
        self.save()

    def __str__(self):
        return self.training_name
