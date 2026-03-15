from django.db import models

class Institutes(models.Model):
    institute_id = models.IntegerField()
    name = models.CharField(max_length=100)
    no_of_courses = models.IntegerField()

    def __str__(self):
        return self.name