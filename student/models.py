from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    study_hours=models.FloatField()
    attendance=models.FloatField()
    previous_score=models.FloatField()
    result=models.CharField(max_length=50)

    def __str__(self):
        return self.name

